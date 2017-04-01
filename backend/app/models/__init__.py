from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import DatabaseError


db = SQLAlchemy()
DatabaseException = DatabaseError


class MixinModel(object):

    def to_dict(self):
        if hasattr(self, '__table__'):
            return {
                c.name: str(getattr(self, c.name))
                if getattr(self, c.name) is not None else None
                for c in self.__table__.columns
            }
        else:
            return {}

    def save(self, data):
        for k, v in dict(data).items():
            setattr(self, k, v)


from .client import Client
from .horse import Horse
from .location import Location
from .medication import Medication
from .service import Service
