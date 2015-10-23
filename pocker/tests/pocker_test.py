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


import sys
import uuid

import unittest

import pocker


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        pass

    def test_create(self):
        cname = str(uuid.uuid1())
        pocker.pocker_create(cname, pocker.DEFAULT_CONTAINER)
        self.assertTrue(pocker.container_exist(cname))


if __name__ == '__main__':
    unittest.main()
