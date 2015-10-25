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

from . import colors


def superuser(f):
    """Decorator to test whether the user is root."""

    def wrap(*args, **kwargs):
        if not os.getuid() == 0:
            print("%s[ERROR]%s This function requires root." %
                  (colors.RED, colors.NORMAL))
            sys.exit()
        else:
            f(*args, **kwargs)

    return wrap


if __name__ == "__main__":
    print("This module isn't intended to be run directly.")
