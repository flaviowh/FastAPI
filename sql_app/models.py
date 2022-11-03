from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from .database import Base



pokedex = Table(
    "pokedex",
    Base.metadata,
    Column("trainer_id", ForeignKey("trainer.id"), primary_key=True),
    Column("pokemon_id", ForeignKey("pokemon.id"), primary_key=True),
)


class Trainer(Base):
    __tablename__ = "trainer"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    bio = Column(String, nullable=True)

    pokemons =  relationship("Pokemon", secondary="pokedex", back_populates="trainers")

   
    
class Pokemon(Base):
    __tablename__ = "pokemon"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable= False)
    type = Column(String, nullable= False)
    description = Column(String, index=True, nullable=True)
    
    
    trainers = relationship("Trainer", secondary="pokedex", back_populates="pokemons")


