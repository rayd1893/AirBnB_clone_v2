#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv, name
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String
from models.base_model import BaseModel, Base
import models
from models.city import City


if getenv("HBNB_TYPE_STORAGE") == "db":
    class State(BaseModel, Base):
        """ State class """
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship('City')
else:
    class State(BaseModel):
        """ Defined class to work with FileStorage'"""
        name = ''

        @property
        def cities(self):
            '''Function getter to amenities'''
            cities = []
            l = models.storage.all(City)
            for k, v in l.items():
                if v.state_id == self.id:
                    cities.append(v)
            return cities
