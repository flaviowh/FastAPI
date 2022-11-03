from pydantic import BaseModel

class PokemonBase(BaseModel):
    name : str
    type: str 
    description : str | None = None

class TrainerBase(BaseModel):
    name: str
    bio: str | None = None


class Pokemon(PokemonBase):
    id: int
    
    
    class Config:
        orm_mode = True

class PokemonCreate(PokemonBase):
    pass



class Trainer(TrainerBase):
    id: int
    

    class Config:
        orm_mode = True

class TrainerCreate(TrainerBase):
    pass


# class PokemonSchema(PokemonBase):
#     trainers: list[TrainerBase]

#     class Config:
#         orm_mode = True

# class TrainerSchema(TrainerBase):
#     pokemons: list[PokemonBase]

#     class Config:
#         orm_mode = True

# class PokemonBase(BaseModel):
#     id: int
#     name: str
#     type: str
#     description: str | None = None

#     class Config:
#         orm_mode = True

# class TrainerBase(BaseModel):
#     id: int
#     name: str
#     bio: str | None = None

#     class Config:
#         orm_mode = True

# class PokemonCreate(PokemonBase):
#     name: str
#     type: str
    

# class Pokemon(PokemonBase):
#     id: int
#     type: str
#     owners: list[TrainerBase]


#     class Config:
#         orm_mode = True



# class TrainerCreate(TrainerBase):
#     name: str
#     bio: str


# class Trainer(TrainerBase):
#     id: int
#     name: str
#     bio: str

#     pokemons: list[PokemonBase]

#     class Config:
#         orm_mode = True
