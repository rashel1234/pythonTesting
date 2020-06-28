import unittest
import add

class TestBasic(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add.add(2,2), 4)
