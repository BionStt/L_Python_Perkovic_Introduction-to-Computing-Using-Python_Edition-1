def temperature(t):
    'prints message based on temperature value t'
    if t > 86:
        print('It is hot!')
    elif t > 32:
        print('It is cool.')
    else:                        # t <= 32
        print('It is freezing!')



def sorted(lst):
    'returns True if sequence lst is increasing, False otherwise'
    for i in range(0, len(lst)-1): # i = 0, 1, 2, ..., len(lst)-2
        if lst[i] > lst[i+1]:
            return False
    return True



def nested(n):
    'prints n lines each containing value 0 1 2 ... n-1'
    for j in range(n):          # repeat n times:
        for i in range(n):          # print 0, 1, ..., n-1
            print(i, end=" ")
        print()                # move cursor to next line



def nested2(n):
    'prints n lines 0 1 2 ... j for j = 0, 1, ..., n-1'
    for j in range(n):       # j = 0, 1, ..., n-1
        for i in range(j+1):    # print 0 1 2 ... j
            print(i, end=" ")
        print()                 # move to next line


def print2D(t):
    'prints values in 2D list t as a 2D table'
    for row in t:
        for item in row:         # print item followed by 
            print(item, end=' ')     # a blank space
        print()                  # move to next line


def incr2D(t):
    'increments each number in 2D list of numbers t'
    nrows = len(t)                   # number of rows
    ncols = len(t[0])                # number of columns

    for i in range(nrows):           # i is the row index
        for j in range(ncols):           #j is the column index
            t[i][j] += 1



def fibonacci(bound):
    'returns the smallest Fibonacci number greater than bound'
    previous = 1	# first Fibonacci number
    current = 1	        # second Fibonacci number
    while current <= bound:
        # current becomes previous, and new current is computed
        previous, current = current, previous+current
    return current



def hello2():
    '''a greeting service; it repeatedly requests the name
       of the user and then greets the user'''
    while True:
        name = input('What is your name? ')
        print('Hello {}'.format(name))



def cities():
    '''returns the list of cities that are interactively entered
       by the user; the empty string ends the interactive input'''
    lst = []
    
    city = input('Enter city: ')   # ask user to enter first city

    while city != '':              # if city is not the flag value
        lst.append(city)           # append city to list
        city = input('Enter city: ')   # and ask user once again

    return lst



def cities2():
    '''returns the list of cities that are interactively entered
       by the user; the empty string ends the interactive input'''
    lst = []

    while True:                  # forever repeat:
        city = input('Enter city: ') # ask user to enter city

        if city == '':               # if city is the flag value
            return lst                   # return list

        lst.append(city)             # append city to list



def print2D2(table):
    'prints values in 2D list t as a 2D table'
    for row in table:
        for entry in row:
            print(entry, end=' ')
        print()



def before0(table):
    '''prints values in 2D list of numbers t as a 2D table;
       only values in row up to first 0 are printed'''
    for row in table:

        for num in row:     # inner for loop
            if num == 0:        # if num is 0
                break           # terminate inner for loop
            print(num, end=' ') # otherwise print num

        print()             # move cursor to next line



def ignore0(table):
    '''prints values in 2D list of numbers t as a 2D table;
       0 values are no printed'''
    for row in table:

        for num in row:     # inner for loop
            if num == 0:        # if num is 0, terminate
                continue        # current inner loop iteration
            print(num, end=' ') # otherwise print num

        print()             # move cursor to next line



##################################
# Solutions to Practice Problems #
##################################



def myBMI(weight, height):
  'prints BMI report'
  bmi = weight * 703 / height**2
  if bmi < 18.5:
    print('Underweight')
  elif bmi < 25:
    print('Normal')
  else:                        # bmi >= 25
    print('Overweight')



def powers(n):
    'prints 2**i for i = 1, 2, ..., n'
    for i in range(1, n+1):
        print(2**i)



def arithmetic(lst):
    '''returns True if list lst contains an arithmetic sequence,
       False otherwise'''
    if len(lst) < 2: # a sequence of length < 2 is arithmetic
        return True
   # checking that difference between successive items is equal
   # to the difference between the first two numbers 
    diff = lst[1] - lst[0]
    for i in range(1, len(lst)-1):
        if lst[i+1] - lst[i] != diff:
            return False
    return True



def factorial(n):
    'returns n! for input integer n'
    res = 1
    for i in range(2, n+1):
        res *= i
    return res



def acronym(phrase):
    'returns the acronym of the input string phrase'
    # splits phrase into a list of words
    words = phrase.split()
    # accumulate first character, as an uppercase, of every word
    res = ''
    for w in words:
        res = res + w[0].upper()
    return res



def divisors(n):
    'returns the list of divisors of n'
    res = []
    for i in range(1, n+1):
        if n % i == 0:
            res.append(i)
    return res



def xmult(l1,l2):
    '''returns the list of products of items in list l1
       with items in list l2'''
    l = []
    for i in l1:
        for j in l2:
            l.append(i*j)
    return l



def bubblesort(lst):
    'sorts list lst in nondecreasing order'
    for i in range(len(lst)-1, 0, -1):
        # perform pass that ends at
        # i < len(lst)-1, len(lst)-2, ..., 1
        for j in range(i):
            # compare items at index j and j+1
            # for every j = 0, 1, ..., i-1
            if lst[j] > lst[j+1]:
                # swap numbers at index j and j+1
                lst[j], lst[j+1] = lst[j+1], lst[j]


def add2D(t1, t2):
    '''t1 and t2 are 2D lists with the same number of rows and
       same number of equal sized columns

       add2D increments every item t1[i][j] by t2[i][j]'''
    nrows = len(t1)                # number of rows
    ncols = len(t1[0])             # number of columns
    for i in range(nrows):         # for every row index i
        for j in range(ncols):         # for every column index j
            t1[i][j] += t2[i][j]



def interest(rate):
    '''returns the number of years for investment

      to double for the given rate'''
    amount = 100                 # initial account balance
    count = 0
    while amount < 200:
        # while investment not doubled in value
        count += 1               # add one more year
        amount += amount*rate    # add interest
    return count



def approxE(error):
    'returns approximation of e within error'

    prev = 1                        # approximation 0
    current = 2                     # approximation 1
    i = 2                           # index of next approximation
    while current - prev > error:
        # while difference between current and previous
        # approximation is too large
                                    # current approximation
        prev = current              # becomes previous
                                    # compute new approximation
        current = prev + 1/factorial(i)  # based on index i
        i += 1                      # index of next approximation
    return current

