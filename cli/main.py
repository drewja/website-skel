#!/usr/bin/python3

import sys
import os
from _parsearg import parse

DEFAUT_NAME = 'my-website'
SKEL = os.path.join(os.path.expanduser('~'), '.local/lib/website-skel/skel')

def confirm(msg):
    resp = input(msg)
    if resp.lower() in ['n', '0', 'no']:
        return False
    return True

if __name__ == "__main__":

    root = os.getcwd()

    name = input("Project Name ? (%s) " %DEFAUT_NAME)
    if not name: name = DEFAUT_NAME
    dest = input("Where would like to put your new project? directory must exist (%s): " %root)
    try:
        if not os.path.isabs(dest):
            dest = os.path.join(root, dest)
        dest = os.path.abspath(dest)
        if not os.path.isdir(dest):
            print(" -- -- Destination directory does not exist (%s) -- --" %dest)
            print("run : 'mkdir -p %s' to create and try again" %dest)
            exit(1)
    except Exception as e:
        print(e)
    

    dest = os.path.join(dest, name)
    empty = False
    exists = False
    if os.path.exists(dest):
        exists = True
        if not os.path.isdir(dest):
            print('invalid path')
            exit(1)
        if not os.listdir(dest):
            empty = True
            print("--------    Project directory exists and is empty     -----------")
        else:
            if not confirm("-------- Project directory already exists and in not empty! ARE YOU SURE? -------- (y) or n : "):
                print("Make new project cancelled")
                exit(0)

    if not confirm("Confirm: %s (y) or n : " %dest):
        print('Make new project canceled')
        exit(0)
    

    import shutil
    try:
        print('copying files from {} to {}'.format(SKEL, dest))
        r = shutil.copytree(SKEL, dest, symlinks=False, ignore=None, copy_function=shutil.copy2, ignore_dangling_symlinks=False, 
            dirs_exist_ok=False)
        print("----------DONE-----------------")
        print("cd to {} and run 'npm install -i'".format(dest))
    except Exception as e:
        print(e)
    print(r)

        
