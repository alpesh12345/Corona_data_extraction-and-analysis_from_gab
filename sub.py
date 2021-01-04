import subprocess
import csv
import json
import os

tsv_file = open("./covid_keywords_lazer_lab.tsv")
read_tsv = csv.reader(tsv_file, delimiter="\t")
num=0      #
for row in read_tsv:
    tag=row[0].replace(" ","_").replace("-","_")
    print(tag)
    #tag2='corona'
    try:
        output=subprocess.check_output(['garc','search', tag ])
        #print(1)
        #print(type(output))
        output2=output.decode('utf-8')
        data = (output2.replace("}\n{", "}78694545454552\n{"))
        total=data.split("78694545454552")
        total2=[]
        i = 0
        for a in total:
            #print(i)
            try:
                total2.append(json.loads(a))
                i = i + 1
            except:
                print("error " + str(i))
        num=num + i
        print(str(i)+" number of gabs for "+tag + " total gabs till now :"+str(num))
    except:
        total2=[]
    filename = "./r3/"+tag+".json"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    json_file = open(filename, 'w')
    json.dump(total2, json_file, indent=1)
    json_file.close()

print("Finished and total gabs:"+ str(num))