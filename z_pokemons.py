# FastAPI

from typing import Union
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:9595",
    "http://192.168.0.5",
    "https://192.168.0.5",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Pokemon(BaseModel):
    name: str
    level: float
    is_wild: Union[bool, None] = None


db = [
 Pokemon(name="Pikachu", level= 10),
 Pokemon(name="Squirtle", level=12), 
 Pokemon(name="Bulbasaur", level=1), 
 Pokemon(name='Charmander', level=12.0, is_wild=False)]


@app.post("/pokemons/")
async def post_pokemon(pokemon: Pokemon):
    db.append(pokemon)
    return str(db[-1])

@app.get("/")
async def read_root():
    return {"message":"Welcome to the Pokemon database :D"}

@app.get("/pokemons")
async def read_root():
    return db

@app.get("/pokemons/{pokemon_id}")
async def read_pokemon(pokemon_id: int):
    if pokemon_id < len(db):
        return {"pokemon_id": pokemon_id, "name": db[pokemon_id].name, "level": db[pokemon_id].level, "is wild": db[pokemon_id].is_wild}
    return {"pokemon_id": pokemon_id, "name": "null"}    

@app.put("/pokemons/{pokemon_id}")
def update_pokemon(pokemon_id: int, pokemon: Pokemon):
    if pokemon_id in range(len(db)):
        db[pokemon_id] = pokemon
    else:
        db.append(pokemon)
    return {"pokemon_id": pokemon_id, "name": "null"} 

@app.delete("/pokemons/del")
async def delete_pokemon(pokemon_name: str):
    for i, pok in enumerate(db):
        if pok.name == pokemon_name:
            del db[i]
            return f"pokemon {pokemon_name} is gone!"
    return {"error": f"pokemon {pokemon_name} not found!"}



if __name__ == "__main__":
    uvicorn.run(app, host="192.168.0.100", port=9595)