#!/usr/bin/python3
"""This module defines a class User"""
from os import lseek
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
import models


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    if models.type_storage == "db":
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)

        places = relationship("Place")
        reviews = relationship("Review")
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
