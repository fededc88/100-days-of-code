import unittest 

import reverse_array as ra

class test_reverse_array_in_place(unittest.TestCase):

    lst = ['1', '2', '3', 'p', 'r', 'o', 'b', 'a', 'n', 'd', 'o', '!']
    lst_reverse = ['!','o', 'd','n', 'a', 'b', 'o', 'r', 'p', '3', '2', '1']

    def test_reverse_arrat_in_place(self):

        self.assertListEqual(ra.reverse_array_in_place(self.lst), self.lst_reverse)
        self.assertMultiLineEqual(ra.reverse_array_in_place("1 2 3 probando!"), "!odnaborp 3 2 1")

if __name__ == '__main__':
    unittest.main()
    
