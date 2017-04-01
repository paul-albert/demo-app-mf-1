from sqlalchemy import Column, Sequence
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, String, Text

from . import db, MixinModel


class Client(db.Model, MixinModel):

    __tablename__ = 'clients'

    clients_id_seq = Sequence('clients_id_seq')

    id = Column('id', Integer, clients_id_seq,
                server_default=clients_id_seq.next_value(),
                primary_key=True)
    name = Column('name', String(255))
    first_name = Column('first_name', String(255))
    last_name = Column('last_name', String(255))
    city = Column('city', String(64))
    zipcode = Column('zipcode', String(32))
    street = Column('street', String(255))
    additional_address_data = Column('additional_address_data', String(255))
    phone = Column('phone', String(64))
    mobphone = Column('mobphone', String(64))
    fax = Column('fax', String(64))
    email = Column('email', String(128))
    account_type_1 = Column('account_type_1', String(64))
    owner_1 = Column('owner_1', String(255))
    account_number_1 = Column('account_number_1', String(255))
    banking_code_1 = Column('banking_code_1', String(255))
    account_type_2 = Column('account_type_2', String(64))
    owner_2 = Column('owner_2', String(255))
    account_number_2 = Column('account_number_2', String(255))
    banking_code_2 = Column('banking_code_2', String(255))
    open_stall = Column('open_stall', Integer)
    stall = Column('stall', Integer)
    coupler = Column('coupler', Integer)
    additional_info = Column('additional_info', Text)
    vet = Column('vet', String(255))
    smith = Column('smith', String(255))

    horses = relationship('Horse', backref='clients', cascade='all, delete')

    def get_horses(self):
        return [h.to_dict() for h in self.horses] if self.id is not None else []
