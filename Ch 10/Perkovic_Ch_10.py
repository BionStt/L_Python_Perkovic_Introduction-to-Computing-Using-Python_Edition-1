__author__ = 'Rolando'



# 10.1

# def countdown0(n):
#     print(n)
#     countdown0(n - 1)


def countdown(n):
    """ Counts down to 0
    """

    if n <= 0:                   # base case: n reaches 0
        print('Blastoff!!!')
    else:                       # n > 0: recursive step
        print(n)                # print n first and the
        countdown(n - 1)        # countdown from n-1

print(countdown(10))


def vertical(n):
    """ Prints digits on n vertically
    """

    if n < 10:                  # base case: n has 1 digit (n < 10)
        print(n)
    else:                       # recursive step: n has 2 or more digits
        vertical(n // 10)       # recursively print all but last digit
        print(n % 10)           # print last digit of n

print(vertical(3124))


def pattern(n):
    """ Prints the n-th pattern
    """

    if n == 0:                  # base case
        print(0, end=' ')
    else:                       # recursive step: n > 0
        pattern(n - 1)          # print n-1st pattern
        print(n, end=' ')       # print n
        pattern(n - 1)          # print n-1st pattern

print(pattern(4))


def koch(n):
    """ Returns turtle directions for drawing curve Koch(n)
    """

    if n == 0:                  # base case
        return 'F'

    tmp = koch(n - 1)           # recursive step: get directions for Koch(n - 1)
                                # use them to construct direction for Koch(n - 1)
    return tmp + 'L' + tmp + 'R' + tmp + 'L' + tmp

from turtle import Screen, Turtle


def draw_koch(n):
    """ Draws nth Koch curve using instructions from function koch()
    """

    s = Screen()                        # create screen
    t = Turtle()                        # create turtle
    directions = koch(n)                # obtain directions to draw koch(n)

    for move in directions:             # follow specified moves
        if move == 'F':
            t.forward(300 / 3 ** n)     # move forward, length normalized
        if move == 'L':
            t.lt(60)                    # rotate left 60 degrees
        if move == 'R':
            t.rt(120)                   # rotate right 60 degrees

    s.bye()

import os


def scan(pathname, signatures):
    """ Recursively scans files contained directly
        or indirectly, in folder pathname
    """

    for item in os.listdir(pathname):           # for every file or folder
                                                # in folder pathname
        # create pathname for item called next1
        # next1 = pathname + '/' + item          # Mac only
        # next1 = pathname + '\' + item          # Windows only
        next1 = os.path.join(pathname, item)     # any OS

        try:                                    # blindly recurse on next
            scan(next1, signatures)
        except:                                 # base case: exception means that next is a file
            for virus in signatures:
                # check if file next has virus signature
                if open(next1).read().find(signatures[virus]) >= 0:
                    print('{}, found virus {}'.format(next1, virus))


def power(a, n):
    """ Returns a to the n-th power
    """

    res = 1
    for i in range(n):
        res *= a
    return res

p_counter = 0


def rpower(a, n):
    """ Returns a to the n-th power using recursion
    """

    global p_counter

    if n == 0:                   # base case: n == 0
        return 1

    tmp = rpower(a, n // 2)     # recursive step : n > 0

    if n % 2 == 0:
        p_counter += 1
        return tmp * tmp        # a ** n = a ** (n//2) * a ** a(n//2)
    else:
        p_counter += 2
        return a * tmp * tmp    # a ** n = a ** (n//2) * a ** a(n//2) * a


def fib(n):
    """ Returns n-th Fibonacci number
    """

    previous = 1        # 0th Fibonacci number
    current = 1         # 1st Fibonacci number
    i = 1               # index of current Fibonacci number

    while i < n:        # while current is not nth Fibonacci number
        previous, current = current, previous + current
        i += 1

    return current

f_counter = 0


def rfib(n):
    """ Returns n-th Fibonacci number using recursion
    """
    global f_counter

    if n < 2:
        return 1                        # base: case

    f_counter += 1
    return rfib(n - 1) + rfib(n - 2)    # recursive step


import time


def timing(func, n):
    """ Runs func on input returned by buildInput
    """

    func_input = build_input(n)   # obtain input for func

    start = time.time()         # take start time
    func(func_input)             # run func on funcInput
    end = time.time()           # take end time

    return end - start          # return execution time


# def build_input(n):
#     """ Returns input for Fibonacci functions
#     """
#     return n


def timing_analysis(func, start, stop, inc, runs):
    """ Prints average run times of function func on inputs of
        size start, start+inc, start+2*inc, ..., up to stop
    """

    for n in range(start, stop, inc):           # for every input size n
        acc = 0.0                               # initialize accumulator

        for i in range(runs):                   # repeat runs times:
            acc += timing(func, n)              # run func on input size n
                                                # and accumulates run times
        # print average run times for input size n
        format_str = 'Run time of {}({}) is {:.7f} seconds.'
        print(format_str.format(func.__name__, n, acc / runs))


def search(lst, target, i, j):
    """ Attempts to find target in sorted sub-list lst[i:j];
        index of target is returned if found, -1 otherwise
    """

    if i == j:                      # base case: empty lit
        return -1                   # target cannot be in list

    mid = (i + j) // 2              # index of median of l[i:j]

    if lst[mid] == target:          # target is the median
        return mid

    if target < lst[mid]:           # search left of median
        return search(lst, target, i, mid)

    else:
        return search(lst, target, mid + 1, j)

import random


def binary(lst):
    """ Chooses item in list lst at random and runs search() on it
    """

    target = random.choice(lst)
    return search(lst, target, 0, len(lst))


def linear(lst):
    """ Chooses item in list lst at random and runs index() on it
    """

    target = random.choice(lst)
    return lst.index(target)


def dup1(lst):
    """ Returns True if list lst has duplicates, False otherwise
    """

    for item in lst:
        if lst.count(item) > 1:
            return True
    return False


def dup2(lst):
    """ Returns True if list lst has duplicates, False otherwise
    """

    lst.sort()
    for index in range(1, len(lst)):
        if lst[index] == lst[index - 1]:
            return True
    return False


def dup3(lst):
    """ Returns True if list has duplicates, False otherwise
    """

    s = set()
    for item in lst:
        if item in s:
            return False
        else:
            s.add(item)
    return True


def dup4(lst):
    """ Returns True if list lst has duplicates, False otherwise
    """

    return len(lst) != len(set(lst))


def kth_smallest(lst, k):
    """ Returns the k-th smallest item in lst
    """

    lst.sort()
    return lst[k - 1]


def frequent(lst):
    """ Returns mst frequently occurring item
        in non-empty list lst using a list
    """

    lst.sort()                                  # first sort list

    current_len = 1                             # length of current sequence
    longest_len = 1                             # length of longest sequence
    most_freq = lst[0]                          # item with longest sequence

    for i in range(1, len(lst)):
        # compare current item with previous
        if lst[i] == lst[i - 1]:                # if equal
            current_len += 1                    # current sequence continues
        else:                                   # if not equal
            if current_len > longest_len:       # if sequence that ended
                                                # is longest so far
                longest_len = current_len       # store its length
                most_freq = lst[i - 1]
            current_len = 1                     # new sequence starts

    return most_freq


def frequent2(lst):
    """ Returns most frequently occurring item
        in non-empty list lst using a dictionary
    """

    counters = {}                               # initialize dictionary for counters

    for item in lst:
        if item in counters:                    # if counter for item already exists
            counters[item] += 1                 # increment it
        else:                                   # otherwise, create a counter
            counters[item] = 1                  # for item starting at 1

    return counters

############
### 10.1 ###
############
print('\nPP 10.1')


def reverse(n):
    """ Takes a non-negative integer as input and prints the digit n vertically, starting with the lower digit
    """

    if n < 10:                  # base case: one has 1 digit
        print(n)
    else:                       # recursive step: n has at least 2 digits
        print(n % 10)           # print last digit of n
        reverse(n // 10)        # recursively print in reverse all but the last digit

print(reverse(42121))

############
### 10.2 ###
############
print('\nPP 10.2')


def cheers(n):
    """ Takes an integer and out puts n copies of 'Hip', followed by 'Hurray!!!'
    """

    if n <= 0:
        print('Hurray!!!')
    else:
        print('Hip', end=' ')
        cheers(n - 1)

print(cheers(2))

############
### 10.3 ###
############
print('\nPP 10.3')


def factorial(n):
    """ returns the factorial of integer n
    """

    if n in [0, 1]:                     # base case
        return 1
    return factorial(n - 1) * n         # recursive step: n > 1

############
### 10.4 ###
############
print('\nPP 10.4')


def pattern2(n):
    """
    """

    if n > 0:
        pattern2(n - 1)
        print('*' * n)
        pattern2(n - 1)

print(pattern2(3))

############
### 10.5 ###
############
print('\nPP 10.5')


def snowflake(n):
    """ Draws n-th snowflake curve using Koch() 3 times
    """

    s = Screen()
    t = Turtle()
    directions = koch(n)

    for i in range(3):
        for move in directions:     # draw hook (n)
            if move == 'F':
                t.fd(300 / 3 ** n)
            if move == 'L':
                t.lt(60)
            if move == 'R':
                t.rt(120)
        t.rt(120)

    s.bye()

############
### 10.6 ###
############
print('\nPP 10.6')

# print(timing_analysis(fib, 24, 35, 2, 100))
# print(timing_analysis(rfib, 24, 35, 2, 10))
#
#
# def build_input(n):
#     """ Returns input for Fibonacci functions
#     """
#     return n
#
# def power2(n):
#     return power(2, n)
#
#
# def rpower2(n):
#     return rpower(2, n)
#
#
# def pow2(n):
#     return 2 ** n
#
# print(timing_analysis(power2, 20000, 80000, 20000, 10))
# print(timing_analysis(rpower2, 20000, 80000, 20000, 10))      # faster
# print(timing_analysis(pow2, 20000, 80000, 20000, 10))         # faster

############
### 10.7 ###
############
print('\nPP 10.7')


# def build_input(n):
#     """  Returns a random sample of n numbers range [0, 2n)
#     """
#
#     lst = random.sample(range(2 * n), n)
#     lst.sort()
#     return lst
#
# print(timing_analysis(linear, 20000, 100000, 20000, 20))
# print(timing_analysis(binary, 20000, 100000, 20000, 20))      # faster
#
#
def build_input(n):
    """ Returns a list of n random integers in range [0, n ** 2)
    """

    res = []
    for i in range(n):
        res.append(random.choice(range(n ** 2)))
    return res
#
# print(timing_analysis(dup1, 2000, 10000, 2000, 10))
# print(timing_analysis(dup2, 2000, 10000, 2000, 10))
# print(timing_analysis(dup3, 2000, 10000, 2000, 10))
# print(timing_analysis(dup4, 2000, 10000, 2000, 10))           # fastest, speed decreases ascending statements ^

############
### 10.8 ###
############
print('\nPP 10.8')


print(timing_analysis(frequent, 2000, 10000, 2000, 10))
print(timing_analysis(frequent2, 2000, 10000, 2000, 10))

############
### 10.9 ###
############
print('\nPP 10.9')

# 10.9 does not ask for code

#############
### 10.10 ###
#############
print('\nPP 10.10')


def countdown2(n):
    """ Counts down from 0
    """

    if n <= 0:                   # base case: n reaches 0
        print('Blastoff!!!')
    else:                       # n > 0: recursive step
        countdown2(n - 1)
        print(n)


print(countdown2(3))

#############
### 10.11 ###
#############
print('\nPP 10.11')

# 10.11 does not ask for code

#############
### 10.12 ###
#############
print('\nPP 10.12')


def countdown3(n):
    """ Counts down to zero, saying boom halfway
    """

    if n <= 0:
        print('Blastoff!!!')
    elif n == 2:
        print('\tBOOOM!!!\n\tScared you...\n' + str(n))
        countdown3(n - 1)
    else:
        print(n)
        countdown3(n - 1)

print(countdown3(5))

#############
### 10.13 ###
#############
print('\nPP 10.13')

# 10.13 does not ask for code

#############
### 10.14 ###
#############
print('\nPP 10.14')


def combinations(n, k):
    """
    """

    if k == 0:
        return 1
    elif n < k:
        return 0
    else:
        return combinations(n - 1, k - 1) + combinations(n - 1, k)

print(combinations(1, 2))
print(combinations(2, 1))
print(combinations(5, 2))

#############
### 10.15 ###
#############
print('\nPP 10.15')

#############
### 10.16 ###
#############
print('\nPP 10.16')

#############
### 10.17 ###
#############
print('\nPP 10.17')


def silly(n):
    """ Takes n as input and prints n question marks, followed by n exclamation points.
    """

    if n <= 0:
        print('', end='')
    else:
        print('*', end='')
        silly(n - 1)
        print('!', end='')

print(silly(0))
print(silly(1))
print(silly(10))


#############
### 10.18 ###
#############
print('\nPP 10.18')


def num_ones(n):
    """ Takes a non-negative integer n as input and return the number of 1's in the binary representation of n
    """

    if n < 1:
        return 0
    else:
        return n % 2 + num_ones(n // 2)

print(num_ones(0))
print(num_ones(1))
print(num_ones(14))

#############
### 10.19 ###
#############
print('\nPP 10.19')


def rgdc(a, b):
    """
    """

    if b == 0:
        return a
    else:
        return rgdc(b, a % b)

print(rgdc(3, 0))
print(rgdc(18, 12))

#############
### 10.20 ###
#############
print('\nPP 10.20')


def rem(lst, temp=()):
    """ Takes a list and returns of copy of it in which one copy of every duplicate value is removed
    """

    items = list(temp)

    if len(lst) <= 1:
        if lst[0] in items:
            return [lst[0]]
        else:
            return []
    elif lst[0] in items:
        result = [lst[0]]
        result.extend(rem(lst[1:], items))
        return result
    else:
        result = []
        items.append(lst[0])
        result.extend(rem(lst[1:], items))
        return result

print(rem([4]))
print(rem([4, 4]))
print(rem([4, 1, 3, 2]))
print(rem([2, 4, 2, 4, 4]))

#############
### 10.21 ###
#############
print('\nPP 10.21')


def address(lst):
    """ Find the median using recursion, if there are two medians, use smallest one
    """

    if len(lst) <= 2:
        return lst[0]
    else:
        lst.sort()
        return address(lst[1:-1])


print(address([2, 1, 8, 5, 9]))
print(address([2, 1, 8, 9]))
print(address([1, 1, 1, 2, 3, 3, 4, 4, 4, 5]))


#############
### 10.22 ###
#############
print('\nPP 10.22')


def base(n, b):
    """ Takes a non-negative integer n and a positive integer 1 < b < 10
        and prints base-b representation of integer n
    """

    if n < b:
        return n

    places = get_places(n, b)

    return get_result(n, b, places - 1)


def get_places(n, b, places=0):
    """
    """

    if n - b ** places <= 0:
        return 0
    else:
        return 1 + get_places(n, b, places + 1)

st = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def get_result(n, b, places, result=''):
    """
    """

    global st

    if places <= -1:
        return ''
    else:
        en = (st[n // (b ** places)] +
              get_result(n - ((n // b ** places) * b ** places), b, places - 1, result + st[n // (b ** places)]))
        return en


print(base(0, 2))
print(base(1, 2))
print(base(10, 2))
print(base(10, 3))

#############
### 10.23 ###
#############
print('\nPP 10.23')


def tough(p, n):
    """ takes two non-negative integer arguments and outputs a pattern
    """
    if n == 0:
        return ''
    else:
        tough(p, n // 2)
        print(' ' * p + '*' * n)
        tough(p + n - n // 2, n // 2)


# print(tough(0, 0))
# print(tough(0, 1))
print(tough(0, 2))
print(tough(0, 4))

#############
### 10.24 ###
#############
print('\nPP 10.24')


def permutations(lst):
    """ Takes a lst and returns a list of all the permutations of lst
    """

    if len(lst) <= 1:
        return [lst]
    else:
        result = []
        x = lst[0]
        xs = permutations(lst[1:])

        for i in xs:
            for j in range(len(lst)):
                new_i = i[:j] + [x] + i[j:]
                result.append(new_i)

        return result

    # else:
    #     result = []
    #     for i in range(len(lst)):
    #         x = lst[i]
    #         xs = lst[:i] + lst[i + 1:]
    #         for p in permutations(xs):
    #             result.append([x] + p)
    #     return result

print(permutations([1, 2, 3]))


#############
### 10.25 ###
#############
print('\nPP 10.25')


def anagrams(file, word):
    """ Takes a dictionary file and a word, and prints
        all anagrams of the word that are in the dictionary
    """

    infile = open(file, 'r')
    content = infile.read()
    content = content.split('\n')
    for i in content:
        i.strip()
    infile.close()

    ana_list = make_anagrams(word)
    ana_list.remove(word)
    print(ana_list)
    for i in ana_list:
        if i in content:
            print(i)


def make_anagrams(word):
    """
    """
    if len(word) <= 1:
        return word
    else:
        result = []
        x = word[0]
        xs = make_anagrams(word[1:])

        for i in xs:
            for j in range(len(word)):
                new_i = i[:j] + x + i[j:]
                result.append(new_i)

        return result

print(anagrams('dictionary.txt', 'trace'))

#############
### 10.26 ###
#############
print('\nPP 10.26')


def pairs1(lst, n):
    """ Takes a list of integers and an integer target value and returns True
        if there are more than two numbers in the list that add up to the target
        and false otherwise
    """

    for i in range(len(lst)):
        for j in range(len(lst)):
            if i == j:
                continue
            else:
                if lst[i] + lst[j] == n:
                    return True
    return False


def pairs2(lst, n):
    """
    """

    lst.sort()

    for i in range(len(lst)):
        for j in range(len(lst)):
            if i == j:
                continue
            else:
                if lst[i] + lst[j] == n:
                    return True
    return False

list_p = [4, 1, 9, 3, 5]
print(pairs1(list_p, 13))
print(pairs1(list_p, 11))

#############
### 10.27 ###
#############
print('\nPP 10.27')


def crawl(file):
    """ Takes a file and prints each file being visited, opens the file,
        reads each link, and recursively continues the crawl on each link
    """

    infile = open(file)
    content = infile.read()
    content = content.split('\n')

    print('Visiting', file)

    for i in content:
        if '.txt' not in i:
            return ''
        else:
            crawl(i)

print(crawl('file0.txt'))

#############
### 10.28 ###
#############
print('\nPP 10.28')


def pascal_line(n):
    """ Takes n and returns a list containing the sequence of
        numbers appearing in the nth line of Pascal's triangle
    """

    if n <= 0:
        return [1]
    else:
        result = []
        xs = pascal_line(n - 1)
        result.extend(xs)
        result.append(1)

        for i in range(1, (len(xs))):
            result[i] = xs[i - 1] + xs[i]

        return result

print(pascal_line(4))

#############
### 10.29 ###
#############
print('\nPP 10.29')


def traverse(pathname, d):
    """ Takes as input a pathname of a folder (str) and an integer d,
        and prints on the screen the pathname of every file and sub-folder
        path contained in the folder, directly or indirectly
    """

    for item in os.listdir(pathname):
        next1 = os.path.join(pathname, item)

        try:
            print('{}{}'.format('    ' * d, next1))
            traverse(next1, d + 1)
        except:
            pass

print(traverse('test', 0))

#############
### 10.30 ###
#############
print('\nPP 10.30')


def search_2(filename, pathname):
    """ Takes the name of a file and the pathname of a folder and searches for the file
        in the older and any sub-folder contained in it, direct;y or indirectly.
    """

    for item in os.listdir(pathname):
        next1 = os.path.join(pathname, item)

        try:
            result = ''
            result += search_2(filename, next1)
            if result == '':
                return None
            return result
        except:
            if filename in next1[len(filename):]:
                return next1
            else:
                pass

print(search_2('fileE.txt', 'test'))

#############
### 10.31 ###
#############
print('\nPP 10.31')


def draw_levy(n):
    """ Draws nth Levy Curve using instructions from function levy
    """
    s = Screen()
    t = Turtle()
    directions = levy(n)

    for move in directions:
        if move == 'F':
            t.forward(300 / n)
        if move == 'L':
            t.lt(45)
        if move == 'R':
            t.rt(45)

    s.bye()


def levy(n):
    """ Returns turtle directions for levy curve
        Rules: first pattern is 'F'
               every next pattern replaces existing 'F' s with 'LFRRFL'
    """
    if n == 0:
        return 'F'
    else:
        symbols = levy(n - 1)
        return symbols.replace('F', 'LFRRFL')

# print(draw_levy(6))

#############
### 10.32 ###
#############
print('\nPP 10.32')


# a
def square(t, x, y, s):
    """ Draws a square centered at point x, y with side length s
    """

    t.penup()
    t.setx(x - s / 2)
    t.sety(y - s / 2)
    t.pendown()
    for i in range(4):
        t.forward(s)
        t.left(90)


# b
def squares(t, x, y, s, n):
    """ Draws square pattern
        Rules: When n = 0, nothing is drawn
               When n = 1, a square is drawn
               When n > 1, squares are repeatedly drawn at existing empty corners x-times
    """

    if n == 0:
        return None
    elif n == 1:
        return square(t, x, y, s)
    else:
        square(t, x, y, s)
        squares(t, x - s / 2, y - s / 2, s / 2.2, n - 1)
        squares(t, x + s / 2, y - s / 2, s / 2.2, n - 1)
        squares(t, x + s / 2, y + s / 2, s / 2.2, n - 1)
        squares(t, x - s / 2, y + s / 2, s / 2.2, n - 1)

# s = Screen()
# t = Turtle()
#
# print(squares(t, 0, 0, 100, 4))