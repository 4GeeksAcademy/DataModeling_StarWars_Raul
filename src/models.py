import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gravity = Column(Float, nullable=False)
    population = Column(Integer, nullable=False)
    image = Column(String(250))
    character = relationship("Character", backref = "planet", lazy =True)

# enumerate((0,"Male"),(1,"Female"),(2,"Other"))

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    specie = Column(String(250), nullable=False)
    genre = Column(String(250), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    starship = relationship("Starship", secondary="characters_starships", lazy = "subquery", backref="character")

class Starship(Base):
    __tablename__ = 'starship'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    model = Column(String(250), nullable=False)
    name = Column(String(250))
    image = Column(String(250))

class Characters_Starships(Base):
    __tablename__ = 'characters_starships'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)
    starship_id = Column(Integer, ForeignKey('starship.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
