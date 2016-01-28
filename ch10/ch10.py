'''
def countdown(n):
        print(n)
        countdown(n-1)
'''



def countdown(n):
    'counts down to 0'
    if n <= 0:               # base case
        print('Blastoff!!!')
    else:                    # n > 0: recursive step 
        print(n)                 # print n first and then
        countdown(n-1)           # count down from n-1



def vertical(n):
    'prints digits of n vertically'
    if n <10:           # base case: n has 1 digit
        print(n)            # just print n
    else:               # recursive step: n has 2 or more digits
        vertical(n//10)     # recursively print all but last digit
        print(n%10)         # print last digit of n



def pattern(n):
    'prints the n-th pattern'
    if n == 0:           # base case
        print(0, end=' ')
    else:                # recursive step: n > 0
        pattern(n-1)         # print n-1st pattern
        print(n, end=' ')    # print n
        pattern(n-1)         # print n-1st pattern



from turtle import Screen, Turtle
def koch(n):
    'returns turtle directions for drawing curve Koch(n)'

    if n==0:     # base case
        return 'F'

    tmp = koch(n-1) # recursive step: get directions for Koch(n-1)
                    # use them to construct directions for Koch(n)

    return tmp+'L'+tmp+'R'+tmp+'L'+tmp

def drawKoch(n):
    '''draws nth Koch curve using instructions from function koch()'''

    s = Screen()              # create screen
    t = Turtle()              # create turtle    
    directions = koch(n)      # obtain directions to draw Koch(n)

    for move in directions:   # follow the specified moves
        if move == 'F':
            t.forward(300/3**n)   # forward move length, normalized 
        if move == 'L':
            t.lt(60)              # rotate left 60 degrees
        if move == 'R':
            t.rt(120)             # rotate right 60 degrees
    s.bye()



import os
def scan(pathname, signatures):
    '''recursively scans all files contained, directly or
       indirectly, in the folder pathname'''

    for item in os.listdir(pathname):       # for every file or folder 
                                            # in folder pathname 
        # create pathname for item called next
        # next = pathname + '/' + item	    # Mac only
        # next = pathname + '\' + item	    # Windows only
        next = os.path.join(pathname, item) # any OS

        try: # blindly recurse on next
            scan(next, signatures)
        except: # base case: exception means that item is a file
            # for every virus signature
            for virus in signatures:

                # check if file next has the virus signature
                if open(next).read().find(signatures[virus]) >= 0:
                    print('{}, found virus {}'.format(next,virus))



def power(a,n):
    'returns a to the n-th power'
    res = 1
    for i in range(n):
        res *= a
    return res



def rpower(a,n):
    'returns a to the n-th power'
    if n==0:               # base case: n == 0
        return 1

    tmp = rpower(a,n//2)   # recursive step: n > 0

    if n%2 == 0:
        return tmp*tmp         # a**n = a**(n//2) * a**a(n//2)
    else: # n%2==1
        return a*tmp*tmp       # a**n = a**(n//2) * a**a(n//2) * a



'''
def rpower(a,n):
    'returns a to the n-th power'
    global counter
    if n==0:
        return 1
    tmp = rpower(a,n//2)
    if n%2 == 0:
        counter += 1
        return tmp*tmp
    else: # n%2==1
        counter += 2
        return a*tmp*tmp
'''



def rfib(n):
    'returns n-th Fibonacci number'
    if n < 2:                     # base case
        return 1
    return rfib(n-1) + rfib(n-2)  # recursive step



def fib(n):
    'returns n-th Fibonacci number'
    previous = 1     # 0th Fibonacci number
    current = 1      # 1st Fibonacci number
    i = 1            # index of current Fibonacci number

    while i < n:     # while current is not nth Fibonacci number
        previous, current = current, previous+current
        i += 1

    return current



import time
def timing(func, n):
    'runs func on input returned by buildInput'
    funcInput = buildInput(n)  # obtain input for func 

    start = time.time()        # take start time
    func(funcInput)            # run func on funcInput
    end = time.time()          # take end time

    return end - start         # return execution time


# buildInput for run-time testing of Fibonacci functions
def buildInput(n):
    'returns input for Fibonacci functions'
    return n

import random
'''
# buildInput for comparing Linear and Binary search
def buildInput(n):
    'returns a random sample of n numbers in range [0, 2n)'
    lst = random.sample(range(2*n), n)
    lst.sort()
    return lst
'''

'''
# buildInput for Practice Problems 10.7, 10.8
def buildInput(n):
    'returns a list of n random integers in range [0, n**2)'
    res = []
    for i in range(n):
        res.append(random.choice(range(n**2)))
    return res
'''

def timingAnalysis(func, start, stop, inc, runs):
    '''prints average run-times of function func on inputs of
       size start, start+inc, start+2*inc, ..., up to stop'''

    for n in range(start, stop, inc):  # for every input size n
        acc=0.0                        # initialize accumulator

        for i in range(runs):       # repeat runs times:
            acc += timing(func, n)      # run func on input of size n
                                        # and accumulate run-times
        # print average run times for input size n
        formatStr = 'Run-time of {}({}) is {:.7f} seconds.'
        print(formatStr.format(func.__name__,n,acc/runs))



def search(lst, target, i, j):
    '''attempts to find target in sorted sublist lst[i:j];
       index of target is returned if found, -1 otherwise'''
    if i == j:                       # base case: empty list
        return -1                    # target cannot be in list

    mid = (i+j)//2                   # index of median of l[i:j]

    if lst[mid] == target:           # target is the median     
        return mid
    if target < lst[mid]:            # search left of median
        return search(lst, target, i, mid)
    else:                            # search right of median
        return search(lst, target, mid+1, j)



def binary(lst):
    'chooses item in list lst at random and runs search() on it'
    target = random.choice(lst)
    return search(lst, target, 0, len(lst))



def linear(lst):
    'choose item in list lst at random and runs index() on it'
    target = random.choice(lst)
    return lst.index(target)



def dup1(lst):
    'returns True if list lst has duplicates, False otherwise'
    for item in lst:
        if lst.count(item) > 1:
            return True
    return False



def dup2(lst):
    'returns True if list lst has duplicates, False otherwise'
    lst.sort()
    for index in range(1, len(lst)):
        if lst[index] == lst[index-1]:
            return True
    return False



def dup3(lst):
    'returns True if list lst has duplicates, False otherwise'
    s = set()
    for item in lst:
        if item in s:
            return False
        else:
            s.add(item)
    return True



def dup4(lst):
    'returns True if list lst has duplicates, False otherwise'
    return len(lst) != len(set(lst))



def kthsmallest(lst,k):
    'returns k-th smallest item in lst'
    lst.sort()
    return lst[k-1]



def frequent(lst):
    '''returns most frequently occurring item
       in non-empty list lst'''
    lst.sort()                 # first sort list

    currentLen = 1             # length of current sequence
    longestLen = 1             # length of longest sequence
    mostFreq   = lst[0]        # item with longest sequence

    for i in range(1, len(lst)):
        # compare current item with previous
        if lst[i] == lst[i-1]: # if equal
            # current sequence continues
            currentLen+=1
        else:                  # if not equal
            # update longest sequence if necessary
            if currentLen > longestLen: # if sequence that ended
                                        # is longest so far 
                longestLen = currentLen # store its length 
                mostFreq   = lst[i-1]   # and the item 
            # new sequence starts
            currentLen = 1
    return mostFreq



##################################
# Solutions to Practice Problems #
##################################



def reverse(n):
    'prints digits of n vertically starting with low-order digit'
    if n <10:          # base case: one digit number
        print(n)
    else:              # n has at least 2 digits
       print(n%10)     # prints last digit of n
       reverse(n//10)  # recursively print in reverse all but
                       # the last digit



def cheers(n):
    if n == 0:
        print('Hurray!!!')
    else: # n > 0
        print('Hip', end=' ')
        cheers(n-1)



def factorial(n):
    'returns the factorial of integer n'
    if n in [0, 1]: # base case
        return 1
    return factorial(n-1)*n # recursive step when n > 1



def pattern2(n):
    'prints the n-th pattern'
    if n > 0:
        pattern2(n-1)  # prints pattern2(n-1)
        print(n * '*') # print n stars
        pattern2(n-1)  # prints pattern2(n-1)



def drawSnowflake(n):
    'draws n-th snowflake curve using function koch() 3 times'    
    s = Screen()
    t = Turtle()
    directions = koch(n)
    for i in range(3):
        for move in directions: # draw koch(n)
            if move == 'F':
                t.fd(300/3**n)
            if move == 'L':
                t.lt(60)
            if move == 'R':
                t.rt(120)
        t.rt(120)               # turn right 120 degrees
    s.bye()

