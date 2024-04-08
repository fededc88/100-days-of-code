import unittest
from unittest.mock import MagicMock
from master import master


class test_master(unittest.TestCase):
    
    def setUp(self):
        global mst
        mst = master(MagicMock(name='transport'));

    def test_connect(self):
        self.assertTrue(mst.connect())

if __name__ == '__main__':
    unittest.main()
    


