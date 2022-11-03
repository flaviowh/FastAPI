from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session, joinedload

from . import crud, models, schemas
from .database import SessionLocal, engine

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

@app.post("/pokemons/", response_model=schemas.Pokemon)
def create_pokemon(pokemon: schemas.PokemonCreate, db: Session = Depends(get_db)):
    db_pokemon = crud.get_pokemon_by_name(db=db, pokemon_name=pokemon.name)
    if db_pokemon:
        raise HTTPException(status_code=400, detail="Pokemon already added.")
    return crud.add_pokemon(db=db, pokemon=pokemon)

@app.put("/pokemons/{pokemon_id}", response_model=schemas.Pokemon)
def update_pokemon(pokemon_id : int, pokemon: schemas.PokemonCreate, db: Session = Depends(get_db)):
    old_pokemon = crud.get_pokemon_by_id(db=db, pokemon_id= pokemon_id)
    if not old_pokemon:
        raise HTTPException(status_code=400, detail="Pokemon not found by ID. Try adding it.")

    old_pokemon.name = pokemon.name
    old_pokemon.type = pokemon.type
    old_pokemon.description = pokemon.description
  
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
def create_trainer(trainer: schemas.TrainerCreate, db: Session = Depends(get_db)):
    db_trainer = crud.get_trainer_by_name(db=db, trainer_name=trainer.name)
    if db_trainer:
        raise HTTPException(status_code=400, detail="Trainer already added.")
    return crud.add_trainer(db=db, trainer=trainer)

@app.put("/trainers/{trainer_id}", response_model=schemas.Trainer)
def update_trainer(trainer_id : int, trainer: schemas.TrainerCreate, db: Session = Depends(get_db)):
    old_trainer = crud.get_trainer_by_id(db=db, trainer_id= trainer_id)
    if not old_trainer:
        raise HTTPException(status_code=400, detail="Trainer not found by ID. Try adding it.")

    old_trainer.name = trainer.name
    old_trainer.bio = trainer.bio

    db.commit()
    return old_trainer

