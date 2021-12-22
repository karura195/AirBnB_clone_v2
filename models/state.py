#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from models.city import City
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String


class State(BaseModel):
    """ State class """
    if models.is_db == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City')
    else:
        name = ""
        cities = models.storage.all(City)
