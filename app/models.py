import uuid

from sqlalchemy import Column, Float, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class City(Base):
    __tablename__ = "cities"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)

    animals = relationship("Animal", back_populates="city")


class Animal(Base):
    __tablename__ = "animals"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    animal_type = Column(String)
    breed = Column(String)
    city_id = Column(UUID(as_uuid=True), ForeignKey("cities.id"))

    city = relationship("City", back_populates="animals")

    __mapper_args__ = {"polymorphic_identity": "animal", "polymorphic_on": animal_type}


class Cat(Animal):
    __tablename__ = "cats"

    id = Column(UUID(as_uuid=True), ForeignKey("animals.id"), primary_key=True)
    favorite_fish = Column(String)

    __mapper_args__ = {"polymorphic_identity": "cat"}


class Dog(Animal):
    __tablename__ = "dogs"

    id = Column(UUID(as_uuid=True), ForeignKey("animals.id"), primary_key=True)
    bark_decibels = Column(Float)

    __mapper_args__ = {"polymorphic_identity": "dog"}

