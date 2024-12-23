# CSV2JSON

A Python module made for converting CSV files to JSON.

## Installation and usage:

### Installation:

```bash
git clone https://github.com/Cursor-Gaming/csv2json.git
```

### Usage:

Converting files:

```python
from csv2json import csv2json_file

csv_file = "your/path/to.csv"
json_file = "your/path/to.json"

csv2json_file(csv_file, json_file).convert()
```

Converting variables:

```python
from csv2json import csv2json

csv = """id,first_name,last_name,email,gender,ip_address
1,Colan,Courteney,ccourteney0@examiner.com,Male,40.162.21.249
2,Bridie,Kipping,bkipping1@liveinternet.ru,Genderqueer,159.45.62.155
3,Petey,Tomblett,ptomblett2@mac.com,Non-binary,127.67.231.47
4,Dene,Bonsey,dbonsey3@nydailynews.com,Male,78.113.94.160
5,Hermann,Joisce,hjoisce4@g.co,Male,76.128.231.82"""

json = csv2json(csv).convert()
```

You can give the `.convert` method the arguments `json.dump()` or `json.dumps()` accesps.

Data sample used in the example is from [mockaroo.com](https://www.mockaroo.com/)