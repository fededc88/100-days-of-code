#. Write a function that reverses an array in place.

#In other words, the function should not use an auxiliary array to do the work.


def reverse_array_in_place(lst):

    # get lst class type
    lst_type = type(lst)

    if lst_type is list:
        lst = lst[::-1]

    elif lst_type is str:
        lst = lst[::-1]
    
    return lst   
