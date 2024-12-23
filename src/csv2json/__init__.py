"""
# CSV2JSON

A Python module made for converting CSV files to JSON.
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
    def __init__(self, csv_file: CSVFile, json_file: JSONFile):
        self.csv_file = csv_file
        self.json_file = json_file

    def convert(self, *args, **kwargs) -> JSONFile:
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
    def __init__(self, csv: CSVObject):
        self.csv = csv

    def convert(self, *args, **kwargs):
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