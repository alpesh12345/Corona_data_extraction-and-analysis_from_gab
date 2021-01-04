import os
import csv
import json
import subprocess
import garc

tsv_file = open("./covid_keywords_lazer_lab.tsv")
read_tsv = csv.reader(tsv_file, delimiter="\t")
i=0
for row in read_tsv:
    tag=row[0].replace(" ","_").replace("-","_")
    print(tag + " " + str(i))
    i=i+1
print(str(i))
#coronavirus	chen_lerman_ferrara | green_et_al | twitter_2020-05-13
#covid19	chen_lergman_ferrara | green_et_al | twitter_2020-05-13