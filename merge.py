import os
import shutil

file_list = os.listdir('./deview')
file_list.sort()
with open('merge.ts', 'wb') as f:
    for fn in file_list:
        with open('./deview/' + fn, 'rb') as file:
            shutil.copyfileobj(file, f)