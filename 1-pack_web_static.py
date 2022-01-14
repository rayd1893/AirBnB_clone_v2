#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the
contents of the web_static folder of your AirBnB Clone
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    must return the archive path if the archive has been correctly
    generated. Otherwise, it should return None
    """
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
