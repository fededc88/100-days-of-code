import unittest 
import random

import reverse_array as ra

class test_reverse_array_in_place(unittest.TestCase):


    def test_reverse_arrat_in_place(self):

        lst = ['1', '2', '3', 'p', 'r', 'o', 'b', 'a', 'n', 'd', 'o', '!']
        lst_reverse = ['!','o', 'd','n', 'a', 'b', 'o', 'r', 'p', '3', '2', '1']

        self.assertListEqual(ra.reverse_array_in_place(lst), lst_reverse)
        self.assertMultiLineEqual(ra.reverse_array_in_place("1 2 3 probando!"), "!odnaborp 3 2 1")

    def test_find_missing_number(self):
    # Write a function that finds the missing number in an unsorted array
    # containing every one of the other 99 numbers ranging from 1 to 100.

        # create the list and shuffle it
        lst_missing = [d for d in range (1,100)]
        random.shuffle(lst_missing)

        # get a random missing object
        missing_idx = int(random.randrange(0,99))
        
        # save it for the testing and miss it
        missing_number = lst_missing[missing_idx]
        lst_missing.remove(missing_number)

        self.assertEqual(ra.find_missing_number(lst_missing), missing_number)

if __name__ == '__main__':
    unittest.main()
    
