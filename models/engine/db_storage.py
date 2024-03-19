#!/usr/bin/python3
"""
This module define the DBStorage
"""

from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

class DBStorage:

    __engine=None
    __session=None

    def __init__(self):
        """Initializes the DBStorage class."""
        username = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        db_name = getenv("HBNB_MYSQL_DB")
        db_host = getenv("HBNB_MYSQL_HOST")
        url = f"mysql+mysqldb://{username}:{password}@{db_host}/{db_name}"
        print(url)
        self.__engine = create_engine(f"mysql+mysqldb://{username}:{password}@{db_host}/{db_name}",
                                     pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
        Returns a dictionary of objects from the database.
        """
        from models.base_model import Base
        from sqlalchemy.orm import sessionmaker
        from models.state import State
        from models.city import City
        from models.user import User
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review
        models = [User, City, Place, Amenity, Review, State]
        result = {}
        if cls is None:
            for model in models:
                query = self.__session.query(model)
                for obj in query.all():
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    result[key] = obj    
        else: 
            query = self.__session.query(cls)
            for obj in query.all():
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                result[key] = obj
        return result
        
    def save(self):
        """
        Commits changes to the database.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes an object from the database.
        """
        if obj is not None:
            self.__session.delete(obj)
    
    def new(self, obj):
        """
        Adds a new object to the session.
        """
        if obj is not None:
            self.__session.add(obj)

    
    def reload(self):
        """
        Creates all tables and initializes a new session.
        """
        Base.metadata.create_all(bind=self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)()

