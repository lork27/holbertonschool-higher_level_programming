#!/usr/bin/python3
'''module that contains Base Class'''
import json


class Base:
    '''base class for all other classes in this project'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''initializes object'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns json representation of list of dictionaries'''
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        '''returns list of the JSON string'''
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        '''saves JSON representation of an object to a text file'''
        if list_objs is None:
            with open(cls.__name__ + ".json", 'w', encoding="utf-8") as file:
                file.write("[]")
        else:
            list_of_dict = []
            for obj in list_objs:
                list_of_dict.append(obj.to_dictionary())
            with open(cls.__name__ + ".json", 'w', encoding="utf-8") as file:
                file.write(Base.to_json_string(list_of_dict))
