# -*- coding: utf-8 -*-

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

import lxc


__all__ = ['pocker_create']

MIN_REQUIRED_FREE_SPACE = 1

POCKER_CONTAINER_PATH = os.environ.get('POCKER_CONTAINER_PATH',
                                       '/var/lib/lxc/')

DEFAULT_CONTAINER = {
    "arch": "amd64",
    "dist": "ubuntu",
    "release": "trusty"
}


def superuser(f):
    """Decorator to test whether the user is root."""

    def wrap(*args, **kwargs):
        if not os.getuid() == 0:
            print("[ERROR]: This function requires root.")
            sys.exit()
        else:
            f(*args, **kwargs)

    return wrap


def has_container(cname):
    """Verify if the container exists."""

    if POCKER_CONTAINER_PATH[-1] != '/':
        path = POCKER_CONTAINER_PATH + '/' + cname
    else:
        path = POCKER_CONTAINER_PATH + cname

    return os.path.isdir(path)


def _has_freespace():
    """Check free disk space. """

    st = os.statvfs('/')
    freespace = ((st.f_bsize * st.f_bavail)/(1024 * 1024 * 1024))

    return freespace > MIN_REQUIRED_FREE_SPACE


@superuser
def pocker_create(cname, options=DEFAULT_CONTAINER):
    """Creating a new container.

    Args:
      cname (str): Container name.
      options (dict of str: str): Container options.

    Returns:
        bool: True if successful, False otherwise.

    """

    if not _has_freespace():
        print("[ERROR] No space left.")
        sys.exit(0)

    if has_container(cname):
        print("[ERROR] Container exist, try to start it.")
        sys.exit(0)

    print ("[POCKER] Creating container: %s..." % (cname))

    container = lxc.Container(cname)
    if container.create("download", 0, options):
        print ("[OK] Container %s created." % cname)
    else:
        print ("[ERRO] Container %s not created." % cname)


def _is_pocker_running(cname):

    if not has_container(cname):
        print("[ERROR] Container does not exist.")
        return False

    if pocker_status(cname) == "RUNNING":
        return False

    return True


def pocker_status(cname):
    """ Container Status.

    Args:
      cname (str): Container name.

    Return:
      str: Container status.

   """

    if not has_container(cname):
        print("[ERROR] Container does not exist.")
        return False

    return lxc.Container(cname).state


@superuser
def pocker_destroy(cname):
    """ Destroy the conainter.

    Args:
      cname (str): Container name.

    Returns:
        bool: True if successful, False otherwise.

    """

    if not has_container(cname):
        print("[ERROR] Container does not exist.")
        return False

    if not _is_pocker_running(cname):
        print("[ERROR] Pocker is RUNNING, stop it first.")
        return False

    if lxc.Container(cname).destroy():
        print("[OK] Booooowwwwwww!!!")
    else:
        print("[ERROR] Container is indestructible")


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
