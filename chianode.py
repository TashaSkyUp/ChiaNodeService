#!/usr/bin/env python

import logging
from flask import Flask
import matplotlib.pyplot as plt
import os, time
import subprocess, select

# Initialization
log = logging.getLogger('chianode')
log.setLevel(logging.INFO)


app = Flask(__name__)

@app.route('/')
def index():
    commands="""<div>
    <a href='restart'>restart</a>
    <a href='update'>update</a>
    </div>    
    """
    return(commands)


@app.route('/update')
def update():
    os.system("""cd /home/chianode/ChiaNodeService &&
    git fetch --all &&
    git reset --hard origin/master &&
    sudo chmod +777 * -R
    """)

    return ("updating...")

@app.route('/restart')
def restart():
    os.system("sudo systemctl restart chianode")
    return("restarting..")

# If this program was called directly (as opposed to imported)
if __name__ == "__main__":
    print("hello from main")
    app.run(host="0.0.0.0", port=80)

