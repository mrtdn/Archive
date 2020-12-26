lst = input('Please enter 10 numbers by space seperated: ').strip().split()
lst = [int(i) for i in lst]


def recur_minval(lst, n):
    """A function that returns the minimum value in a given list.

    Args:
        lst (list): list name as parameter
        n (int): length of the list - 1

    Returns:
        int: minimum value in the list
    """
    if n == 1:
        if lst[1] <= lst[0]:
            return lst[1]
        else:
            return lst[0]
    else:
        if lst[n] <= lst[n-1]:
            minval = lst[n]
            recur_min = recur_minval(lst, n - 2)
            if minval <= recur_min:
                return minval
            else:
                return recur_min
        else:
            minval = lst[n - 1]
            recur_min = recur_minval(lst, n - 2)
            if minval <= recur_min:
                return minval
            else:
                return recur_min
    
    
def recur_maxval(lst, n):
    """A function that calculates the max val in a list
    by using recursion functions.

    Args:
        lst (list): list name
        n (integer): use length(lst) - 1 for indexing without any trouble

    Returns:
        integer: maximum value in the list
    """
    if n == 1:
        if lst[1] >= lst[0]:
            return lst[1]
        else:
            return lst[0]
    else:
        if lst[n] >= lst[n-1]:
            maxval = lst[n]
            recur_max = recur_maxval(lst, n - 2)
            if maxval >= recur_max:
                return maxval
            else:
                return recur_max
        else:
            maxval = lst[n - 1]
            recur_max = recur_maxval(lst, n - 2)
            if maxval >= recur_max:
                return maxval
            else:
                return recur_max
            
            
def recur_sumval(lst, n):
    """A function that sums every element of a list by using recursion method.

    Args:
        lst (list): list name
        n (int): len(list) - 1

    Returns:
        int: returns the sum of elements in a list
    """
    sumval = 0
    if n == 0:
        return lst[0]
    else:
        sumval += lst[n] + recur_sumval(lst, n - 1)
        return sumval
    
print('Maximum value: ', recur_maxval(lst, len(lst) - 1))
print('Minimum value: ', recur_minval(lst, len(lst) - 1))
print('Average value: ', (recur_sumval(lst, len(lst) - 1) / len(lst)))