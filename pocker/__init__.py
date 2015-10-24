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

from . import util


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
            print("%s[ERROR]%s This function requires root." %
                  (util.RED, util.NORMAL))
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
        print("%s[ERROR]%s No space left." % (util.RED, util.NORMAL))
        return False

    if has_container(cname):
        print("%s[ERROR]%s Container exist, try to start it." %
              (util.RED, util.NORMAL))
        return False

    print ("%s[OK]%s Creating container: %s..." %
           (util.GREEN, util.NORMAL, cname))

    container = lxc.Container(cname)
    if container.create("download", 0, options):
        print ("%s[OK]%s Container %s created." %
               (util.GREEN, util.NORMAL, cname))
    else:
        print ("%s[ERRO]%s Container %s not created." %
               (util.RED, util.NORMAL, cname))


def _is_pocker_running(cname):

    if not has_container(cname):
        print ("%s[ERRO]%s Container does not exist." %
               (util.RED, util.NORMAL))
        return False

    if pocker_status(cname) != "RUNNING":
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
        print ("%s[ERRO]%s Container does not exist." %
               (util.RED, util.NORMAL))
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
        print ("%s[ERRO]%s Container does not exist." %
               (util.RED, util.NORMAL))
        return False

    if not _is_pocker_running(cname):
        print ("%s[ERRO]%s Pocker is RUNNING, stop it first." %
               (util.RED, util.NORMAL))
        return False

    if lxc.Container(cname).destroy():
        print ("%s[OK]%s Booowwwwww!!!." % (util.GREEN, util.NORMAL))
    else:
        print ("%s[ERRO]%s Container is indestructible." %
               (util.RED, util.NORMAL))


@superuser
def pocker_start(cname):
    """Start the conainter.

    Args:
      cname (str): Container name.

    Returns:
        bool: True if successful, False otherwise.

    """

    if not has_container(cname):
        print("%s[ERRO]%s Container does not exist." % (util.RED, util.NORMAL))
        return False

    if  _is_pocker_running(cname):
        print("%s[ERRO]%s Pocker is RUNNING." %
               (util.RED, util.NORMAL))
        return False

    cont = lxc.Container(cname)
    if cont.start():
        print("%s[OK]%s Container started." % (util.GREEN, util.NORMAL))
        return True
 
    print ("%s[ERROR]%s Container not started." % (util.RED, util.NORMAL))

    return False


@superuser
def pocker_stop(cname):
    """Stop the conainter.

    Args:
      cname (str): Container name.

    Returns:
        bool: True if successful, False otherwise.

    """

    if not has_container(cname):
        print("%s[ERRO]%s Container does not exist." % (util.RED, util.NORMAL))
        return False

    if  not _is_pocker_running(cname):
        print("%s[ERRO]%s Pocker is not RUNNING." %
               (util.RED, util.NORMAL))
        return False

    cont = lxc.Container(cname)
    if cont.stop():
        print("%s[OK]%s Container stopped." % (util.GREEN, util.NORMAL))
        return True
 
    print ("%s[ERROR]%s Container not stopped." % (util.RED, util.NORMAL))

    return False


def pocker_list():
    """List all conainters.
    """

    print ("%s   NAME \t STATUS %s" % (util.CYAN, util.NORMAL))
    dirs = os.listdir(POCKER_CONTAINER_PATH)
    for container in dirs:
        print ("   %s \t %s" % (container, pocker_status(container)))


if __name__ == "__main__":
    print("This module isn't intended to be run directly.")
