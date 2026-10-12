#!/usr/bin/python3
"""Defines the State class."""

from sqlalchemy import Column, String
from models.base_model import BaseModel


class State(BaseModel):
    """Defines a State."""

    __tablename__ = "states"

    name = Column(String(128), nullable=False, default="")
