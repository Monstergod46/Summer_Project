import json
from pprint import pprint

with open('citylots.json') as data_file:
    data = json.load(data_file)

for item in data["data"]:
    i = 0
    print(list(data.keys())[0])
