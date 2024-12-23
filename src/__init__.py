import json, csv

class csv2json:
    def __init__(self, csv_file, json_file):
        self.csv_file = csv_file
        self.json_file = json_file

    def convert(self):
        with open(self.csv_file, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            json_data = []
            for row in csv_reader:
                json_data.append(row)
        with open(self.json_file, 'w') as json_file:
            json.dump(json_data, json_file, indent = 4)