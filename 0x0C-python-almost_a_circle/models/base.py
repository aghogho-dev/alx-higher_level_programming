#!/usr/bin/python3
"""The Base class module."""
import json


class Base:
    """Inside the base class.

    Attributes:
        __nb_objects (int): count instantiated obj.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base class instance.

        Args:
            id (int): id of class.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Inside to json string.

        Args:
            list_dictionaries (list): list dictionaries
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON serialization of obj to file.

        Args:
            list_objs (list): list of objs.
        """
        with open(cls.__name__ + ".json", mode="w") as f:
            if not list_objs:
                f.write("[]")
            else:
                list_dicts = [i.to_dictionary() for i in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Deserialize JSON string.

        Args:
            json_string (str): to deserialize.
        Returns:
            empty list or list repr.
        """
        if not json_string or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Instantiate a dictionary of atttrs.

        Args:
            dictionary (dict): dict of attrs.
        """
        if dictionary:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Load from file method.

        Returns:
             list of instances.
        """
        filename = f"{cls.__name__!s}.json"
        
        try:
            with open(filename) as f:
                list_dicts = Base.from_json_string(f.read())
                return [cls.create(**j) for j in list_dicts]
        except IOEerror:
            return []
