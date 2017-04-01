import json
from flask import Blueprint, Response

controllers = Blueprint('controllers', __name__)

def response(data, status):
    return Response(response=json.dumps(data),
                    status=status,
                    mimetype='application/json')

from .clients import *
from .horses import *
from .locations import *
from .medications import *
from .services import *
