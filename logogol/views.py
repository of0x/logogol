from logogol import app

from flask import jsonify, request, url_for
from flask import json

from logogol.database import db_session
from logogol.models import Link
from logogol.error_handlers import InvalidUsage


@app.route('/links', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        request_json = request.get_json()
        if 'url' in request_json:
            link = Link(request_json['url'])
        else:
            raise InvalidUsage('url is required')
        # link.description = request_json('description')
        # link.paths = request_json('path')
        # link.tags = request_json('tags')
        db_session.add(link)
        db_session.commit()
        return jsonify(construct_dict(link))
    else:
        response = [] # paging here?
        for link in Link.query.all():
            response.append(construct_dict(link))
        return json.dumps(response)

@app.route('/links/<int:link_id>', methods=['GET', 'PATCH', 'DELETE'])
def link(link_id):
    link = Link.query.filter(Link.id == link_id).first()
    if request.method == 'PATCH':
        request_json = request.get_json()
        if 'description' in request_json:
            link.description = request_json['description']
        if 'paths' in request_json:
            link.paths = request_json['paths']
        if 'tags' in request_json:
            link.tags = request_json['tags']
        db_session.commit()
    elif request.method == 'DELETE':
        db_session.delete(link)
        db_session.commit()
        return jsonify(dict())
    if link:
        return jsonify(construct_dict(link))
    else:
        return jsonify(dict())


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


def construct_dict(link):
    return dict(description=link.description, paths=link.paths,
        url=link.url, id=link.id)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
