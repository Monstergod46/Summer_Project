import json
from pprint import pprint

action = 0

with open ('Color_Example.json') as data_file:
    data = json.load(data_file)


for item in data["colorsArray"]:
    print ("colorsArray[" + str(action) + "].colorName = " + item["colorName"])
    print ("colorsArray[" + str(action) + "].hexValue = " + item["hexValue"])
    print ()
    action += 1
