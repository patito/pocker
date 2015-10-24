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


import argparse

import pocker


def main():
    parser = argparse.ArgumentParser(
        description='Messing arount with LXC and Python.')
    subparsers = parser.add_subparsers(help='commands')

    # Command: pocker create <OPTIONS>
    create = subparsers.add_parser('create', help='Create new container.')
    create.add_argument('-n', '--name', type=str, help='Container name',
                        required=True)
    create.add_argument('-d', '--dist', type=str, help='Distribution',
                        required=True)
    create.add_argument('-r', '--release', type=str, help='Release',
                        required=True)
    create.add_argument('-a', '--arch', type=str, help='Release',
                        required=True)
    create.set_defaults(function=pocker.pocker_create)

    # Command: pocker start <OPTIONS>
    start = subparsers.add_parser('start', help='Start a container.')
    start.add_argument('-n', '--name', type=str, help='Container name',
                       required=True)
    start.set_defaults(function=pocker.pocker_start)

    # Command: pocker stop <OPTIONS>
    stop = subparsers.add_parser('stop', help='Stop a container.')
    stop.add_argument('-n', '--name', type=str, help='Container name',
                      required=True)
    stop.set_defaults(function=pocker.pocker_stop)

    # Command: pocker destroy <OPTIONS>
    destroy = subparsers.add_parser('destroy', help='Destroy a container.')
    destroy.add_argument('-n', '--name', type=str, help='Container name',
                         required=True)
    destroy.set_defaults(function=pocker.pocker_destroy)

    args = parser.parse_args()
    if 'release' in args:
        options = {
            "arch": args.arch,
            "dist": args.dist,
            "release": args.release
        }
        args.function(args.name, options)
    else:
        args.function(args.name)


if __name__ == '__main__':
    main()
