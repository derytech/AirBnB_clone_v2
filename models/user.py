#!/usr/bin/python3
"""Defines the User class."""

from sqlalchemy import Column, String
from models.base_model import BaseModel


class User(BaseModel):
    """Defines a User."""

    __tablename__ = "users"

    email = Column(String(128), nullable=False, default="")
    password = Column(String(128), nullable=False, default="")
    first_name = Column(String(128), nullable=False, default="")
    last_name = Column(String(128), nullable=False, default="")
