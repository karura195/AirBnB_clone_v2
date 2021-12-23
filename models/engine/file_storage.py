#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


classes = {"BaseModel": BaseModel, "User": User, "State": State,
           "Place": Place, "City": City, "Amenity": Amenity, "Review": Review}


class FileStorage:
        """This class manages storage of hbnb models in JSON format"""
        __file_path = 'file.json'
        __objects = {}

        def all(self, cls=None):
                """Devuelve un diccionario de modelos actualmente
                almacenados"""
                if cls is None:
                        return FileStorage.__objects
                else:
                        dic_classes = {}
                        for key in self.__objects:
                                # State.id
                                class_id = key.split(".")
                                if class_id[0] == cls.__name__:
                                        dic_classes[key] = self.__objects[key]
                return dic_classes

        def new(self, obj):
                """Adds new object to storage dictionary"""
                self.all().update({obj.to_dict()['__class__'] + '.' +
                                   obj.id: obj})

        def save(self):
                """Saves storage dictionary to file"""
                with open(FileStorage.__file_path, 'w') as f:
                        temp = {}
                        temp.update(FileStorage.__objects)
                        for key, val in temp.items():
                                temp[key] = val.to_dict()
                                json.dump(temp, f)

        def delete(self, obj=None):
                """Para eliminar obj de __objects si está dentro"""
                if not obj:
                        return
                key = "{}.{}".format(type(obj).__name__, obj.id)
                del FileStorage.__objects[key]

        def reload(self):
                """Loads storage dictionary from file"""
                try:
                        temp = {}
                        with open(FileStorage.__file_path, 'r') as f:
                                temp = json.load(f)
                                for key, val in temp.items():
                                        self.all()[key] =
                                        classes[val['__class__']](**val)
                except FileNotFoundError:
                        pass
