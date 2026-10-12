#!/usr/bin/python3
"""Defines the Review class."""

from sqlalchemy import Column, String
from models.base_model import BaseModel


class Review(BaseModel):
    """Defines a Review."""

    __tablename__ = "reviews"

    place_id = Column(String(60), nullable=False, default="")
    user_id = Column(String(60), nullable=False, default="")
    text = Column(String(1024), nullable=False, default="")
