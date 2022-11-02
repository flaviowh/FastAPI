from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

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

# @app.post("/trainers/", response_model=schemas.Trainer)
# def create_trainer(trainer: schemas.TrainerCreate, db: Session = Depends(get_db)):
#     db_trainer = crud.get_trainer_by_name(db, name=trainer.name)
#     if db_trainer:
#         raise HTTPException(status_code=400, detail="Trainer already registered")
#     return crud.create_trainer(db=db, trainer=trainer)

# @app.get("/trainers/", response_model=list[schemas.Trainer])
# def read_trainers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     trainers = crud.get_trainers(db, skip=skip, limit=limit)
#     return trainers


# @app.get("/trainers/{trainer_id}", response_model=schemas.Trainer)
# def read_trainer(trainer_id: int, db: Session = Depends(get_db)):
#     db_trainer = crud.get_trainer(db, trainer_id=trainer_id)
#     if db_trainer is None:
#         raise HTTPException(status_code=404, detail="Trainer not found")
#     return db_trainer


# @app.post("/trainers/{trainer_id}/pokemon/", response_model=schemas.Pokemon)
# def create_pokemon_for_trainer(
#     trainer_id: int, pokemon: schemas.PokemonCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_pokemon(db=db, pokemon=pokemon)


# @app.get("/pokemons/", response_model=list[schemas.Pokemon])
# def read_pokemon(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     pokemon = crud.get_pokemon(db, skip=skip, limit=limit)
#     return pokemon
