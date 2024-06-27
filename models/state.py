#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from models import storage_type
from .city import City

if storage_type == 'db':
    class State(BaseModel, Base):
        """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship('City', back_popoulates="cities, backref="state",
                          cascade="all, delete-orphan"")

else:
    class State(BaseModel):
        """Attributes:
        name (str): The name of the state.
        """

        name = ""

        @property
        def cities(self):
            from models import storage
            all_cities = list(storage.all(City).values())
            return list(filter((lambda c: c.state_id == self.id), all_cities)

        @getter
        def cities(self):
        """
        gets the list of city instances
        """
        return ("cities where state_id = State.id")
