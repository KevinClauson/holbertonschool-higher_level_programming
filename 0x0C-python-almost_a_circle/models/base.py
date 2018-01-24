#!/usr/bin/python3
import json
"""
module with class Base
"""


class Base:
    """
    classf or all objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        instantiate base
        """    
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        takes a dict and puts into a json string
        """
        if list_dictionaries == None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        if list_objs == None:
            new_list = []
        else:
            new_list = list(item.to_dictionary() for item in list_objs)
        
        file_name = cls.__name__ + ".json"

        with open("{}".format(file_name), "w") as new_file:
            new_file.write(Base.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if json_string == None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            r = cls(2, 3)
        elif cls.__name__ == "Square":
            r = cls(4)
        r.update(**dictionary)
        return (r)

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name) as fd:
                js = Base.from_json_string(fd.read())
        except FileNotFoundError:
            return []
        return list(map(lambda g: cls.create(**g), js))
