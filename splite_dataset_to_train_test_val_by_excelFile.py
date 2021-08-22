import os
import pandas as pd
import shutil

dataset_path ="E:/Esmaill/Project/deepLearning/Zahraprj/plate/Modify_plate_dataset/"
paths= ["dataset/train", "dataset/test", "dataset/validation"]
for path in paths:
    if not os.path.isdir(path):
        os.makedirs(path)



def copy_files(path_excel, dest_path):
    df = pd.read_excel(path_excel, header=None)
    files = list(df[0])

    for file in files:
        name = os.path.join(dataset_path, file+".jpg")
        if os.path.isfile(name):
            shutil.copy(name, dest_path)
        else:
            print('file does not exist', name)


train_file_path = 'train_list.xlsx'
test_file_path  = 'test_list.xlsx'
val_file_path   = 'val_list.xlsx'


copy_files(train_file_path, paths[0])
copy_files(test_file_path, paths[1])
copy_files(val_file_path, paths[2])

