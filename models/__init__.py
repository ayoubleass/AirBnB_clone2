#!/usr/bin/python3

from models.engine import file_storage
from models.engine import db_storage
from  os import  getenv

storage = file_storage.FileStorage()

if getenv("HBNB_TYPE_STORAGE")== "db":
    storage = db_storage.DBStorage()


storage.reload()
