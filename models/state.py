#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', back_populates='state',
                              cascade='delete')
    else:
        name = ""

        @property
        def cities(self):
            from models import storage, City
            res = []
            for c in storage.all(City).values():
                if c.id == self.id:
                    res.append(c)
            return res
