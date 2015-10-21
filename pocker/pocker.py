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


import lxc
import uuid
import os
import sys
import time


class Pocker(object):
    """Pocker...

    Args:
        arch (str): Image architeture.
        dist (str): Linux distribution.
        release (str): Distribution release.

    """

    CONTAINER_NAME = str(uuid.uuid1())
    CLONE_NAME = str(uuid.uuid1())
    RENAME_NAME = str(uuid.uuid1())

    def __init__(self, arch, dist, release):
        self.container = lxc.Container(self.CONTAINER_NAME)
        self.arch = arch
        self.dist = dist
        self.release = release

    def create(self):
        options = {
            "dist": self.dist,
            "release": self.release,
            "arch": self.arch
        }
        self.container.create("download", 0, options)

    def start(self):
        """Container Start. x) """
        self.container.start()
        #self.container.wait("RUNNING", 3)

    def get_ip(self):
        """Getting IP address. """
        count = 0
        ips = []
        while not ips or count == 10:
            ips = self.container.get_ips()
            time.sleep(1)
            count += 1

    def console(self):
        self.container.console(ttynum=1)


if __name__ == "__main__":
    print("This module isn't intended to be run directly.")
