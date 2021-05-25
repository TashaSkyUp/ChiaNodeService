#!/bin/python3
import subprocess
import re


def get_disk_info():
    cmd = "sudo hwinfo --disk".split(" ")
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    result = proc.communicate()
    result = result[0].decode("utf8").splitlines()
    out = []
    for line in result:
        tmp = line.split(":")
        if len(line) > 2:
            if len(tmp) == 1:
                # print ("one",line)
                tmp = line.split(" at ")
                # print("two",tmp)
                line = tmp[0] + ":" + tmp[1]

            elif len(tmp) >= 3:
                # print (tmp)
                line = tmp[0] + ":" + " ".join(tmp[1:])
            else:
                pass
                # print(line)
                # print(tmp)

            out = out + [line]
    out_dict = {}
    for line in out:
        tmp = line.strip().split(":")
        try:
            num = int(tmp[0])
            out_dict[line] = {}
            cur_key = line
        except:
            out_dict[cur_key][tmp[0]] = tmp[1]

    # result = re.match('[0-9a-zA-Z:\- ]+',result )
    # result = re.match('[]', result)

    # print('\n'.join(result))
    # print ('\n'.join(out))
    for data in out_dict.items():
        #print("----->", data[0], "<-----")
        for data2 in data[1].items():
            pass
            #print(data2[0], data2[1])

    out_dict2 = {}
    for data in out_dict.items():
        key = out_dict[data[0]]["Device File"]
        print(key)

        out_dict2[key] = {}
        data_in = out_dict[data[0]]
        print('\n'.join(data_in))

        fields = ["Model",
                  "Vendor",
                  "Device",
                  "Capacity"]
        for field in fields:
            if field in data_in.keys():
                out_dict2[key][field]=data_in[field]

    return out_dict2
disk_info=get_disk_info()
for disk in disk_info:
    print(disk)
    for field in disk_info[disk].keys():
        try:
            print(disk_info[disk][field])
        except:
            pass
    print("")