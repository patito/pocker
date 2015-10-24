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


    def setUp(self):
        #self.cname = str(uuid.uuid1())
        self.cname = "test"

    def test_upper(self):
        pass
        # self.cname = str(uuid.uuid1())

    def test_create(self):
        pocker.pocker_create(self.cname, pocker.DEFAULT_CONTAINER)
        self.assertTrue(pocker.has_container(self.cname))

    def test_destroy(self):
        pocker.pocker_destroy(self.cname)
        self.assertFalse(pocker.has_container(self.cname))


if __name__ == '__main__':
    unittest.main()
