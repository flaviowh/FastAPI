from sqlalchemy.orm import Session

from . import models, schemas


def get_pokemon_by_id(db: Session, pokemon_id: int):
    return db.query(models.Pokemon).filter(models.Pokemon.id == pokemon_id).first()

def get_pokemon_by_name(db: Session, pokemon_name: int):
    return db.query(models.Pokemon).filter(str(models.Pokemon.name).lower() == pokemon_name.lower()).first()

def get_all_pokemons(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Pokemon).offset(skip).limit(limit).all()

def add_pokemon(db: Session, pokemon: schemas.PokemonCreate):
    db_pokemon = models.Pokemon(name= pokemon.name, type = pokemon.type, description = pokemon.description)
    db.add(db_pokemon)
    db.commit()
    db.refresh(db_pokemon)
    return db_pokemon


def get_all_trainers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Trainer).offset(skip).limit(limit).all()

def get_trainer_by_id(db: Session, trainer_id: int):
    return db.query(models.Pokemon).filter(models.Trainer.id == trainer_id).first()

def get_trainer_by_name(db: Session, trainer_name: str):
    return db.query(models.Trainer).filter(str(models.Trainer.name).lower() == trainer_name.lower()).first()

def add_trainer(db: Session, trainer: schemas.TrainerCreate):
    db_trainer = models.Trainer(name= trainer.name, bio = trainer.bio)
    db.add(db_trainer)
    db.commit()
    db.refresh(db_trainer)
    return db_trainer



