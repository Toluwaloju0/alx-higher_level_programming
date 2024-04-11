#!/usr/bin/python3
"""A module to tests the Base class"""


from models.base import Base
import unittest


a = Base()
b = Base()
c = Base(89)

class Testbase_id(unittest.TestCase):
    def test_base_id(self):
        self.assertEqual(a.id, 1)
        self.assertEqual(b.id, a.id + 1)
        self.assertEqual(c.id, 89)
        self.assertNotEqual(a.id, b.id)
