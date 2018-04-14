import json
from pprint import pprint

count = 0
actionCount = 0

with open('Facebook_Example.json') as data_file:    
    data = json.load(data_file)

for item in data["data"]:
    print ("data[" + str(count) + "].id = " + item["id"])
    print ("data[" + str(count) + "].from.name = " + item["from"]["name"])
    print ("data[" + str(count) + "].from.id = " + item["from"]["id"])
    print ("data[" + str(count) + "].message = " + item["message"])
    print ("data[" + str(count) + "].actions[" + str(actionCount) + "].name = " + item["actions"][0]["name"])
    print ("data[" + str(count) + "].actions[" + str(actionCount) + "].link = " + item["actions"][0]["link"])
    actionCount += 1
    print ("data[" + str(count) + "].actions[" + str(actionCount) + "].name = " + item["actions"][1]["name"])
    print ("data[" + str(count) + "].actions[" + str(actionCount) + "].link = " + item["actions"][1]["link"])
    print ("data[" + str(count) + "].type = " + item["type"])
    print ("data[" + str(count) + "].created_time = " + item["created_time"])
    print ("data[" + str(count) + "].updated_time = " + item["updated_time"])
    print ()
    count += 1
    actionCount = 0
