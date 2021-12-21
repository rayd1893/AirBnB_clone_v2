#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City')