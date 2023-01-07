from sqlalchemy import Column, Integer, String, Boolean
from pydantic import BaseModel

from database import Base


class Character(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    species = Column(String)
    birthplace = Column(String)
    lightsaber_color = Column(String)


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(String)
    director = Column(String)


class Vehicle(Base):
    __tablename__ = 'vehicles'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    affiliation = Column(String)

# hierna maken we alle creates aan.


class CharacterCreate(Character):
    pass


class MovieCreate(Movie):
    pass


class VehicleCreate(Vehicle):
    pass


class CharacterUpdate(Character):
    pass


class MovieUpdate(Movie):
    pass


class VehicleUpdate(Vehicle):
    pass


class CharacterUpdateSchema(BaseModel):
    id: int
    name: str
    species: str
    birthplace: str
    lightsaber_color: str


class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    is_active = Column(Boolean, default=True)
