from flask import jsonify, make_response, request
from flask_api import status

from models import Location, db, DatabaseException
from . import controllers


@controllers.route('/locations/', methods=['GET'])
def get_locations():
    locations = [l.to_dict() for l in Location.query.all()]
    response_status = status.HTTP_200_OK
    return make_response(jsonify({
        'locations': locations,
    }), response_status)


@controllers.route('/locations/<int:id>', methods=['GET'])
def get_location(id):
    location = Location.query.get(id)
    horse = location.get_horse() if location is not None else None
    horses_list = location.get_horses_list()
    location = location.to_dict() if location is not None else None
    response_status = status.HTTP_200_OK
    return make_response(jsonify({
        'location': location,
        'location_horse': horse,
        'horses_list': horses_list,
    }), response_status)


@controllers.route('/locations/<int:id>', methods=['DELETE'])
def delete_location(id):
    location = Location.query.get(id)
    if location is not None:
        try:
            db.session.delete(location)
            db.session.commit()
            message = 'Location {:d} was deleted.'.format(id)
            response_status = status.HTTP_204_NO_CONTENT
        except DatabaseException as e:
            db.session.rollback()
            message = str(e)
            response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        message = 'Location {:d} is not found.'.format(id)
        response_status = status.HTTP_404_NOT_FOUND
    return make_response(jsonify({
        'message': message,
    }), response_status)


@controllers.route('/locations/<int:id>', methods=['PUT'])
def update_location(id):
    location = Location.query.get(id)
    if location is not None:
        try:
            location.save(request.json)
            db.session.commit()
            message = 'Location {:d} was updated.'.format(id)
            response_status = status.HTTP_200_OK
        except DatabaseException as e:
            db.session.rollback()
            message = str(e)
            response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        message = 'Location {:d} is not found.'.format(id)
        response_status = status.HTTP_404_NOT_FOUND
    return make_response(jsonify({
        'message': message,
        'location': location.to_dict(),
    }), response_status)


@controllers.route('/locations/', methods=['POST'])
def create_location():
    location = Location()
    try:
        location.save(request.json)
        db.session.add(location)
        db.session.commit()
        message = 'Location {:d} was created.'.format(location.id)
        response_status = status.HTTP_201_CREATED
    except DatabaseException as e:
        db.session.rollback()
        message = str(e)
        response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
    return make_response(jsonify({
        'message': message,
        'location': location.to_dict(),
    }), response_status)
