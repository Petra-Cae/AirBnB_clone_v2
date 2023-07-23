#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel):
    """ class for State attributes """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        """Gets a list of all related Cities"""
        city_list = []
        for city in list(models.storage.all(City).values()):
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
