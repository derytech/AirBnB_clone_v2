
#!/usr/bin/python3
"""Defines the State class."""

import os

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """Defines a State."""

    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship(
            "City",
            back_populates="state",
            cascade="all, delete-orphan"
        )
    else:
        @property
        def cities(self):
            """Return the cities belonging to this state."""
            from models import storage
            from models.city import City

            return [
                city for city in storage.all(City).values()
                if city.state_id == self.id
            ]