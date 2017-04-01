from sqlalchemy import Column, ForeignKey, Sequence
from sqlalchemy.orm import relationship
from sqlalchemy.types import DateTime, Integer, String, Text

from . import db, MixinModel, Horse


class Medication(db.Model, MixinModel):

    __tablename__ = 'medications'

    medications_id_seq = Sequence('medications_id_seq')

    id = Column('id', Integer, medications_id_seq,
                server_default=medications_id_seq.next_value(),
                primary_key=True)
    horse_id = Column('horse_id', Integer, ForeignKey('horses.id'))
    medicament = Column('medicament', String(255))
    date = Column('date', DateTime)
    note = Column('note', Text)

    horse = relationship('Horse', foreign_keys=horse_id)

    def get_horse(self):
        return self.horse.to_dict() if self.id is not None else None

    def get_horses_list(self):
        horses = Horse.query.with_entities(Horse.id, Horse.name).all()
        return [{h.id: h.name} for h in horses]
