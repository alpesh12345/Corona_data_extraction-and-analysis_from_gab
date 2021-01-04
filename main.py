import json
import os
import subprocess
tag='coronavirus'
num=35127
try:
    output=subprocess.check_output(['garc','search', tag ])
    #print(1)
    #print(type(output))
    output2=output.decode('utf-8')
    data = (output2.replace("}\n{", "}786945\n{"))
    total=data.split("786945")
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
filename = "./result/"+tag+".json"
os.makedirs(os.path.dirname(filename), exist_ok=True)
json_file = open(filename, 'w')
json.dump(total2, json_file, indent=1)
json_file.close()

print("Finished and total gabs:"+ str(num))