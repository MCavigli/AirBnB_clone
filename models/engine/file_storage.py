#!/usr/bin/python3
"""serializes instances to a JSON file and deserializes JSON file to instances"""
import json
from os import path

class FileStorage:
    """ """
    
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ """
        return self.__objects
    
    def new(self, obj):
        """ """
        self.__objects[obj.__class__.__name__ + '.' + str(obj.id)] = obj

    def save(self):
        """ """
        with open(self.__file_path, "w", encoding="utf-8") as written_file:
            json.dump(self.__object, written_file)

    def reload(self):
        """ """
        if path.exist(self.__file_path):
            with open(self.__file_path, mode='r') as read_file:
                return json.load(read_file)
