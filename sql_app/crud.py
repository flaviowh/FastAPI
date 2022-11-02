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

def update_pokemon(db: Session, old_pokemon, pokemon: schemas.Pokemon):
    old_pokemon.update({"name": pokemon.name, "description": pokemon.description, "type": pokemon.type})
    db.commit()
    return old_pokemon
    
# @app.put("/deposit/{id}")
# def deposit(id, request:schemas.PaymentRequest, db:Session=Depends(get_db)):
#     old_account = db.query(models.Account).filter(models.Account.id == id)
#     if not old_account.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'old_account with the id {id} is not available')
#     old_account.update({'name':name, 'deposits_made':deposits_made, 'total ':total})
#     db.commit()
#     return {"code":"success","message":"donation made"}

# def get_trainer(db: Session, trainer_id: int):
#     return db.query(models.Trainer).filter(models.Trainer.id == trainer_id).first()


# def get_trainer_by_name(db: Session, name: str):
#     return db.query(models.Trainer).filter(models.Trainer.name == name).first()


# def get_trainers(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Trainer).offset(skip).limit(limit).all()


# def create_trainer(db: Session, trainer: schemas.TrainerCreate):
#     db_trainer = models.Trainer(name=trainer.name, bio=trainer.bio)
#     db.add(db_trainer)
#     db.commit()
#     db.refresh(db_trainer)
#     return db_trainer


# def get_pokemon(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Pokemon).offset(skip).limit(limit).all()


# def create_pokemon(db: Session, pokemon: schemas.PokemonCreate):
#     db_pokemon = models.Pokemon(**pokemon.dict())
#     db.add(db_pokemon)
#     db.commit()
#     db.refresh(db_pokemon)
#     return db_pokemon
