from flask import jsonify, make_response, request
from flask_api import status

from models import Horse, db, DatabaseException
from . import controllers


@controllers.route('/horses/', methods=['GET'])
def get_horses():
    horses = [h.to_dict() for h in Horse.query.all()]
    response_status = status.HTTP_200_OK
    return make_response(jsonify({
        'horses': horses,
    }), response_status)


@controllers.route('/horses/<int:id>', methods=['GET'])
def get_horse(id):
    horse = Horse.query.get(id)
    client = horse.get_client() if horse is not None else None
    horse_locations = horse.get_locations() if horse is not None else []
    horse_medications = horse.get_medications() if horse is not None else []
    horse_services = horse.get_services() if horse is not None else []
    clients_list = horse.get_clients_list()
    horse = horse.to_dict() if horse is not None else None
    response_status = status.HTTP_200_OK
    return make_response(jsonify({
        'horse': horse,
        'horse_client': client,
        'horse_locations': horse_locations,
        'horse_medications': horse_medications,
        'horse_services': horse_services,
        'clients_list': clients_list,
    }), response_status)


@controllers.route('/horses/<int:id>', methods=['DELETE'])
def delete_horse(id):
    horse = Horse.query.get(id)
    if horse is not None:
        try:
            db.session.delete(horse)
            db.session.commit()
            message = 'Horse {:d} was deleted.'.format(id)
            response_status = status.HTTP_204_NO_CONTENT
        except DatabaseException as e:
            db.session.rollback()
            message = str(e)
            response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        message = 'Horse {:d} is not found.'.format(id)
        response_status = status.HTTP_404_NOT_FOUND
    return make_response(jsonify({
        'message': message,
    }), response_status)


@controllers.route('/horses/<int:id>', methods=['PUT'])
def update_horse(id):
    horse = Horse.query.get(id)
    if horse is not None:
        try:
            horse.save(request.json)
            db.session.commit()
            message = 'Horse {:d} was updated.'.format(id)
            response_status = status.HTTP_200_OK
        except DatabaseException as e:
            db.session.rollback()
            message = str(e)
            response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        message = 'Horse {:d} is not found.'.format(id)
        response_status = status.HTTP_404_NOT_FOUND
    return make_response(jsonify({
        'message': message,
        'horse': horse.to_dict(),
    }), response_status)


@controllers.route('/horses/', methods=['POST'])
def create_horse():
    horse = Horse()
    try:
        horse.save(request.json)
        db.session.add(horse)
        db.session.commit()
        message = 'Horse {:d} was created.'.format(horse.id)
        response_status = status.HTTP_201_CREATED
    except DatabaseException as e:
        db.session.rollback()
        message = str(e)
        response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
    return make_response(jsonify({
        'message': message,
        'horse': horse.to_dict(),
    }), response_status)
