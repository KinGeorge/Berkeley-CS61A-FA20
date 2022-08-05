HW_SOURCE_FILE=__file__


def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """
    if x < 10 and x == 8:
        return 1
    elif x < 10:
        return 0
    else:
        return num_eights(x % 10) + num_eights(x  // 10)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    """
    """
    Non-Recursive Version
    index, ppn, dir = 1, 1, 1
    while index != n:
        index += 1
        ppn += dir
        if index % 8 == 0 or num_eights(index):
            dir = -dir
    return ppn
    """
    def helper(index, ppn, dir):
        while(index<n):
            if index % 8 == 0 or num_eights(index):
                dir = -dir
                return helper(index+1, ppn+dir, dir)
            else:
                return helper(index+1, ppn+dir, dir)
        return ppn
    return helper(1, 1, 1)

            
            
def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    def helper(n, k, result=0):
        if n == 0:
            return result
        else:
            without_last, last = n // 10, n % 10
            if k - last > 1:
                return helper(without_last, last, result+(k-last-1))
            else:
                return helper(without_last, last, result)
                              
    return helper(n, n%10)

def next_largest_coin(coin):
    """Return the next coin. 
    >>> next_largest_coin(1)
    5
    >>> next_largest_coin(5)
    10
    >>> next_largest_coin(10)
    25
    >>> next_largest_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def count_coins(total):
    """Return the number of ways to make change for total using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])                                          
    True
    """
    def helper(remain, smallest_coin):
        if remain == 0:
            return 1
        elif remain < 0:
            return 0
        elif smallest_coin == None:
            return 0
        else:
            with_smallest = helper(remain, next_largest_coin(smallest_coin))
            wo_smallest = helper(remain-smallest_coin, smallest_coin)
            return with_smallest+wo_smallest
        
    return helper(total, 1)
        
        

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return lambda b: (lambda a, b: a(a, b)) (lambda a, b: b*a(a, b-1) if b > 0 else 1, b)

