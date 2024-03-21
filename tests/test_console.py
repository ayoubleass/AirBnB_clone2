#!/usr/bin/python3
"""
A unit test module for the console (command interpreter).
"""
import json
import MySQLdb
import os
import sqlalchemy
import unittest
from io import StringIO
from unittest.mock import patch

from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from tests import clear_stream


class TestHBNBCommand(unittest.TestCase):
    """
    """
    def test_all(self):
        """ test all method """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Houses")
            self.assertEqual(f.getvalue(), "\n** class doesn't exist **\n")

    def test_create(self):
        """ test create method """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Houses")
            self.assertEqual(f.getvalue(), "\n** class doesn't exist **\n")

    def test_update(self):
        """ test update method """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update Houses")
            self.assertEqual(f.getvalue(), "\n** class doesn't exist **\n")
    
    def test_destroy(self):
        """ test destroy method """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Houses")
            self.assertEqual(f.getvalue(), "\n** class doesn't exist **\n")

    def test_return_value(self):
        #conosle = HBNBCommand()
        #console.onecmd('create City name="Califronia"')
        pass

