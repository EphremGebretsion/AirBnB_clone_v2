#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import getenv
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


storage_type = getenv("HBNB_TYPE_STORAGE")
__all__ = ['Amenity', 'City', 'Place', 'Review', 'State', 'User']
if storage_type == 'db':
    from models.engine.file_storage import FileStorage
    storage = DBStorage()
    storage.reload()
    __all__.append('storage')
else:
    from models.engine.db_storage import DBStorage
    storage = FileStorage()
    storage.reload()
    __all__.append('storage')
