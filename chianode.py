#!/usr/bin/env python
import psutil
import processutils
import threading
import logging
from flask import Flask
from flask import redirect
import matplotlib.pyplot as plt
import os, time
import subprocess, select
import sys
import re
# Initialization
log = logging.getLogger('chianode')
log.setLevel(logging.INFO)

app = Flask(__name__)


def get_free_space_at_path(path):
    df = subprocess.Popen(["df", path + "/."], stdout=subprocess.PIPE)
    output = df.communicate()
    #device, size, used, available, percent, mountpoint = \

    out = output[0]
    out = re.findall(b"\d{3,100}", out)[2]
    print(path," DF OUTPUT: ", out)
    #out = out.replace(b"  ",b" ")
    #out = out.split(b"\n")[1]
    #out = out.split(b" ")[3]
    out = out.decode("utf8")
    if out == '':
        out ='0'
    #out =str(out)
    return out


def find_good_lanes_on_machine():
    out = []
    for i in range(50):
        plot_path = '/'+'plot' + str(i)
        farm_path = '/'+'farm' + str(i
        if (os.path.isdir(plot_path)) & (os.path.isdir(farm_path)):
            plot = 0
            farm = 0
            good = 0
            print ("looking at lane ",i)
            free_plot_space = get_free_space_at_path(plot_path)
            free_farm_space = get_free_space_at_path(farm_path)
            if (int(free_farm_space) > 120000000):
                farm =1
            if (int(free_plot_space) >= 251980504):
                plot =1
            if plot & farm:
                good=1

            out += [(i,good,plot,farm)]

    return out


def get_plot_info_strings():

    by_id={}
    for pid in processutils.get_chia_pids():
        pid_data = processutils.get_chia_data(pid)
        if pid_data:
            if pid_data["id"] not in by_id.keys():
                by_id[pid_data["id"]] = {}

            if "lane" in pid_data.keys():
                by_id[pid_data["id"]]["lane"] = pid_data["lane"]

    """strings = {}
    for pid in processutils.get_chia_pids():
        pid_data = processutils.get_chia_data(pid)
        if pid_data:
            plot_id = pid_data["id"]
            plot_lane = pid_data["lane"]
            tminus = ((pid_data["start_time"] - time.time()) / (60 * 60))
            size = pid_data["cur_dir_size_1"] / (1024 * 1024 * 1024)
            outstr = "Lane: " + plot_lane + \
                     "Plot: " + plot_id + \
                     " size: " + str(size)[:6] + " GiB" + \
                     " T minus: " + str(tminus)[:6] + " hours" + \
                     " MiB/sec: " + str(size * 100 / -(tminus * 60))[:6]

            strings[plot_id] = outstr
            """
    return by_id


@app.route('/')
def index():
    commands = ""

    for data in get_plot_info_strings().items():
        commands += "Lane: "+data[1]["lane"] +" "+data[0] +" <br>"

    for data in find_good_lanes_on_machine():
        commands += "Lane "+str(data[0])
        commands += " exists "*data[1] or " not available"
        commands += "<br>"

    commands += """
    <div style="display:grid">
        <a href='restart'>restart</a>
        <a href='update'>update</a>
    </div>    
    """
    return commands


@app.route('/update')
def update():
    os.system("""    
    cd /home/chianode/ChiaNodeService &&
    mkdir backup
    cp * backup &&
    git fetch --all &&
    git reset --hard origin/master &&
    sudo chmod +777 * -R
    echo "activating venv" &&
    source venv/bin/activate &&
    echo "install requirements" &&
    pip3 install -r requirements.txt &&
    """)

    return ("updated")


@app.route('/restart')
def restart():
    threading.Timer(.5, lambda x: os.system("sudo systemctl restart chianode"))
    return redirect("/restarted", code=302)


@app.route('/restart')
def restarted():
    return redirect("/", code=302)


if __name__ == "__main__":
    print("hello from main")
    print(sys.argv)
    print(len(sys.argv))
    if len(sys.argv) > 1:
        app.run(host="0.0.0.0", port=80, debug=True)
    else:
        app.run(host="0.0.0.0", port=5000, debug=True)
