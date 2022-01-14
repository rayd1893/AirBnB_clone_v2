#!/usr/bin/python3
'''Create file tgz that contents web statics'''
from fabric.api import local
from datetime import datetime


def do_pack():
    '''Function to run fabric'''
    now = datetime.now()
    year = str(now.year)
    month = str(now.month).zfill(2)
    day = str(now.day).zfill(2)
    hour = str(now.hour).zfill(2)
    minute = str(now.minute).zfill(2)
    second = str(now.second).zfill(2)
    folder = "web_static"
    tar = "versions/" + folder + "_" + year + month + day
    tar += hour + minute + second
    command = "tar -cvzf " + tar + ".tgz " + folder
    try:
        local("mkdir -p version")
        local(command)
        return tar
    except Exception as e:
        return None
