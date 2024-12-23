"""
# CSV2JSON

A Python module made for converting CSV files to JSON.

visit [github.com/Cursor-Gaming/csv2json](https://github.com/Cursor-Gaming/csv2json) for more information
"""

import json
from typing import TypeAlias
from os import PathLike

StrOrBytesPath: TypeAlias = str | bytes | PathLike[str] | PathLike[bytes]
CSVObject: TypeAlias = str | list[str]
"""CSV Object that could be parsed by csv.DictReader()"""
JSONObject: TypeAlias = dict[object, object] | list[dict[object, object]] | list[object] | str
"""JSON Object or String that could be parsed by json.loads()"""
CSVFile: TypeAlias = StrOrBytesPath
"""CSV File that could be parsed by csv.DictReader()"""
JSONFile: TypeAlias = StrOrBytesPath
"""JSON File that could be parsed by json.load()"""

class csv2json_file:
    """
    A class for converting CSV files to JSON files.

    Args:
        csv_file (CSVFile): The CSV file to be read and converted.
        json_file (JSONFile): The JSON file to be created or overwritten.

    Attributes:
        csv_file (CSVFile): The CSV file to be read and converted.
        json_file (JSONFile): The JSON file to be created or overwritten.
    
    Methods:
        convert(*args, **kwargs): Converts the CSV file to JSON file.
        __repr__(): Returns a string representation of the object.
        __str__(): Returns a string representation of the object.
        __call__(): Converts the CSV file to JSON file.
    """
    def __init__(self, csv_file: CSVFile, json_file: JSONFile):
        self.csv_file = csv_file
        self.json_file = json_file

    def convert(self, *args, **kwargs) -> JSONFile:
        """Converts the CSV file to JSON file.
        
        Args:
            *args: Additional arguments to be passed to the json.dump() function.
            **kwargs: Additional keyword arguments to be passed to the json.dump() function.
        """
        csv = open(self.csv_file, "r").read()
        data: str = csv.removeprefix(csv.split("\n")[0])
        json_data: list[object] = []
        fieldnames: list[str] = csv.split("\n")[0].split(",")
        for row in data.split("\n"):
            parsed_row = row.split(",")
            json_data.append(dict(zip(fieldnames, parsed_row)))
        with open(self.json_file, "w") as json_file:
            json.dump(obj = json_data, fp = json_file, *args, **kwargs)

    def __repr__(self):
        return f"csv2json({self.csv_file}, {self.json_file})"

    def __str__(self):
        return f"csv2json({self.csv_file}, {self.json_file})"

    def __call__(self):
        return self.convert()

    def __enter__(self):
        return self

class csv2json:
    """
    A class for converting CSV objects to JSON objects. Useful for variables, not files.

    Args:
        csv (CSVObject): The CSV object to be converted.

    Attributes:
        csv (CSVObject): The CSV object to be converted.
    
    Methods:
        convert(*args, **kwargs): Converts the CSV object to JSON object.
        __repr__(): Returns a string representation of the object.
        __str__(): Returns a string representation of the object.
        __call__(): Converts the CSV object to JSON object.
    """
    def __init__(self, csv: CSVObject):
        self.csv = csv

    def convert(self, *args, **kwargs):
        """Converts the CSV object to JSON object.
        
        Args:
            *args: Additional arguments to be passed to the json.dump() function.
            **kwargs: Additional keyword arguments to be passed to the json.dump() function.
        """
        data: str = self.csv.removeprefix(self.csv.split("\n")[0])
        json_data: list[object] = []
        fieldnames: list[str] = self.csv.split("\n")[0].split(",")
        for row in data.split("\n"):
            parsed_row = row.split(",")
            json_data.append(dict(zip(fieldnames, parsed_row)))
        return json.dumps(json_data[1:], *args, **kwargs)

    def __repr__(self):
        return f"csv2json({self.csv})"

    def __str__(self):  
        return f"csv2json({self.csv})"

    def __call__(self):
        return self.convert()

    def __enter__(self):
        return self