from flask import jsonify, make_response, request
from flask_api import status

from models import Medication, db, DatabaseException
from . import controllers


@controllers.route('/medications/', methods=['GET'])
def get_medications():
    medications = [m.to_dict() for m in Medication.query.all()]
    response_status = status.HTTP_200_OK
    return make_response(jsonify({
        'medications': medications,
    }), response_status)


@controllers.route('/medications/<int:id>', methods=['GET'])
def get_medication(id):
    medication = Medication.query.get(id)
    horse = medication.get_horse() if medication is not None else None
    horses_list = medication.get_horses_list()
    medication = medication.to_dict() if medication is not None else None
    response_status = status.HTTP_200_OK
    return make_response(jsonify({
        'medication': medication,
        'medication_horse': horse,
        'horses_list': horses_list,
    }), response_status)


@controllers.route('/medications/<int:id>', methods=['DELETE'])
def delete_medication(id):
    medication = Medication.query.get(id)
    if medication is not None:
        try:
            db.session.delete(medication)
            db.session.commit()
            message = 'Medication {:d} was deleted.'.format(id)
            response_status = status.HTTP_204_NO_CONTENT
        except DatabaseException as e:
            db.session.rollback()
            message = str(e)
            response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        message = 'Medication {:d} is not found.'.format(id)
        response_status = status.HTTP_404_NOT_FOUND
    return make_response(jsonify({
        'message': message,
    }), response_status)


@controllers.route('/medications/<int:id>', methods=['PUT'])
def update_medication(id):
    medication = Medication.query.get(id)
    if medication is not None:
        try:
            medication.save(request.json)
            db.session.commit()
            message = 'Medication {:d} was updated.'.format(id)
            response_status = status.HTTP_200_OK
        except DatabaseException as e:
            db.session.rollback()
            message = str(e)
            response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        message = 'Medication {:d} is not found.'.format(id)
        response_status = status.HTTP_404_NOT_FOUND
    return make_response(jsonify({
        'message': message,
        'medication': medication.to_dict(),
    }), response_status)


@controllers.route('/medications/', methods=['POST'])
def create_medication():
    medication = Medication()
    try:
        medication.save(request.json)
        db.session.add(medication)
        db.session.commit()
        message = 'Medication {:d} was created.'.format(medication.id)
        response_status = status.HTTP_201_CREATED
    except DatabaseException as e:
        db.session.rollback()
        message = str(e)
        response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
    return make_response(jsonify({
        'message': message,
        'medication': medication.to_dict(),
    }), response_status)
