#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base     
from sqlalchemy.orm import relationship 
from sqlalchemy import Column, Integer, String
from models.base_model import Base
from  os import  getenv

class State(BaseModel, Base):
    """ State class """

    if getenv("HBNB_TYPE_STORAGE") != "db":
        name = ""
        state_id = ""
        @property
        def cities(self):
            """ Getter attribute that connects relationship with City """
            from models import storage
            from models.city import City
            city_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
    else:
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="delete")
