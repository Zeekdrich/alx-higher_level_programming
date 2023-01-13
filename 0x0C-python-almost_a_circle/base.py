#!/usr/bin/python3
"""base
"""

import json
import csv


class Base:
    """Base of the selected shapes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Json string representation
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)


    @staticmetod
    def from_json_string(json_string):
        """Json strings to list
        """
        if type(json_string) != str or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return all existing instances with attributes
        """
        if cls.__name__ = "Rectangle":
            temp = cls(1, 1)
        if cls.__name__ = "Square":
            temp = cls(1)

        temp.update(**dictionary)
        return temp

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes to JSON string
        """
        with open(cls.__name__ + ".json", mode="w") as write_file:
            if list_objs is None:
                write_file.write("[]")
            else:
                write_file.write(cls.to_json_string( [item.to_dictionary() for item in list_objs]))

    @classmethod
    def load_from_file(cls):
        """Returns list of instances
        """

        res = []
        with open(cls.__name__ + ".json", mode="r") as read_file:
            text = read_file.read()
        text = cls.from_json_string(text)
        for item in text:
            if type(item) == dict:
                res.append(cls.create(**item))
            else:
                res.append(item)
        return res

    @classmethod
    def save_to_csv_file(cls, list_objs):
        """Save to csv
        """

        res = [item.to_dictionary() for item in list_objs]
        with open(cls.__name__ + ".csv", mode="w") as save_file:
            write_to = csv.DictWriter(save_file, res[0].keys())
            write_to.writeheader()
            write_to.writerows(res)

    @classmethod
    def load_from_file_csv(cls):
        """Loads from csv file
        """

        res = []
        res_dict = {}
        with open(cls.__name__ + ".csv", mode="r") as read_file:
            read_from = csv.DictReader(read_file)
            for item in read_from:
                for x, i in dict(item).items():
                    res_dict[x] = int(i)
                res.append(cls.create(**res_dict))
        return res
