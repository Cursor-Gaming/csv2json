import json, csv
from typing import TypeAlias
from os import PathLike

StrOrBytesPath: TypeAlias = str | bytes | PathLike[str] | PathLike[bytes]
FileDescriptorOrPath: TypeAlias = int | StrOrBytesPath

class csv2json:
    def __init__(self, csv_file: FileDescriptorOrPath, json_file: FileDescriptorOrPath):
        self.csv_file = csv_file
        self.json_file = json_file

    def convert(self):
        with open(self.csv_file, "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            json_data = []
            for row in csv_reader:
                json_data.append(row)
        with open(self.json_file, "w") as json_file:
            json.dump(json_data, json_file, indent = 4)