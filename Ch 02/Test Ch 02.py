__author__ = 'Rolando'


def addition(n, k):
    """ return the sum of n and k using recursion
    """

    if k == 0:
        return n
    elif k < 0:
        return addition(n - 1, k + 1)
    else:
        return addition(n + 1, k - 1)

print('\n# Addition')
print(addition(10, 10))
print(addition(11, -2))


def multiplication(n, k):
    """ Returns the product of n and k using recursion
    """

    if k == 0:
        return 0
    elif k < 0:
        return - n - multiplication(-n, k + 1)
    else:
        return n + multiplication(n, k - 1)

print('\n# Multiplication')
print(multiplication(10, 10))
print(multiplication(10, -3))


def division(n, k):
    """ Returns the quotient of n and k using recursion
    """

    if n == 0:
        return 0
    else:
        return 1 + division(n - k, k)

print('\n# Division')
print(division(10, 2))


def list_count(lst):
    """ returns a count of items in a list
    """

    if lst is []:
        return 0
    else:
        return 1 + len(lst[1:])

print('\n# list len')
list_0 = [1, 2, 3, 4]
print(list_count(list_0))


def list_increment(lst):
    """ Returns a copy of lst with each item incremented by 1
    """

    if len(lst) <= 1:
        return [lst[0] + 1]
    else:
        result = [lst[0] + 1]
        result.extend(list_increment(lst[1:]))
        return result

print('\n# list increment')
print(list_increment(list_0))


def list_multiply(lst):
    """ Returns a copy of lst with each item multiplied by 2
    """

    if len(lst) <= 1:
        return [lst[0] * 2]
    else:
        result = [lst[0] * 2]
        result.extend(list_multiply(lst[1:]))
        return result

print('\n# list multiply')
print(list_multiply(list_0))


def map_function(func, lst):
    """ Applies a function to each item in the list
    """

    if len(lst) <= 1:
        return [func(lst[0])]
    else:
        result = [func(lst[0])]
        result.extend(map_function(func, lst[1:]))
        return result

list_neg = (-1, 2, -3, 4)
print('\n# list function')
print(map_function(abs, list_neg))


def d2x(n, x):
    """ Takes a non-negative integer (n) and an integer (x) and returns a string of digits that
        represents the base-x representation of n
    """
    s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    places = 0
    result = ''

    # if n < x:
    #     return n

    while n - x ** places > 0:
        places += 1

    print(places)
    if n < x:
        return n

    places -= 1
    while places > -1:
        result += (s[n // (x ** places)])
        n -= (n // x ** places) * x ** places
        places -= 1
        print(result)
    return result

print('\n# d2x')
# print(d2x(0, 2))
# print(d2x(1, 2))
print(d2x(10, 2))
print(d2x(10, 3))
# print(d2x(10, 8))

# print(d2x(231, 16))


