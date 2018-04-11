#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import shutil
import sys

from notes.model import db
from notes import config


INSTALL_PATH = "/var/www/notes/"


def usage():
    print("Usage: python setup.py [install | uninstall | initdb]")
    return


def install():
    """ copy notes directory into python standard library path. """
    try:
        if not os.path.exists(INSTALL_PATH):
            os.mkdir(INSTALL_PATH)
    except IOError as e:
        print("Install failed: ",  e)
        return

    for obj in os.listdir('.'):
        try:
            if obj == ".git":
                pass
            elif os.path.isfile(obj):
                shutil.copy2(obj, INSTALL_PATH)
            elif os.path.isdir(obj):
                shutil.copytree(obj, INSTALL_PATH + obj)
        except OSError as e:
            # ignore file exists error
            if e[0] != 17:
                print("Install failed: ", e)
            else:
                print(e)


def uninstall():
    pass


def initdb():
    """ Create database and related tables. """
    try:
        if not os.path.exists(config.DB_LOCATION):
            os.mkdir(config.DB_LOCATION)

        print("Create tables for notes")
        db.create_tables(config.DATABASE)

        if not os.path.exists(config.UPLOAD_DIR):
            print("Create upload directory")
            os.mkdir(config.DB_LOCATION)
    except Exception as e:
        print(e) 


def main():
    if len(sys.argv) != 2:
        usage()
        return

    menu = {
        "install": install, 
        "initdb": initdb,
        "uninstall": uninstall
    }

    function = menu.get(sys.argv[1])
    if function:
        function()
    return


if __name__ == '__main__':
    main()
   
