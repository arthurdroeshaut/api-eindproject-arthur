import random
from passlib.hash import pbkdf2_sha256
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import ValidationError
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import auth
import models
import crud
import schemas
from schemas import CharacterCreate, Character, MovieCreate, Movie, VehicleCreate, Vehicle
from database import SessionLocal, engine
import os


if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

# "sqlite:///./sqlitedb/sqlitedata.db"
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "https://localhost.tiangolo.com",
    "http://127.0.0.1:5500",
    "https://arthurdroeshaut.github.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# api routes


# token route
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Try to authenticate the user
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # Add the JWT case sub with the subject(user)
    access_token = auth.create_access_token(
        data={"sub": user.email}
    )
    # Return the JWT as a bearer token to be placed in the headers
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/users/create", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    users = crud.get_user(db, skip=skip, limit=limit)
    return users


# alle get routes


@app.get("/characters/random/name")
def get_random_character_name(db: Session = Depends(get_db)):
    character_count = db.query(models.Character).count()
    random_character_id = random.randint(1, character_count)
    random_character = db.query(models.Character).filter(models.Character.id == random_character_id).first()
    if random_character is None:
        return "No characters found in the database"
    return random_character.name


@app.get("/movies/random/title")
def get_random_movie_title(db: Session = Depends(get_db)):
    movie_count = db.query(models.Movie).count()
    random_movie_id = random.randint(1, movie_count)
    random_movie = db.query(models.Movie).filter(models.Movie.id == random_movie_id).first()
    if random_movie is None:
        return "No movies found in the database"
    return random_movie.title


@app.get("/vehicles/random/type")
def get_random_vehicle_type(db: Session = Depends(get_db)):
    vehicle_count = db.query(models.Vehicle).count()
    random_vehicle_type = random.randint(1, vehicle_count)
    random_vehicle = db.query(models.Vehicle).filter(models.Vehicle.type == random_vehicle_type).first()
    if random_vehicle is None:
        return "No vehicles found in the database"
    return random_vehicle.type


# alle post routes


@app.post("/characters")
def create_character(character: CharacterCreate, db: Session = Depends(get_db)):
    db_character = models.Character(**character.dict())
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    return db_character


@app.post("/vehicles")
def create_vehicle(vehicle: VehicleCreate, db: Session = Depends(get_db)):
    new_vehicle = models.Vehicle(**vehicle.dict())
    db.add(new_vehicle)
    db.commit()
    db.refresh(new_vehicle)
    return new_vehicle


@app.post("/movies")
def create_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    new_movie = models.Movie(**movie.dict())
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie


# om een karakter met een bepaald ID te updaten


@app.put("/characters/{character_id}")
def update_character(characterid: int, character: models.CharacterUpdateSchema):
    try:
        # Update character in database
        updated_character = models.CharacterUpdateSchema(**character.dict())
        return updated_character
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=e.errors())


# om een voertuig te verwijderen op basis van zijn ID


@app.delete("/vehicles/{vehicle_id}")
def delete_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    vehicle = db.query(models.Vehicle).filter(models.Vehicle.id == vehicle_id).first()
    if vehicle:
        db.delete(vehicle)
        db.commit()
        return {"message": "Successfully deleted vehicle."}
    else:
        return {"message": "Vehicle not found."}
