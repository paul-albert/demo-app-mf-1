from flask import jsonify, make_response, request
from flask_api import status

from models import Service, db, DatabaseException
from . import controllers


@controllers.route('/services/', methods=['GET'])
def get_services():
    services = [s for s in Service.query.order_by(Service.id).all()]
    services = [dict(s.to_dict(), horse_name=s.get_horse()['name']) for s in services]
    response_status = status.HTTP_200_OK
    return make_response(jsonify({
        'services': services,
    }), response_status)


@controllers.route('/services/<int:id>', methods=['GET'])
def get_service(id):
    service = Service.query.get(id)
    horse = service.get_horse() if service is not None else None
    horses_list = service.get_horses_list()
    service = service.to_dict() if service is not None else None
    response_status = status.HTTP_200_OK
    return make_response(jsonify({
        'service': service,
        'service_horse': horse,
        'horses_list': horses_list,
    }), response_status)


@controllers.route('/services/<int:id>', methods=['DELETE'])
def delete_service(id):
    service = Service.query.get(id)
    if service is not None:
        try:
            db.session.delete(service)
            db.session.commit()
            message = 'Service {:d} was deleted.'.format(id)
            response_status = status.HTTP_204_NO_CONTENT
        except DatabaseException as e:
            db.session.rollback()
            message = str(e)
            response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        message = 'Service {:d} is not found.'.format(id)
        response_status = status.HTTP_404_NOT_FOUND
    return make_response(jsonify({
        'message': message,
    }), response_status)


@controllers.route('/services/<int:id>', methods=['PUT'])
def update_service(id):
    service = Service.query.get(id)
    if service is not None:
        try:
            service.save(request.json)
            db.session.commit()
            message = 'Service {:d} was updated.'.format(id)
            response_status = status.HTTP_200_OK
        except DatabaseException as e:
            db.session.rollback()
            message = str(e)
            response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        message = 'Service {:d} is not found.'.format(id)
        response_status = status.HTTP_404_NOT_FOUND
    return make_response(jsonify({
        'message': message,
        'service': service.to_dict(),
    }), response_status)


@controllers.route('/services/', methods=['POST'])
def create_service():
    service = Service()
    try:
        service.save(request.json)
        db.session.add(service)
        db.session.commit()
        message = 'Service {:d} was created.'.format(service.id)
        response_status = status.HTTP_201_CREATED
    except DatabaseException as e:
        db.session.rollback()
        message = str(e)
        response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
    return make_response(jsonify({
        'message': message,
        'service': service.to_dict(),
    }), response_status)
