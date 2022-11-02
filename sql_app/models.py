from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from .database import Base


class Pokemon(Base):
    __tablename__ = "pokemon"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    type = Column(String)
    description = Column(String, index=True, nullable=True)
    


# pokedex = Table(
#     "pokedex",
#     Base.metadata,
#     Column("trainer_id", ForeignKey("trainer.id"), primary_key=True),
#     Column("pokemon_id", ForeignKey("pokemon.id"), primary_key=True),
# )



# class Trainer(Base):
#     __tablename__ = "trainer"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     bio = Column(String, index=True, nullable=True)
#     pokemons =  relationship("Pokemon", secondary="pokedex", back_populates="pokemon")

    
# class Pokemon(Base):
#     __tablename__ = "pokemon"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, unique=True, index=True)
#     type = Column(String)
#     description = Column(String, index=True, nullable=True)
    
    
#     owners = relationship("Trainer", secondary="pokedex", back_populates="trainer")

