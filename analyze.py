
import glob
import os
from collections import Counter
from mapdict import letterMapNumberDict
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
dataset_path ="./dataset/test/"

def read_image_lis():
    plate_path_list = glob.glob(dataset_path + "*")
    plate_name_list = []
    for plate_path in plate_path_list:
        plate_name_list.append(os.path.splitext(os.path.basename(plate_path))[0])
    dataset_letters = ''.join(plate_name_list)
    res = Counter(dataset_letters)

    print(len(plate_name_list), len(res.keys()), res.keys())
    print(res)
    print("data number:", sum(res.values()))

read_image_lis()