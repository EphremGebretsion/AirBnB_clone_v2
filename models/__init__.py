#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == 'db':
    from models.engine.file_storage import FileStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.db_storage import DBStorage
    storage = FileStorage()
    storage.reload()
