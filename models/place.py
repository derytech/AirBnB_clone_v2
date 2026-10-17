#!/usr/bin/python3
"""Defines the Place class."""

import os

from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


class Place(BaseModel, Base):
    """Defines a Place."""

    __tablename__ = "places"

    city_id = Column(
        String(60),
        ForeignKey("cities.id"),
        nullable=False,
        default=""
    )
    user_id = Column(
        String(60),
        ForeignKey("users.id"),
        nullable=False,
        default=""
    )
    name = Column(String(128), nullable=False, default="")
    description = Column(String(1024), nullable=True, default="")
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True, default=0.0)
    longitude = Column(Float, nullable=True, default=0.0)
    amenity_ids = []

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        user = relationship(
            "User",
            back_populates="places"
        )
        cities = relationship(
            "City",
            back_populates="places"
        )
