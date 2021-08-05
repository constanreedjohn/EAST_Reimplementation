# Author: Trần Tiến Hưng - https://github.com/constanreedjohn/constanreedjohn

import glob
import os
import numpy as np
from tqdm import tqdm
import pandas as pd
import json

# Label folder path
root_path = 'D:/PaddleModel/Data/validation/fix_val/*'
files = glob.glob(root_path)
outfile = 'D:/PaddleModel/Data/validation/val_annotation.txt'

# Read each file
for file in files:
    print(file)

# If file is empty - skip
    if (os.stat(file).st_size == 0):
        print('{} skipped'.format(file))
        continue

# Create dataframe from label
    with open(file, "r", encoding='utf8') as fin:
        data = pd.read_csv(fin, delimiter=",", header=None, engine='c')
        data.columns = ["x1", 'y1', 'x2', 'y2', 'x3', 'y3', 'x4', 'y4', 'NAME']          

    length = len(data)
    content = []

# Create annotation format
    for i in range(length):
        con = {"transcription": str(data['NAME'][i])}
        con['points'] = list([list([int(data['x1'][i]),int(data['y1'][i])]), list([int(data['x2'][i]),int(data['y2'][i])]), list([int(data['x3'][i]),int(data['y3'][i])]), list([int(data['x4'][i]),int(data['y4'][i])])])
        content.append(con)
        json_string = json.dumps(content, ensure_ascii=False)

# Print outfile - Adjust suitable path in line 41
    with open(outfile, "a", encoding='utf8') as fout:
        fout.write(f'\ntest_img/train_{file[-8:-4]}.jpg\t{json_string}')