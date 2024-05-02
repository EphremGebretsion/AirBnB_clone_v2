#!/usr/bin/python3
"""
New engine for database storage
"""
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
class DBStorage():
    """
    class used to manage and use database as a storage
    """
    __engine = None
    __session = None
    def __init__(self):
        """initializing the class DBStorage"""
        dialect = 'mysql'
        driver = 'mysqldb'
        user = getenv("HBNB_MYSQL_USER", default="hbnb_dev")
        pswd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST", default="localhost")
        db = getenv("HBNB_MYSQL_DB", default="hbnb_dev_db")
        hbnb_env = getenv("HBNB_ENV")
        dbURL = f"{dialect}+{driver}://{user}:{pswd}@{host}/{db}"
        self.__engine = create_engine(dbURL, pool_pre_ping=True)
        if hbnb_env == "test":
            Base.metadata.drop_all(self.__engine)


    def all(self, cls=None):
        """
        gets all the objects of the cls from the table
        if not adds all the objects from the table
        in dictionary
        """
        all_cls = (User, State, City, Amenity, Place, Review)
        res = {}
        if not cls:
            for icls in all_cls:
                all_obj = self.__session.query(icls).all()
                for obj in all_obj:
                    key = obj.to_dict()['__class__'] + '.' + obj.id
                    res[key] = obj
            return res
        all_obj = self.__session.query(cls).all()
        for obj in all_obj:
            key = obj.to_dict()['__class__'] + '.' + obj.id
            res[key] = obj
        return res

    def new(self, obj):
        """adds obj to the session"""
        self.__session.add(obj)

    def save(self):
        """commits all the changes made"""
        self.__session.commit()

    def delete(self, obj=None):
        """delets obj from database"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """creates all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
