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


POCKER_CONTAINER_PATH = os.environ.get('POCKER_CONTAINER_PATH', '/var/lib/lxc/')


if __name__ == '__main__':
    print('This module isn\'t intended to be run directly.')
