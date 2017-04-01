from sqlalchemy import Column, ForeignKey, Sequence
from sqlalchemy.orm import relationship
from sqlalchemy.types import DateTime, Integer, Numeric, String

from . import db, MixinModel, Horse


class Service(db.Model, MixinModel):

    __tablename__ = 'services'

    services_id_seq = Sequence('services_id_seq')

    id = Column('id', Integer, services_id_seq,
                server_default=services_id_seq.next_value(),
                primary_key=True)
    horse_id = Column('horse_id', Integer, ForeignKey('horses.id'))
    active = Column('active', Integer)
    service_name = Column('service_name', String(255))
    performed_by = Column('performed_by', String(255))
    start_date = Column('start_date', DateTime)
    end_date = Column('end_date', DateTime)
    price = Column('price', Numeric(8, 2))
    account_type = Column('account_type', String(64))
    contract_number = Column('contract_number', String(255))

    horse = relationship('Horse', foreign_keys=horse_id)

    def get_horse(self):
        return self.horse.to_dict() if self.id is not None else None

    def get_horses_list(self):
        horses = Horse.query.with_entities(Horse.id, Horse.name).all()
        return [{h.id: h.name} for h in horses]
