import json

with open('malaysia.json', 'r') as myfile:
    data=myfile.read()

obj = json.loads(data)

print("first: " + str(obj['item21']))
