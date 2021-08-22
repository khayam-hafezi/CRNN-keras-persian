import glob
import os
from collections import Counter
from mapdict import letterMapNumberDict
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

dataset_path ="../../Modify_plate_dataset/"
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

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
    cnt = Counter()
    data = dict((k, []) for k in letterMapNumberDict.keys())
    dataset = dict((k, []) for k in plate_name_list)

    print(data)
    letter_plate_map = {}
    for words in plate_name_list:
          for letter in words:
              if letter in letterMapNumberDict.keys():
                data[letter].append(words)
                dataset[words] = letterMapNumberDict[letter]

    print(len(data['B']))
    print(dataset["11B23155"])
    return dataset


def show_dataset_feature():
    pass
    # Use a breakpoint in the code line below to debug your script.
    from collections import Counter


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    dataset = read_image_lis()
    x = np.array(list(dataset.keys()))
    y = np.array(list(map(int, dataset.values())))
    print(y)
    x_train, x_test_val, y_train, y_test_val = train_test_split(x, y, test_size = 0.2, random_state = 4, stratify=y)
    x_test, x_val, y_test, y_val = train_test_split(x_test_val, y_test_val, test_size = 0.5, random_state = 4, stratify=y_test_val)

    df_train = pd.DataFrame.from_dict({'data': x_train})
    df_train.to_excel('train_list.xlsx', header=False, index=False)

    df_test = pd.DataFrame.from_dict({'data1': x_test})
    df_test.to_excel('test_list.xlsx', header=False, index=False)

    df_val = pd.DataFrame.from_dict({'data2': x_val})
    df_val.to_excel('val_list.xlsx', header=False, index=False)

    print(len(y_test))
    
    show_dataset_feature()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
