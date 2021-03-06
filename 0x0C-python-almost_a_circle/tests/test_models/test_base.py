#!/usr/bin/python3


import unittest
from models import base
from models.base import Base
Base = Base


class TestBase(unittest.TestCase):

    def test_doc(self):
        self.assertTrue(len(base.__doc__) > 0)

    def test_id(self):
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

if __name__ == '__main__':
    unittest.main()
