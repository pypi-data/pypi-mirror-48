#!/usr/bin/env python
from __future__ import absolute_import
import json
import traceback
from plynx.db import Node, NodeCollectionManager
from flask import request, g
from plynx.graph.base_nodes import NodeCollection
from plynx.plugins.managers import resource_manager
from plynx.web import app, requires_auth, make_fail_response
from plynx.utils.common import to_object_id, JSONEncoder
from plynx.constants import NodeStatus, NodePostAction, NodePostStatus

PAGINATION_QUERY_KEYS = {'per_page', 'offset', 'status', 'base_node_names', 'search'}

node_collection_manager = NodeCollectionManager()
node_collection = NodeCollection()


@app.route('/plynx/api/v0/nodes', methods=['GET'])
@app.route('/plynx/api/v0/nodes/<node_link>', methods=['GET'])
@requires_auth
def get_nodes(node_link=None):
    user_id = to_object_id(g.user._id)
    # if node_link is a base node
    if node_link in node_collection.name_to_class:
        return JSONEncoder().encode({
            'data': node_collection.name_to_class[node_link].get_default().to_dict(),
            'resources_dict': resource_manager.resources_dict,
            'status': 'success'})
    # if node_link is defined (Node id)
    elif node_link:
        try:
            node_id = to_object_id(node_link)
        except Exception:
            return 'Invalid ID', 404
        node = node_collection_manager.get_db_node(node_id, user_id)
        if node:
            return JSONEncoder().encode({
                'data': node,
                'resources_dict': resource_manager.resources_dict,
                'status': 'success'})
        else:
            return 'Node `{}` was not found'.format(node_link), 404
    else:
        query = json.loads(request.args.get('query', "{}"))
        nodes_query = {k: v for k, v in query.items() if k in PAGINATION_QUERY_KEYS}
        res = node_collection_manager.get_db_nodes(user_id=user_id, **nodes_query)

        return JSONEncoder().encode({
            'nodes': res['list'],
            'total_count': res['metadata'][0]['total'] if res['metadata'] else 0,
            'resources_dict': resource_manager.resources_dict,
            'status': 'success'})


@app.route('/plynx/api/v0/nodes', methods=['POST'])
@requires_auth
def post_node():
    app.logger.debug(request.data)
    try:
        body = json.loads(request.data)['body']

        node = Node.from_dict(body['node'])
        node.author = g.user._id
        node.starred = False
        db_node = node_collection_manager.get_db_node(node._id, g.user._id)
        if db_node and db_node['_readonly']:
            return make_fail_response('Permission denied'), 403

        action = body['action']
        if action == NodePostAction.SAVE:
            if node.node_status != NodeStatus.CREATED and node.base_node_name != 'file':
                return make_fail_response('Cannot save node with status `{}`'.format(node.node_status))

            node.save(force=True)

        elif action == NodePostAction.APPROVE:
            if node.node_status != NodeStatus.CREATED:
                return make_fail_response('Node status `{}` expected. Found `{}`'.format(NodeStatus.CREATED, node.node_status))
            validation_error = node.get_validation_error()
            if validation_error:
                return JSONEncoder().encode({
                    'status': NodePostStatus.VALIDATION_FAILED,
                    'message': 'Node validation failed',
                    'validation_error': validation_error.to_dict()
                })

            node.node_status = NodeStatus.READY
            node.save(force=True)

        elif action == NodePostAction.VALIDATE:
            validation_error = node.get_validation_error()

            if validation_error:
                return JSONEncoder().encode({
                    'status': NodePostStatus.VALIDATION_FAILED,
                    'message': 'Node validation failed',
                    'validation_error': validation_error.to_dict()
                })
        elif action == NodePostAction.DEPRECATE:
            if node.node_status == NodeStatus.CREATED:
                return make_fail_response('Node status `{}` not expected.'.format(node.node_status))

            node.node_status = NodeStatus.DEPRECATED
            node.save(force=True)
        elif action == NodePostAction.MANDATORY_DEPRECATE:
            if node.node_status == NodeStatus.CREATED:
                return make_fail_response('Node status `{}` not expected.'.format(node.node_status))

            node.node_status = NodeStatus.MANDATORY_DEPRECATED
            node.save(force=True)
        elif action == NodePostAction.PREVIEW_CMD:
            job = node_collection.make_job(node)

            return JSONEncoder().encode(
                {
                    'status': NodePostStatus.SUCCESS,
                    'message': 'Successfully created preview',
                    'preview_text': job.run(preview=True)
                })

        else:
            return make_fail_response('Unknown action `{}`'.format(action))

        return JSONEncoder().encode(
            {
                'status': NodePostStatus.SUCCESS,
                'message': 'Node(_id=`{}`) successfully updated'.format(str(node._id))
            })
    except Exception as e:
        app.logger.error(traceback.format_exc())
        return make_fail_response('Internal error: "{}"'.format(str(e)))
