from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from .credentials import Token, Credentials, authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, get_current_active_user
from . import crud, models, schemas
from .database import SessionLocal, engine

from datetime import datetime, timedelta
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/pokemons/", response_model=list[schemas.Pokemon])
def read_pokemons(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pokemons = crud.get_all_pokemons(db = db, skip=skip, limit=limit)
    return pokemons

@app.get("/pokemons/{pokemon_id}")
def get_pokemon(pokemon_id:int, db: Session = Depends(get_db)):
    db_pokemon = crud.get_pokemon_by_id(db, pokemon_id)
    return db_pokemon


@app.get("/pokemons/search/{pokemon_name}")
def get_pokemon(pokemon_name:str, db: Session = Depends(get_db)):
    db_pokemon = crud.get_pokemon_by_name(db, pokemon_name)
    return db_pokemon


@app.put("/pokemons/{pokemon_id}", response_model=schemas.Pokemon)
def update_pokemon(pokemon_id : int, pokemon: schemas.PokemonCreate, db: Session = Depends(get_db)):
    old_pokemon = crud.get_pokemon_by_id(db=db, pokemon_id= pokemon_id)
    if not old_pokemon:
        raise HTTPException(status_code=400, detail="Pokemon not found by ID. Try adding it.")

    old_pokemon.name = pokemon.name
    old_pokemon.types = pokemon.types
    old_pokemon.description = pokemon.description
    old_pokemon.is_legendary = pokemon.is_legendary
    old_pokemon.abilities = pokemon.abilities
    old_pokemon.generation = pokemon.generation
    
    db.commit()
    return old_pokemon


##  TRAINERS


@app.get("/trainers/", response_model=list[schemas.Trainer])
def read_trainers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    trainers = crud.get_all_trainers(db = db, skip=skip, limit=limit)
    return trainers   


@app.get("/trainers/{trainer_id}")
def get_trainer(trainer_id:int, db: Session = Depends(get_db)):
    db_trainer = crud.get_trainer_by_id(db, trainer_id)
    return db_trainer

@app.get("/trainers/search/{trainer_name}")
def search_trainer(trainer_name:str, db: Session = Depends(get_db)):
    db_trainer = crud.get_trainer_by_name(db, trainer_name)
    return db_trainer

@app.post("/trainers/", response_model=schemas.Trainer)
def create_trainer(trainer: schemas.TrainerCreate, db: Session = Depends(get_db), login = Depends(get_current_active_user)):
    #if authenticate_user(trainer.username, trainer.password):
    
    db_trainer = crud.get_trainer_by_name(db=db, trainer_name=trainer.name)
    if db_trainer:
        raise HTTPException(status_code=400, detail="Trainer already added.")
    return crud.add_trainer(db=db, trainer=trainer)
   # raise HTTPException(status_code=401, detail= "Username and password not valid.")

@app.put("/trainers/{trainer_id}", response_model=schemas.Trainer)
def update_trainer(trainer_id : int, trainer: schemas.TrainerCreate, db: Session = Depends(get_db)):
    old_trainer = crud.get_trainer_by_id(db=db, trainer_id= trainer_id)
    if not old_trainer:
        raise HTTPException(status_code=400, detail="Trainer not found by ID. Try adding it.")

    old_trainer["name"]= trainer.name
    old_trainer["bio"] = trainer.bio

    db.commit()
    return old_trainer


## SECURITY 


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me/", response_model=Credentials)
async def read_users_me(current_user: Credentials = Depends(get_current_active_user)):
    return current_user
