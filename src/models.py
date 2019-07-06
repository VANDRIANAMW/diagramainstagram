import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    correo = Column(String(250), nullable=False)

class Sigue(Base):
    __tablename__ = 'sigue'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id_seguidor = Column(Integer, ForeignKey('person.id'), primary_key=True)
    id_seguido = Column(Integer, ForeignKey('person.id'), primary_key=True)
    person = relationship(Person)

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    fecha_post = Column(String(250))
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

class Megusta(Base):
    __tablename__ = 'megusta'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    fecha_megusta = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'))
    person_id = Column(Integer, ForeignKey('person.id'))
    post = relationship(Post)
    person = relationship(Person)

class Comentarios(Base):
    __tablename__ = 'comentarios'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    fecha_comentario = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'))
    person_id = Column(Integer, ForeignKey('person.id'))
    post = relationship(Post)
    person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')