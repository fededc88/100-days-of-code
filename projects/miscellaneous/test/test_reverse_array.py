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

        lst_missing = self.__get_unsorted_list__(100)

        # get a random missing object
        missing_idx = int(random.randrange(0,99))
        
        # save it for the testing and miss it
        missing_number = lst_missing[missing_idx]
        lst_missing.remove(missing_number)

        self.assertEqual(ra.find_missing_number(lst_missing), missing_number)

    def test_find_duplicated(self):
        # Write a function that finds the duplicate number in an unsorted array
        # containing every number from 1 to 100.

        # Only one of the numbers will appear twice.

        lst_duplicated = self.__get_unsorted_list__(99)

        # get a random number
        duplicated = int(random.randrange(0,99))
        lst_duplicated.append(duplicated)

        self.assertEqual(ra.find_duplicated(lst_duplicated), duplicated)

    def test_remove_duplicate(self):
        # Write a function that removes every duplicate value in an array.
        
        # There could be more than one value duplicated. You should remove all
        # of them leaving a single copy of the value.

        lst_duplicated = self.__get_unsorted_list__(99)

        # get a random number
        duplicated = int(random.randrange(0,99))
        lst_duplicated.append(duplicated)

        ra.remove_duplicate(lst_duplicated)

        self.assertEqual(ra.find_duplicated(lst_duplicated), None)

    def test_find_min_max(self):
        # Write a function that finds the largest and smallest number in an
        # unsorted array.
        lst = self.__get_unsorted_list__(99)
        
        self.assertListEqual(ra.find_min_max(lst), [1, 98])

    def test_find_array_sum(self):
        # Write a function that finds a subarray whose sum is equal to a given
        # value.
        lst = self.__get_unsorted_list__(20)

        suma = 35;
        
        self.assertEqual(sum(ra.find_array_sum(lst, suma)), suma)

    def __get_unsorted_list__(self, nelements):
        # create the list of nelements and shuffle it
        lst_shuffled = [d for d in range (1,nelements)]
        random.shuffle(lst_shuffled)
        return lst_shuffled


if __name__ == '__main__':
    unittest.main()
    
