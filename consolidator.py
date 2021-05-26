#!/bin/python3
import subprocess
import os
import numpy as np
import sys
import shutil
from file_utils import progress_file_move


def get_free_space_at_dir(path):
    df = subprocess.Popen(["df", "-BG", path], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    output = df.communicate()[0]
    output = output.decode("utf8")
    #print(output)
    try:
        output = output.splitlines()
        output = [o for o in output[1].split(" ") if len(o) >= 1]

        device, size, used, available, percent, mountpoint = \
            output

        # print(device, size, used, available, percent, mountpoint)
    except:
        return -1
    return int(available[:-1])


def get_farm_info():
    farm_dirs = ["/farm" + str(i) for i in range(50)]
    farms_dic = {path: get_free_space_at_dir(path) for path in farm_dirs if get_free_space_at_dir(path) != -1}
    return farms_dic


def find_fullist_farm(info: dict):
    #print(info)
    l = [int(i) for i in info.values()]
    arr = np.array(l)
    return list(info.items())[arr.argmin()][0]

def find_oldist_file_in_dir(path):
    print(path)
    list_of_files = os.listdir(path)
    print(list_of_files)
    full_path = [path+"/"+str(x) for x in list_of_files if x[-4:] == "plot"]
    print(full_path)
    oldest_file = min(full_path, key=os.path.getmtime)
    return oldest_file



dest_dir=sys.argv[1]

try:
    auto= sys.argv[2]
except:
    auto="no"
go=1
while go:
    if auto != "yes":
        go=0

    farm_info = get_farm_info()
    dest_free =farm_info[dest_dir]
    print("dest has ",dest_free," avail")

    if dest_free<102:
        print("dest full")
        exit

    #remove destination as possible soruce
    try:
        farm_info.pop(dest_dir)
    except:
        pass

    fullist_farm = find_fullist_farm(farm_info)
    file_to_move_source = find_oldist_file_in_dir(fullist_farm)

    file_to_move_dest = file_to_move_source.split("/")[-1]
    file_to_move_dest = dest_dir+'/'+file_to_move_dest

    print ("fullist farm is ", fullist_farm, " moving ",file_to_move_source, " to ",file_to_move_dest, " ok?")

    if auto != "yes":
        yesno= input()
    else:
        yesno="y"

    if "y" in yesno:
        print(file_to_move_source+'.moving',file_to_move_dest+'.moving')

        print("rename")
        os.rename(file_to_move_source, file_to_move_source+".moving")

        print("move")
        progress_file_move(file_to_move_source+".moving", file_to_move_dest+'.moving')

        print("rename")
        os.rename(file_to_move_dest+".moving", file_to_move_dest)
