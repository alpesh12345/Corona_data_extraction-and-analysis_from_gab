import json
json_file = open('./r1/coronavirus.json', 'r')
data=json.load(json_file)
print(data[len(data)-1])
json_file.close()