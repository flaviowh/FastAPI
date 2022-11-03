import requests
import random
from sql_app.main import SessionLocal
from sql_app.models import Trainer, Pokemon
from sqlalchemy.orm import joinedload
import csv

pokemon_data = data = r"D:\Data for python\datasets\pokemon dataset\pokemon.csv"





# url = "http://127.0.0.1:8000/users/"

# data = {
# "owner_id": 2,
# "description": "a wild pokemon",
# "title": "squirtle",
# }

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

# pokemons = []
# with open(data,'r', encoding='utf-8') as file:
#     reader = csv.DictReader(file)
#     for poke in reader:
#         is_leg = True if poke['is_legendary'] == "1" else False
#         leg = "a legendary" if is_leg else "a"
#         types = f"{poke['type1']}, {poke['type2']}" if poke["type2"] != "" else poke["type1"]
#         size = float(poke['height_m']) if poke['height_m'] != "" else 1.4
#         size_str = ''
#         if 1.3 <= size < 5:
#             size_str = "big"
#         elif 0 <= size < 0.5:
#             size_str = "small"
#         elif 0.5 <= size < 1.3:
#             size_str = "medium sized"
#         elif 5 <= size :
#             size_str = "enormous"

#         abilities = ''.join(poke["abilities"]).replace("[","")
#         abilities = abilities.replace("]","")
#         abilities = abilities.replace("'","")
#         abilities = abilities.replace("'",'')
#         new_pokemon =  Pokemon(name = poke['name'], abilities = abilities , types = types, generation = poke['generation'], is_legendary = is_leg,
#         description = f"{leg} {size_str} {poke['type1']} {poke['classfication']}".lower())
#         pokemons.append(new_pokemon)

# pokemon1 = Pokemon(name = "Pikachu", type="Electrict", description= "a yellow pokemon")
# pokemon2 = Pokemon(name = "Squirtle", type="Aquatic", description= "a blue pokemon")

# trainer1 = Trainer(name="Ash Ketchum", bio="A boy from the city of Pallet")
# trainer2 = Trainer(name="Misty", bio="a friend of Ash's")

# trainer1.pokemons = [pokemon1, pokemon2]
# trainer2.pokemons = [pokemon2]

# db.add_all([trainer1, trainer2, pokemon1, pokemon2])

# pokemon1 = db.query(Pokemon).where(Pokemon.id == 1).one()
# for t in pokemon1.trainers:
#     print(t)
# if not pokemon1.trainers:
#     print(f"{pokemon1.name} has no trainers")
#t = db.query(Trainer).where(Trainer.id == 1).first()
#obj = {"id": t.id, "name": t.name, "bio": t.bio, "pokemons": [pokemon.name for pokemon in t.pokemons]}
#q = db.execute("SELECT id, name, bio, pokemon_id FROM trainer JOIN pokedex  WHERE(trainer.id == 1) AND trainer_id == 1").all()
# #b1 = db.query(Pokemon.name).where(Pokemon.id in t1.pokemons)
# p1 = db.query(Pokemon).where(Pokemon.id in t1.pokemons).all()
# #print(TrainerSchema.from_orm(t1).json())
#print([pokemon.name for pokemon in t.pokemons])
#print(obj)
# a = db.query(Trainer).where(Trainer.id == 1).first()
# # m = t = db.query(Trainer).where(Trainer.id == 2).first()
# # pika = db.query(Pokemon).where(Pokemon.name.like("Pikachu")).first()
# # squirtle = db.query(Pokemon).where(Pokemon.name.like("Squirtle")).first()
# # a.pokemons = [pika, squirtle]
# # m.pokemons = [squirtle]
# # brock = Trainer(name="Brock", bio="A friend of Ash's, leader of Pewter Gym")
# # onix = db.query(Pokemon).where(Pokemon.name.like("Onix")).first()
# # geodude = db.query(Pokemon).where(Pokemon.name.like("Geodude")).first()
# # brock.pokemons = [onix, geodude]
# # db.add(brock)
# new_pokes = db.query(Pokemon).where(Pokemon.name.in_(["Charmander", "Charizard", "Lapras"])).all()
# a.pokemons = a.pokemons + new_pokes
# db.commit()
# name = "pikachu"
# res = db.execute("SELECT * FROM Pokemon WHERE Pokemon.name LIKE :username ", {'username': name}).first()
# print(res)
db.close()    #{'mv': music_volume, 'ml': message_volume}