#. Write a function that reverses an array in place.

#In other words, the function should not use an auxiliary array to do the work.


def reverse_array_in_place(lst):

    lst = lst[::-1]
    
    return lst   

def find_missing_number(lst):

    for missing_number in range(1,100):
        try:
            lst.index(missing_number)
        except ValueError:
            return missing_number

    return None
    
