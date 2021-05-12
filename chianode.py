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
    commands="""
    <a href='restart'>restart</a>
    <a href='update'>update</a>    
    """
    return(commands)


@app.route('/update')
def update():
    os.system("cd /home/chianode/ChiaNodeService && git pull")
    return ("hopeing it works")

@app.route('/restart')
def restart():
    os.system("sudo systemctl restart chianode")
    #os.system("sudo touch /home/chianode/ChiaNodeService/here.touch")
    #os.system("sudo chmod +777 /home/chianode/ChiaNodeService/here.touch")
    return("testing..")

# If this program was called directly (as opposed to imported)
if __name__ == "__main__":
    print("hello from main")
    app.run()


