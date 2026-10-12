#!/usr/bin/python3
"""Defines the DBStorage class."""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base


Base = declarative_base()


class DBStorage:
    """Interacts with the MySQL database through SQLAlchemy."""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize the database engine and session."""
        user = os.getenv("HBNB_MYSQL_USER", "hbnb_test")
        password = os.getenv("HBNB_MYSQL_PWD", "hbnb_test_pwd")
        host = os.getenv("HBNB_MYSQL_HOST", "localhost")
        database = os.getenv("HBNB_MYSQL_DB", "hbnb_test_db")

        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                user, password, host, database
            ),
            pool_pre_ping=True
        )

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects, optionally filtering by class."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }

        result = {}
        targets = [cls] if cls else list(classes.values())

        for model in targets:
            if isinstance(model, str):
                model = classes.get(model)

            if model is None:
                continue

            for obj in self.__session.query(model).all():
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                result[key] = obj

        return result

    def new(self, obj):
        """Add an object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit changes to the database."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the current database session."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create tables and initialize the database session."""
        from models.state import State
        from models.city import City
        from models.user import User
        from models.place import Place
        from models.review import Review
        from models.amenity import Amenity

        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False
        )
        self.__session = scoped_session(session_factory)
