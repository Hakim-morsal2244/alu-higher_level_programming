#!/usr/bin/python3
import csv
import os

class Base:
    """Base class with CSV serialization/deserialization."""
    # Existing methods...

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serialize a list of objects to a CSV file.
        The filename is <Class name>.csv.
        """
        filename = f"{cls.__name__}.csv"
        with open(filename, mode="w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserialize objects from a CSV file.
        The filename is <Class name>.csv.
        """
        filename = f"{cls.__name__}.csv"
        if not os.path.exists(filename):
            return []

        with open(filename, mode="r", newline="") as csvfile:
            reader = csv.reader(csvfile)
            obj_list = []
            for row in reader:
                if cls.__name__ == "Rectangle":
                    obj = cls(int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[0]))
                elif cls.__name__ == "Square":
                    obj = cls(int(row[1]), int(row[2]), int(row[3]), int(row[0]))
                obj_list.append(obj)
            return obj_list
