
#!/usr/bin/python3
"""Defines the City class."""

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """Defines a City."""

    __tablename__ = "cities"

    name = Column(String(128), nullable=False)
    state_id = Column(
        String(60),
        ForeignKey("states.id"),
        nullable=False
    )

    state = relationship("State", back_populates="cities")