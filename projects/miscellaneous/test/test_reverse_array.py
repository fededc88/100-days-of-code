import unittest 

import reverse_array as ra

class test_reverse_array_in_place(unittest.TestCase):


    def test_reverse_arrat_in_place(self):
        lst = ['1', '2', '3', 'p', 'r', 'o', 'b', 'a', 'n', 'd', 'o', '!']
        lst_reverse = ['!','o', 'd','n', 'a', 'b', 'o', 'r', 'p', '3', '2', '1']

        self.assertListEqual(ra.reverse_array_in_place(lst), lst_reverse)

if __name__ == '__main__':
    unittest.main()
    
