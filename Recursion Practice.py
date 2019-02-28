""" This file is to practice recursion.
"""
from typing import Any


def binary_search(lst: list, item: Any) -> bool:
    """ Uses recursion to compute the binary search.

    Precondition: The list is sorted

    >>> binary_search([1], 1)
    True
    >>> binary_search([1,2,3,4], 5)
    False
    >>> binary_search([421,5432,7456], 1)
    False
    """
    mid = int(len(lst)/2)
    if len(lst) == 0:
        return False
    elif item == lst[mid]:
        return True
    elif item > lst[mid]:
        return binary_search(lst[mid+1:], item)
    else:
        return binary_search(lst[:mid], item)


def sum_of_digits(n: int) -> int:
    """ Returns the sum of the digits of the number.

    >>> sum_of_digits(123)
    6
    >>> sum_of_digits(8923)
    22
    """
    if n < 10:
        return n
    else:
        s = 0
        s += (n % 10) + sum_of_digits(n//10)
        return s


def palindrome(s: str) -> bool:
    """ Check if a number is a palindrome.

    >>> palindrome("2")
    True
    >>> palindrome("")
    True
    >>> palindrome("racecar")
    True
    >>> palindrome("cool")
    False
    """
    if len(s) < 2:
        return True
    else:
        if s[0] == s[len(s)-1]:
            return palindrome(s[1:len(s)-1])
        else:
            return False


def factorial(n: int) -> int:
    """ Returns the factorial of the number given.

    >>> factorial(2)
    2
    >>> factorial(4)
    24
    >>> factorial(5)
    120
    """
    if n <= 1:
        return 1
    else:
        prod = n
        prod *= factorial(n - 1)
        return prod


def fibonnaci(c: int, a: int = 0, b: int = 1) -> str:
    """ Returns the fibonacci series upto the number that is entered.

    >>> fibonnaci(7)
    '0->1->1->2->3->5->8'
    >>> fibonnaci(3)
    '0->1->1'
    """
    if c <= 2:
        return str(a)+"->"+str(b)
    else:
        return str(a)+"->"+ fibonnaci(c-1, b, a + b)


def tribonnaci(d: int, a: int = 0, b: int = 1, c: int = 1) -> str:
    """ Returns the tribonnaci series.

    >>> tribonnaci(6)
    '0->1->1->2->4->7'
    >>> tribonnaci(5)
    '0->1->1->2->4'
    """
    if d <= 3:
        return str(a) + "->" + str(b)+"->" + str(c)
    else:
        return str(a) + "->" + tribonnaci(d-1, b, c, a+b+c)

if '__main__' == __name__:

    import doctest
    doctest.testmod()
