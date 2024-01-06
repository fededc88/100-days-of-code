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

def find_array_sum_len(lst, nlen):

    length = len(lst)

    max_sum = 0
    
    for i in range(0, length - (nlen - 1)):
        #print(lst[i])
        suma = sum(lst[i:(i+nlen)])
        if suma >  max_sum:
            max_sum = suma
            lst_max = lst[i:i+nlen]

    return lst_max

def find_longest_common_array(lst_one, lst_two):

    len_one = len(lst_one)
    len_two = len(lst_two)

    buff_longhest = list()

    for i in range(len_one):
        for j in range(len_two):
            for k in range(len_one-i):
                if lst_one[i:i+k] == lst_two[j:j+k]:
                    if len(lst_one[i:i+k]) > len(buff_longhest):
                        buff_longhest = lst_one[i:i+k]
                        #print(buff_longhest)

    return buff_longhest

def find_shortest_common_array(lst_one, lst_two):

    len_one = len(lst_one)
    len_two = len(lst_two)

    buff = list()
    buff_lst = list()
    break_len = 0

    for i in range(len_one):
        if break_len:
            break_len -= 1
            continue

        for j in range(len_two):
            for k in range(len_one-i):
                #print('K:' + str(k))
                if lst_one[i:i+k] == lst_two[j:j+k]:
                    buff = lst_one[i:i+k]
                elif len(buff) > 1:
                    buff_lst.append(buff)
                    break_len = len(buff) - 1
                    #print(buff)
                    break
            if break_len:
                break

    lst_short = list()
    for lst in buff_lst:
        if len(lst) < len(lst_short) or len(lst_short) == 0:
            lst_short = lst

    return lst_short

def is_the_subarray_partiionable(lst):

    for i in range(len(lst)):
        if sum(lst[:i]) == sum(lst[i:]):
            return [lst[:i],lst[i:]]

    return -1

        
