from pydantic import BaseModel

class PokemonBase(BaseModel):
    name : str
    types: str
    abilities : str
    description : str 
    is_legendary: bool
    generation: int


class TrainerBase(BaseModel):
    name: str
    bio: str | None = None


class Pokemon(PokemonBase):
    id: int
    
    
    class Config:
        orm_mode = True

class PokemonCreate(PokemonBase):
    # username: str
    # password: str
    pass



class Trainer(TrainerBase):
    id: int
    

    class Config:
        orm_mode = True

class TrainerCreate(TrainerBase):
    # username: str
    # password: str
    pass

