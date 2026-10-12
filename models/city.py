#!/usr/bin/python3
"""Defines the City class."""

from sqlalchemy import Column, String
from models.base_model import BaseModel


class City(BaseModel):
    """Defines a City."""

    __tablename__ = "cities"

    state_id = Column(String(60), nullable=False, default="")
    name = Column(String(128), nullable=False, default="")
