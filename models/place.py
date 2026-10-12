#!/usr/bin/python3
"""Defines the Place class."""

from sqlalchemy import Column, Float, Integer, String
from models.base_model import BaseModel


class Place(BaseModel):
    """Defines a Place."""

    __tablename__ = "places"

    city_id = Column(String(60), nullable=False, default="")
    user_id = Column(String(60), nullable=False, default="")
    name = Column(String(128), nullable=False, default="")
    description = Column(String(1024), nullable=False, default="")
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False, default=0.0)
    longitude = Column(Float, nullable=False, default=0.0)
    amenity_ids = []
