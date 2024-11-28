#!/usr/bin/python3
""" Class Base """
import json
import csv
import os.path


class Base:
    """ Starting point for all classes """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Convert dictionary to JSON string """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save a list of objects to a JSON file """
        filename = "{}.json".format(cls.__name__)
        list_dic = []

        if list_objs:
            for obj in list_objs:
                list_dic.append(obj.to_dictionary())

        lists = cls.to_json_string(list_dic)

        with open(filename, 'w') as f:
            f.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """ Convert JSON string to dictionary """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Create an instance from a dictionary """
        if cls.__name__ == "Rectangle":
            new = cls(10, 10)
        else:
            new = cls(10)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """ Load a list of instances from a JSON file """
        filename = "{}.json".format(cls.__name__)

        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as f:
            list_str = f.read()

        list_cls = cls.from_json_string(list_str)
        list_ins = []

        for index in range(len(list_cls)):
            list_ins.append(cls.create(**list_cls[index]))

        return list_ins

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Save a list of objects to a CSV file """
        filename = "{}.csv".format(cls.__name__)

        # Set the keys for the CSV header based on the class type
        if cls.__name__ == "Rectangle":
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:  # Square class
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        # If the list of objects is not empty, extract the data and write to CSV
        if list_objs:
            for obj in list_objs:
                row = [obj.to_dictionary()[key] for key in list_keys]
                matrix.append(row)

        # Write to the CSV file
        with open(filename, 'w', newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(matrix)

    @classmethod
    def load_from_file_csv(cls):
        """ Load a list of instances from a CSV file """
        filename = "{}.csv".format(cls.__name__)

        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as readFile:
            reader = csv.reader(readFile)
            csv_list = list(reader)

        # Set the keys for the CSV columns based on the class type
        if cls.__name__ == "Rectangle":
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:  # Square class
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        # Convert the CSV data into a dictionary with the correct keys
        for csv_elem in csv_list:
            dict_csv = {list_keys[i]: int(csv_elem[i]) for i in range(len(list_keys))}
            matrix.append(dict_csv)

        # Create instances from the dictionary data
        list_ins = []
        for data in matrix:
            list_ins.append(cls.create(**data))

        return list_ins
