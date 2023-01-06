from pip._internal.network import auth
from sqlalchemy.orm import Session
from models import Movie, Character, Vehicle
from schemas import CharacterCreate, Character, MovieCreate, Movie, Vehicle, VehicleCreate
import models
import schemas
import auth

# de create user voor hashing


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# alle Create Read Update Deletes voor karakters


def get_character(db: Session, character_id: int):
    return db.query(Character).filter(Character.id == character_id).first()


def create_character(db: Session, character: CharacterCreate):
    db_character = Character(**character.dict())
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    return db_character


def update_character(db: Session, character: Character, character_update: models.CharacterUpdate):
    character.name = character_update.name
    character.species = character_update.species
    character.birthplace = character_update.birthplace
    character.lightsaber_color = character_update.lightsaber_color
    db.add(character)
    db.commit()
    db.refresh(character)
    return character


def delete_character(db: Session, character: Character):
    db.delete(character)
    db.commit()

# alle CRUDs voor films


def get_movie(db: Session, movie_id: int):
    return db.query(Movie).filter(Movie.id == movie_id).first()


def create_movie(db: Session, movie: MovieCreate):
    db_movie = Movie(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie


def update_movie(db: Session, movie: Movie, movie_update: models.MovieUpdate):
    movie.title = movie_update.title
    movie.release_date = movie_update.release_date
    movie.director = movie_update.director
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return movie


def delete_movie(db: Session, movie: Movie):
    db.delete(movie)
    db.commit()

# alle CRUDs voor voertuigen


def get_vehicle(db: Session, vehicle_id: int):
    return db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()


def create_vehicle(db: Session, vehicle: VehicleCreate):
    db_vehicle = Vehicle(**vehicle.dict())
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle


def update_vehicle(db: Session, vehicle: Vehicle, vehicle_update: models.VehicleUpdate):
    vehicle.name = vehicle_update.name
    vehicle.type = vehicle_update.type
    vehicle.affiliation = vehicle_update.affiliation
    db.add(vehicle)
    db.commit()
    db.refresh(vehicle)
    return vehicle


def delete_vehicle(db: Session, vehicle: Vehicle):
    db.delete(vehicle)
    db.commit()




