from flask import jsonify, make_response, request
from flask_api import status

from models import Client, db, DatabaseException
from . import controllers


@controllers.route('/clients/', methods=['GET'])
def get_clients():
    clients = [c.to_dict() for c in Client.query.order_by(Client.id).all()]
    response_status = status.HTTP_200_OK
    return make_response(jsonify({
        'clients': clients,
    }), response_status)


@controllers.route('/clients/<int:id>', methods=['GET'])
def get_client(id):
    client = Client.query.get(id)
    client_horses = client.get_horses() if client is not None else []
    client = client.to_dict() if client is not None else None
    response_status = status.HTTP_200_OK
    return make_response(jsonify({
        'client': client,
        'client_horses': client_horses,
    }), response_status)


@controllers.route('/clients/<int:id>', methods=['DELETE'])
def delete_client(id):
    client = Client.query.get(id)
    if client is not None:
        try:
            db.session.delete(client)
            db.session.commit()
            message = 'Client {:d} was deleted.'.format(id)
            response_status = status.HTTP_204_NO_CONTENT
        except DatabaseException as e:
            db.session.rollback()
            message = str(e)
            response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        message = 'Client {:d} is not found.'.format(id)
        response_status = status.HTTP_404_NOT_FOUND
    return make_response(jsonify({
        'message': message,
    }), response_status)


@controllers.route('/clients/<int:id>', methods=['PUT'])
def update_client(id):
    client = Client.query.get(id)
    if client is not None:
        try:
            client.save(request.json)
            db.session.commit()
            message = 'Client {:d} was updated.'.format(id)
            response_status = status.HTTP_200_OK
        except DatabaseException as e:
            db.session.rollback()
            message = str(e)
            response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        message = 'Client {:d} is not found.'.format(id)
        response_status = status.HTTP_404_NOT_FOUND
    return make_response(jsonify({
        'message': message,
        'client': client.to_dict(),
    }), response_status)


@controllers.route('/clients/', methods=['POST'])
def create_client():
    client = Client()
    try:
        client.save(request.json)
        db.session.add(client)
        db.session.commit()
        message = 'Client {:d} was created.'.format(client.id)
        response_status = status.HTTP_201_CREATED
    except DatabaseException as e:
        db.session.rollback()
        message = str(e)
        response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
    return make_response(jsonify({
        'message': message,
        'client': client.to_dict(),
    }), response_status)
