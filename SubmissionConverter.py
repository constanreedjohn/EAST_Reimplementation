# Author: Trần Tiến Hưng - https://github.com/constanreedjohn

import os
import pandas as pd
import numpy as np
import glob
import json

annot = 'D:/PaddleModel/predicts_east.txt'
outfile = 'D:/PaddleModel/submit_AI.txt'

data = []
x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []
x4 = []
y4 = []

# Open result file
with open(annot, 'r', encoding='utf8') as fin:
    co = []
    name = []
    for line in fin:
        path, cont = line.strip().split("\t")
        content = json.loads(cont)
        for index in content:
            co.append(index['points'])
            name.append(path)

# Get coor in dict['points']
for i, row in enumerate(co):
    # print("list {}: {}".format(i, row))
    for ind, col in enumerate(row):
        # print("co_pair {}: {}".format(ind, col))
        for coor in col:
            data.append(coor)

length = len(data) 

# Break down each coor into array
for x_1 in range(0,length,8):
    x1.append(data[x_1])
for y_1 in range(1,length,8):
    y1.append(data[y_1])

for x_2 in range(2,length,8):
    x2.append(data[x_2])
for y_2 in range(3,length,8):
    y2.append(data[y_2])

for x_3 in range(4,length,8):
    x3.append(data[x_3])
for y_3 in range(5,length,8):
    y3.append(data[y_3])

for x_4 in range(6,length,8):
    x4.append(data[x_4])
for y_4 in range(7,length,8):
    y4.append(data[y_4])

# Create submission file - Adjust name[i][<namefile>] for suitable file path.
with open(outfile, "a", encoding='utf8') as fout:
    for i in range(len(name)):
        fout.write(f"{name[i][-13:]},{x1[i]},{y1[i]},{x2[i]},{y2[i]},{x3[i]},{y3[i]},{x4[i]},{y4[i]}\n")

