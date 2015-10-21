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


from pocker import Pocker


if __name__ == '__main__':
    pocker = Pocker("amd64", "ubuntu", "trusty")
    pocker.create()
    pocker.start()
    pocker.get_ip()
    pocker.console()

