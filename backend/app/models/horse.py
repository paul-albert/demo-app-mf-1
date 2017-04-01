from sqlalchemy import Column, ForeignKey, Sequence
from sqlalchemy.orm import relationship
from sqlalchemy.types import DateTime, Enum, Integer, String

from . import db, MixinModel, Client


class Horse(db.Model, MixinModel):

    __tablename__ = 'horses'

    horses_id_seq = Sequence('horses_id_seq')

    id = Column('id', Integer, horses_id_seq,
                server_default=horses_id_seq.next_value(),
                primary_key=True)
    client_id = Column('client_id', Integer, ForeignKey('clients.id'))
    name = Column('name', String(255))
    online_number = Column('online_number', String(64))
    birth_date = Column('birth_date', DateTime)
    sex = Column(Enum('m', 'f', name='sex'))
    color = Column('color', String(32))
    arrival_date = Column('arrival_date', DateTime)
    departure_date = Column('departure_date', DateTime)
    active = Column('active', Integer)

    client = relationship('Client', foreign_keys=client_id)
    locations = relationship('Location', backref='locations', cascade='all, delete')
    medications = relationship('Medication', backref='medications', cascade='all, delete')
    services = relationship('Service', backref='services', cascade='all, delete')

    def get_client(self):
        return self.client.to_dict() if self.id is not None else None

    def get_locations(self):
        return [l.to_dict() for l in self.locations] if self.id is not None else []

    def get_medications(self):
        return [m.to_dict() for m in self.medications] if self.id is not None else []

    def get_services(self):
        return [s.to_dict() for s in self.services] if self.id is not None else []

    def get_clients_list(self):
        clients = Client.query.with_entities(Client.id, Client.name).all()
        return [{c.id: c.name} for c in clients]
