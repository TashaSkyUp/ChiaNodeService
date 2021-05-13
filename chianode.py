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

# Initialization
log = logging.getLogger('chianode')
log.setLevel(logging.INFO)

app = Flask(__name__)


def get_plot_info_strings():
    for pid in processutils.get_chia_pids():
        pid_data = processutils.get_chia_data(pid)
        strings = []

        strings += ["plot: " + pid_data["id"] + " " +
                    +"size: " + pid_data["cur_dir_size_1"] + " "
                    ]
    return strings


@app.route('/')
def index():
    commands = ""

    for plot in get_plot_info_strings():
        commands += plot

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
    app.run(host="0.0.0.0", port=80)
