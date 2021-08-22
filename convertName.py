# encoding: utf-8
import glob
import os
from shutil import copyfile
from mapdict import FarsiMapenDict

def plate_name_modify(plate_name, dict_map):
    plate_name_modify = plate_name[6:8] + dict_map[plate_name[5]] + plate_name[:5]
    return plate_name_modify

mypath = "./Plate_farsi/"
destPath ="./Plate_en/"
plate_list = glob.glob(mypath + "*")
print(len(plate_list))
for plate_path in plate_list:
    plate_name = os.path.basename(plate_path)
    plate_name = plate_name_modify(plate_name, FarsiMapenDict)
    print(plate_name)
    src = os.path.abspath(plate_path)
    dst = os.path.abspath(destPath) + "/" + plate_name + ".jpg"
    print(src, dst)
    copyfile(src, dst)