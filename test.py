import requests
import random
from sql_app.main import SessionLocal
from sql_app.models import Trainer, Pokemon
from sqlalchemy.orm import joinedload




url = "http://127.0.0.1:8000/users/"

data = {
"owner_id": 2,
"description": "a wild pokemon",
"title": "squirtle",
}

# response = requests.post(url, json=data)
 
# print("Status Code", response.status_code)
# print("JSON Response ", response.json())


# for n in range(100):
#     data = {
#         "email" :  f"{random.randint(0,20000)}@{random.choice(['sample','email','google'])}",
#         "password": f"{random.randint(100000,200000)}"
#     }
#     requests.post(url, json=data)

    # id = Column(Integer, primary_key=True, index=True)
    # email = Column(String, unique=True, index=True)
    # hashed_password = Column(String)
    # is_active = Column(Boolean, default=True)


db  = SessionLocal()

# pokemon1 = Pokemon(name = "Pikachu", type="Electrict", description= "a yellow pokemon")
# pokemon2 = Pokemon(name = "Squirtle", type="Aquatic", description= "a blue pokemon")

# trainer1 = Trainer(name="Ash", bio="A boy from the city of Pallet")
# trainer2 = Trainer(name="Misty", bio="a friend of Ash's")

# trainer1.pokemons = [pokemon1, pokemon2]
# trainer2.pokemons = [pokemon2]

# db.add_all([trainer1, trainer2, pokemon1, pokemon2])

# pokemon1 = db.query(Pokemon).where(Pokemon.id == 1).one()
# for t in pokemon1.trainers:
#     print(t)
# if not pokemon1.trainers:
#     print(f"{pokemon1.name} has no trainers")
t = db.query(Trainer).where(Trainer.id == 1).first()
obj = {"id": t.id, "name": t.name, "bio": t.bio, "pokemons": [pokemon.name for pokemon in t.pokemons]}
#q = db.execute("SELECT id, name, bio, pokemon_id FROM trainer JOIN pokedex  WHERE(trainer.id == 1) AND trainer_id == 1").all()
# #b1 = db.query(Pokemon.name).where(Pokemon.id in t1.pokemons)
# p1 = db.query(Pokemon).where(Pokemon.id in t1.pokemons).all()
# #print(TrainerSchema.from_orm(t1).json())
#print([pokemon.name for pokemon in t.pokemons])
print(obj)

#db.commit()
db.close()    