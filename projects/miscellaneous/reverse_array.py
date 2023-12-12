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
    
def find_duplicated(lst):

    for duplicated in range(1, 100):
        if lst.count(duplicated) > 1:
                return duplicated

    return None

def remove_duplicate(lst):

    for duplicated in range(1, 100):
        if lst.count(duplicated) > 1:
            lst.remove(duplicated)

    return None

def find_min_max(lst):

    return [min(lst), max(lst)]

def find_array_sum(lst, suma):

    length = len(lst)

    if sum(lst) < suma:
        return None
    else:
        for i in range(length):
            for j in range(i, length):
                if sum(lst[i: j]) == suma:
                    return lst[i: j]
