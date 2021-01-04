import os
import csv
import json
import subprocess

import garc

tsv_file = open("./covid_keywords_lazer_lab.tsv")
read_tsv = csv.reader(tsv_file, delimiter="\t")
tag='coronavirus'
#for row in read_tsv:
#    print(row[0])
row='garc search coronavirus' #--number_gabs=1230'
total=[]
print(row)
stream = os.popen(row)
#print(stream)
#print(1)
output = stream.read()
print(type(output))
print(len(output))
output2=output
data = (output2.replace("}\n{", "}7869\n{"))
total=data.split("7869")
total2=[]
print("safe")
i=0
for a in total:
    print(i)
    try:
        total2.append(json.loads(a))
        i = i + 1
    except:
        print("error "+ str(i))
#total.append(output2)
print(2)
#print(len(total2))
filename = "./result/"+tag+".json"
os.makedirs(os.path.dirname(filename), exist_ok=True)
json_file = open(filename, 'w')
json.dump(total2, json_file, indent=1)
json_file.close()
print("finish")