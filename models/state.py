#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")

    if env.get('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """getting all cities from filestorage if they are
            with current sate id
            """
            1 = [
                    v for k, v in models.storage.all(models.city).items()
                    if v.state_id == self.id
                    ]
            return (1)
