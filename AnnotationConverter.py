# Author: Trần Tiến Hưng - https://github.com/constanreedjohn/constanreedjohn

import glob
import os
import numpy as np
from tqdm import tqdm
import pandas as pd
import json

root_path = 'D:/PaddleModel/Data/train/labels/*'
files = glob.glob(root_path)
outfile = 'D:/PaddleModel/Data/test/train_annotation.txt'

for file in files:
    print(file)

    if (os.stat(file).st_size == 0):
        print('{} skipped'.format(file))
        continue

    with open(file, "r", encoding='utf8') as fin:
        data = pd.read_csv(fin, delimiter=",", header=None, engine='c')
        data.columns = ["x1", 'y1', 'x2', 'y2', 'x3', 'y3', 'x4', 'y4', 'NAME']          

    length = len(data)
    # co_1 = []
    # co_2 = []
    # co_3 = []
    # co_4 = []

    # for i in range(length):
    #     co_1.append([data['x1'][i],data['y1'][i]])
    #     co_2.append([data['x2'][i],data['y2'][i]])
    #     co_3.append([data['x3'][i],data['y3'][i]])
    #     co_4.append([data['x4'][i],data['y4'][i]])

    content = []

    for i in range(length):
        con = {"transcription": str(data['NAME'][i])}
        con['points'] = list([list([int(data['x1'][i]),int(data['y1'][i])]), list([int(data['x2'][i]),int(data['y2'][i])]), list([int(data['x3'][i]),int(data['y3'][i])]), list([int(data['x4'][i]),int(data['y4'][i])])])
        content.append(con)
        json_string = json.dumps(content, ensure_ascii=False)

    with open(outfile, "a", encoding='utf8') as fout:
        fout.write(f'\ntrain_img/train_{file[-8:-4]}.jpg\t{json_string}')