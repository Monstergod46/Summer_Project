import json
from pprint import pprint

with open('citylots.json') as data_file:
    data = json.load(data_file)
print(data)
