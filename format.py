import json
json_file = open('coronavirus', 'r+')
#data=json.load(json_file)
Lines = json_file.readlines()
print(len(Lines))
json_file.close()