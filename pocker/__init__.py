#!/usr/bin/python3

# "THE BARBECUE-WARE LICENSE" (Revision 1):
#
# <benatto@gmail.com> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can make me a brazilian barbecue, including beers
# and caipirinha in return to Paulo Leonardo Benatto.
#
# The quality of the barbecue depends on the amount of beer that has been
# purchased.


import os
import sys
import time
import uuid

import lxc


__all__ = ['pocker_create']


POCKER_CONTAINER_PATH = os.environ.get('POCKER_CONTAINER_PATH', '/var/lib/lxc')


def superuser(f):
    """Decorator to test whether the user is root."""
    
    def wrap(*args, **kwargs):
       
        if not os.getuid() == 0:
            print("[ERROR]: This function requires root.")
            sys.exit(403) 
        else:
            f(*args, **kwargs)
    return wrap


def container_exist(cname):

    if POCKER_CONTAINER_PATH[-1] != '/':
        path = POCKER_CONTAINER_PATH + '/' + cname
    else:
        path = POCKER_CONTAINER_PATH + cname

    return os.path.isdir(path)


def has_disk_space():

    st = os.statvfs('/')
    gb = ((st.f_bsize * st.f_bavail)/(1024 * 1024 * 1024))
    
    return gb > 1

@superuser
def pocker_create(cname):
    if not has_disk_space():
        print("[ERROR] No space left.")
        sys.exit(0)

    if container_exist(cname):
        print("[ERROR] Container exist, try to start it.")
        sys.exit(0)

    print (" * Creating container: %s..." % (cname))

    options = {
       "dist": "ubuntu",
       "release": "trusty",
       "arch": "amd64"
    }
    container = lxc.Container(cname)
    if container.create("download", 0, options):
        print ("[OK] Container %s created." % cname)
    else:
        print ("[ERRO] Container %s not created." % cname)

@superuser
def pocker_start():
    pass


@superuser
def pocker_stop():
    pass


def pocker_list():
    pass


if __name__ == "__main__":
    print("This module isn't intended to be run directly.")
