from pydantic import BaseModel
from models import Character as CharacterModel, Movie as MovieModel, Vehicle as VehicleModel


class CharacterBase(BaseModel):
    name: str
    species: str
    birthplace: str
    lightsaber_color: str | None = None


class CharacterCreate(CharacterBase):
    pass


class Character(CharacterBase):
    id: int

    class Config:
        orm_mode = True


class MovieBase(BaseModel):
    title: str
    release_date: str
    director: str


class MovieCreate(MovieBase):
    pass


class Movie(MovieBase):
    id: int

    class Config:
        orm_mode = True


class VehicleBase(BaseModel):
    name: str
    type: str
    affiliation: str


class VehicleCreate(VehicleBase):
    pass


class Vehicle(VehicleBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
