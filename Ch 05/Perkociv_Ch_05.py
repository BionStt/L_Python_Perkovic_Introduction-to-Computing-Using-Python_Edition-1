__author__ = 'Rolando'
#############################################
### Perkovic Intro to Python              ###
#### CH 5: Execution  Control Structures ####
##### PG 133 CH 5                       #####
#############################################


def tempurature(t):
    """ Prints message based on temperature value t

    """
    if t > 86:
        end = 'It is hot!'
    elif t > 32:
        end = 'It is cool.'
    else:
        end = 'It is freezing!'
    return end
print(tempurature(87))
print(tempurature(86))
print(tempurature(32))

###########
### 5.1 ###
###########
print('\nPP 5.1')


def mybmi(weight, height):
    """ Prints bmi report.

    """
    bmi = weight * 703 / (height**2)
    if bmi < 18.5:
        end = 'Underweight'
    elif bmi < 25:
        end = 'Normal'
    else:
        end = 'Overweight'
    return end
print(mybmi(190, 75))
print(mybmi(140, 75))

###########
### 5.2 ###
###########
print('\nPP 5.2')


def powers(n):
    """ Prints all powers from 1 to 2**n.

    """
    for i in range(1, n + 1):
        print(2**i, end=' ')
print(powers(6))


def sorted1(lst):
    """ Returns True if sequence lst is increasing False otherwise

    """
    for i in range(0, len(lst) - 1):  # i = 0, 1, 2, ..., len(lst)-2
        if lst[i] > lst[i + 1]:
            return False
    return True

###########
### 5.3 ###
###########
print('\nPP 5.3')


def arithmetic(lst):
    """ Takes a list of integers as inputs and returns True if they form and arithmetic sequence (if difference between
        digits is the same).
    """
    if len(lst) < 2:
        return True
    diff = lst[1] - lst[0]
    for i in range(1, len(lst) - 1):
        if lst[i + 1] - lst[i] != diff:
            return False
    return True
print(arithmetic([3, 6, 9, 12, 15]))
print(arithmetic([3, 6, 9, 11, 14]))
print(arithmetic([3]))

###########
### 5.4 ###
###########
print('\nPP 5.4')


def factorial(n):
    """ Takes integer and returns its factorial

    """
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact
print(factorial(0))
print(factorial(3))
print(factorial(5))

###########
### 5.5 ###
###########
print('\nPP 5.5')


def acronym(phrase):
    """ Returns acronym made with first character of each word in phrase capitalized

    """
    words = phrase.split()
    acro = ''
    for i in words:
        acro += i[0]
    acrocaps = acro.upper()
    return acrocaps

print(acronym('Random access memory'))
print(acronym('central processing unit'))

###########
### 5.6 ###
###########
print('\nPP 5.6')


def divisors(n):
    """ Returns list of all positive divisors of n

    """
    divlist = []
    for i in range(1, n + 1):
        if n % i == 0:
            divlist.append(i)
    return divlist
print(divisors(6))


def nested(n):
    """ Prints n lines, each containing value 0, 1, 2 ... n - 1

    """
    for i in range(n):          # Repeat n times
        for j in range(n):      # Print 0, 1, ..., n-1
            print(j, end=' ')
        print()                 # Move cursor to next line
print(nested(5))
###########
### 5.7 ###
###########
print('\nPP 5.7')


def xmult(l1, l2):
    """ Takes two lists of integers and returns list containing all the products
        of integers from the first list with the integers from the second.
    """
    x1 = []
    for i in l1:                # Repeat for each # in l1
        for j in l2:            # and l2
            x1.append(j * i)    # Add each product in order to list
    return x1
print(xmult([2], [1, 5]))
print(xmult([2, 3], [1, 5]))
print(xmult([3, 4, 1], [2, 0]))


def nested2(n):
    """ Prints n lines, each containing value 0 / 0 1 / 0 1 2 / ... 0 1 2 3 ... n - 1

    """
    for i in range(n):          # j = 0, 1, ..., n - 1
        for j in range(i + 1):  # Print 0 1 2 ... j
            print(j, end=' ')
        print()                 # Move cursor to next line
print(nested2(5))

###########
### 5.8 ###
###########
print('\nPP 5.8')


def bubblesort(lst):
    """ Sort lst in ascending order

    """
    for i in range(len(lst) - 1, 0, -1):
        for j in range(i):                                # Pass that ends at i < len(lst)-1, len(lst)-2, ..., 1
            if lst[j] > lst[j + 1]:                       # Compare items at index j and j+1 for every j = 0, 1, ... i-1
                lst[j], lst[j + 1], = lst[j + 1], lst[j]  # Swap numbers at index j and j + 1
    return lst
print(bubblesort([3, 1, 7, 4, 9, 2, 5]))


def print2d(t):
    """ Prints values in 2D list t as 2D table

    """
    for row in t:
        for item in row:
            print(item, end=' ')    # Print item followed by a blank space
        print()                     # Move to next line
t1 = [[4, 7, 2, 5], [5, 1, 9, 2], [8, 3, 6, 9]]
s1 = [[0, 1, 2, 0], [0, 1, 1, 1], [0, 1, 0, 0]]
print(print2d(t1))


def incr2d(t):
    """ Increments each number in 2D list f numbers t

    """
    nrows = len(t)
    ncols = len(t[0])

    for i in range(nrows):
        for j in range(ncols):
            t[i][j] += 1
    return t
print(incr2d(t1))


###########
### 5.9 ###
###########

print('\nPP 5.9')


def add2d(t, s):
    """

    """
    nrows = len(t)
    ncols = len(t[0])

    for i in range(nrows):
        for j in range(ncols):
            t[i][j] += s[i][j]
    return t
print(add2d(t1, s1))

############
### 5.10 ###
############

print('\nPP 5.10')


def interest(n):
    """ Takes yearly interest rate and returns hwo long it would take for value to double in years

    """
    balance = 100
    years = 0
    while balance < 200:
        balance += balance * n
        years += 1
    return years
print(interest(0.07))


def fibonacci(bound):
    """ Refers to the smallest Fibonacci number greater than bound

    """
    previous = 1                # First Fibonacci number
    current = 1                 # Second Fibonacci number
    while current <= bound:     # Current becomes previous, and new is computed
        previous, current = current, previous + current
    return current
print(fibonacci(88))

############
### 5.11 ###
############
print('\nPP 5.11')


def approxe(error):
    """ Returns approximation of E within error
    """
    prev = 1                                # approximation 0
    current = 2                             # approximation 1
    i = 2                                   # index of approximation 2
    while current - prev > error:           # while difference between current and previous i larger than error
        prev = current                      # current approximation becomes previous
        current = prev + 1 / factorial(i)   # compute new approximation based on index i
        i += 1                              # index of next approximation
    return current
print(approxe(0.01))
print(approxe(0.000000001))


def hello2():
    """ A greeting service; it repeatedly requests the name of the user and then greets the user

    """
    while True:
        name = input('What is your name? ')
        print('Hello {}'.format(name))
#print(hello2())


def cities():
    """ Returns the list of cities that are interactively entered by the user;
        the empty string ends the interactive input
    """
    lst = []
    city = input('Enter city: ')        # Ask user to enter first entry
    while city != '':                   # If city is not the flag
        lst.append(city)                # Append city to list
        city = input('Enter city: ')    # And ask user once again

    return lst
#print(cities())


def cities2():
    """ Returns the list of cities that are interactively entered by the user;
        the empty string ends the interactive input
    """
    lst = []
    while True:
        city = input('Enter city: ')
        if city == '':
            return lst
        lst.append(city)
#print(cities2())


def print2d2(table):
    """ Prints values in 2D list of numbers as a table

    """
    for row in table:
        for num in row:
            print(num, end=' ')
        print()
t2 = [[2, 3, 0, 6], [0, 3, 4, 5], [4, 5, 6, 0]]
print(print2d2(t2))


def before0(table):
    """ Prints values in 2D list of numbers t as a 2D table;
        only values in row up to first 0 are printed
    """
    for row in table:
        for num in row:             # Inner loop
            if num == 0:            # if num is 0
                break               # Terminate inner loop
            print(num, end=' ')     # Otherwise print num
        print()                     # Move cursor to next line
print(before0(t2))


def ignore0(table):
    """ Prints values in 2D list of numbers t as 2d table;
        0 values are not printed
    """
    for row in table:
        for num in row:             # Inner loop
            if num == 0:            # If num is 0, terminate
                continue            # Current inner loop iteration
            print(num, end=' ')     # Otherwise print num
        print()
print(ignore0(t2))

############
### 5.12 ###
############
print('\nPP 5.12')


def test(n):
    """ Takes integer and returns whether Positive, Negative, or Zero

    """
    result = ''
    if n < 0:
        result += 'Negative'
    elif n == 0:
        result += 'Zero'
    elif n > 0:
        result += 'Positive'
    return result
print(test(-3))
print(test(0))
print(test(3))

###########################################
### 5.13 doesnt ask for code, only text ###
###########################################
print('\nPP 5.13')

''' REFERENCE

    LOOP PATTERNS
    Iteration Loop : Iterating through an explicit sequence of values and performing some action on value
    Counter Loop : Iterating loop controlled with variable (I.E. range)
    Accumulator Loop : Accumulates values with each Iteration of loop
    Nested Loop : A loop inside a loop
    Sequence Loop : A sequence of objects are generated until a condition is satisfied
    Infinite Loop : A loop that runs forever
    Loop and a Half : When a loop has ended midway die to a condition

    ITERATION CONTROL
    break : current loop iteration is stopped, and loop is exited
    continue : current loop iteration is stopped, but loop continues with next iteration
    pass : used as placeholder for empty body in a function or statement
'''
# 14
'''For Iteration'''
# 15
'''For Iteration'''
# 16
'''For Accumulator'''
# 17
'''For Counter'''
# 18
'''For Counter Accumulator'''
# 19
'''For Nested'''
# 20
'''For Nested Accumulator'''
# 21

# 22

############
### 5.14 ###
############
print('\nPP 5.14')


def mult3(lst):
    """ Takes a list of integers and prints only multiples of 3, one per line

    """
    for i in lst:
        if i % 3 == 0:
            print(i)
print(mult3([3, 1, 6, 2, 3, 9, 7, 9, 5, 4, 5]))

############
### 5.15 ###
############
print('\nPP 5.15')


def vowels(s):
    vowel = 'aeiouAEIOU'
    for i in s:
        if i in vowel:
            print(s.find(i))
print(vowels('Hello WORLD'))

#############
### 5.16 ###
#############
print('\nPP 5.16')


def indexes(word, s):
    """ Takes a a string and a character letter and returns a list of indexes at which the letter occurs

    """
    result = []
    count = -1
    for i in word:
        count += 1
        if i == s:
            result.append(count)
    return result
print(indexes('mississippi', 's'))
print(indexes('mississippi', 'i'))
print(indexes('mississippi', 'a'))

############
### 5.17 ###
############
print('\nPP 5.17')


def doubles(lst):
    """ Takes list of integers and outputs list of integers in the last that are exactly
        twice the previous integer in the list, one per line
    """
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1] * 2:
            print(lst[i], end='\n')
print(doubles([3, 0, 1, 2, 3, 6, 2, 4, 5, 6, 5]))

############
### 5.18 ###
############
print('\nPP 5,18')


def four_letter(lst):
    """ Takes a  list of words and  returns the sub-list of all four letter words in the list

    """
    result = []
    for i in range(len(lst)):
        if len(lst[i]) == 4:
            result.append(lst[i])
    return result
print(four_letter(['dog', 'letter', 'stop', 'door', 'bus', 'dust']))

############
### 5.19 ###
############
print('\nPP 5.19')


def inboth(lst1, lst2):
    """ Takes two lists and returns True if there is an item that is common to both lists and False otherwise

    """
    for i in lst1:
        for j in lst2:
            if i == j:
                return True
        return False
t3 = [3, 2, 5, 4, 7]
s2 = [9, 0, 1, 3]
s3 = [100, 919, 412]
print(inboth(t3, s2))
print(inboth(t3, s3))

############
### 5.20 ###
############
print('\nPP 5.20')


def intersect(lst1, lst2):
    """ Takes two lists, each containing no duplicate values, and returns a list containing values that are present
        in both lists
    """
    result = []
    for i in lst1:
        for j in lst2:
            if i == j:
                result.append(i)
    return result
t4 = [3, 5, 1, 7, 9]
s4 = [4, 2, 6, 3, 9]
print(intersect(t4, s4))

############
### 5.21 ###
############
print('\nPP 5.21')


def pair(lst1, lst2, n):
    """ Takes two lists of integers and one integer n and prints the pairs of integers, one from the input list
        and the other from the second input list, that add up to n. Each pair should be printed
    """
    for i in lst1:
        for j in lst2:
            if i + j == n:
                print('{} {}'.format(i, j))
print(pair([2, 3, 4], [5, 7, 9, 12], 9))

############
### 5.22 ###
############
print('\nPP 5.22')


def pairsum(lst, n):
    """ Takes as input a list of distinct integers lst and integer n, and prints the indexes of all pairs of values in
        lst that sum up to n
    """
    for i in range(len(lst)):
        for j in range(i):
            if lst[i] + lst[j] == n:
                print('{} {}'.format(j, i))
print(pairsum([7, 8, 5, 3, 4, 6], 11))

############
### 5.23 ###
############
print('\nPP 5.23')


def pay(wage, hours):
    """ Takes input hourly wage and number of hours an employee worked in the last week. Function computes and returns
        employee's pay. Overtime work should be paid this way:Any hours beyond 40 but less than 60 should be paid at 1.5
        times the regular hourly wage. Any hours beyond 60 should be paid at 2 times the regular
        hourly wage.
    """
    if hours < 40:
        return wage * hours
    elif hours < 60:
        return (wage * 40) + (hours - 40) * wage * 1.5
    else:
        return (wage * 40) + (20 * wage * 1.5) + ((hours - 60) * wage * 2)
print(pay(10, 35))
print(pay(10, 45))
print(pay(10, 61))

############
### 5.24 ###
############
print('\nPP 5.24')


def case(word):
    """  Takes string as input and returns 'capitalized', 'not capitalized', or 'unknown', depending on whether the
         string starts with an uppercase letter, lowercase letter, or something other than a letting in the English
         alphabet, respectively.
    """
    result = ''
    if word[0] in 'abcdefghijklmnopqrstuvwxyz':
        result += 'Not Capitalized'
    elif word[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        result += 'Capitalized'
    else:
        result += 'Unknown'
    return result
print(case('Android'))
print(case('android'))
print(case('3M'))

############
### 5.25 ###
############
print('\nPP 5.25')


def leap(year):
    """ Takes a year as input and returns True if the year is a leap year and false otherwise.
        (A leap year is divisible by 4, but not by 100, unless it is divisible by 400.
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
print(leap(2008))
print(leap(1900))
print(leap(2000))

############
### 5.26 ###
############
print('\nPP 5.26')


def rps(p1, p2):
    """ Takes the choice of player 1 and the choice of player 2 ('R', 'P', or 'S')
        and returns -1 if player 1 wins, 1 if player 2 wins, or 0 if there is a tie.
    """
    if p1 == p2:
        return 0
    elif p1 == 'R' and p2 == 'S' or p1 == 'S' and p2 == 'P' or p1 == 'P' and p2 == 'R':
        return -1
    else:
        return 1
print(rps('R', 'P'))
print(rps('R', 'S'))
print(rps('S', 'S'))

############
### 5.27 ###
############
print('\nPP 5.27')


def letter2number(grade):
    """ Takes a letter grade (A, B, C, D, F, with + or -) and returns corresponding number grade. The numeric values
        for A, B, C, D, and F are 4, 3, 2, 1, 0, a + increases number grade value by 0.3 and a - decreases it by 0.3
    """
    if grade == 'A':
        return 4.0
    elif grade == 'A-':
        return 3.7
    elif grade == 'B+':
        return 3.3
    elif grade == 'B':
        return 3.0
    elif grade == 'B-':
        return 2.7
    elif grade == 'C+':
        return 2.3
    elif grade == 'C':
        return 2.0
    elif grade == 'C-':
        return 1.7
    elif grade == 'D':
        return 1.0
    else:
        return 0

print(letter2number('A'))
print(letter2number('B+'))
print(letter2number('F'))

############
### 5.28 ###
############
print('\n5.28')


def geometric(lst):
    """ Takes a list of integers and returns True if the integers in the list form a geometric sequence.

    """
    if len(lst) < 2:
        return True
    for i in range(len(lst) - 2):
        if lst[i + 1] / lst[i] != lst[i + 2] / lst[i + 1]:
            return False
    return True
print(geometric([2, 4, 8, 16, 32, 64, 128, 256]))
print(geometric([2, 4, 6, 8]))

############
### 5.29 ###
############
print('\nPP 2.29')


def lastfirst(lst):
    """ Takes a list of strings of the format <LastName, FirstName> and returns a list consisting two lists
    a : all the first names
    b : all the last names
    """
    listsplit = []
    first = []
    last = []
    for i in lst:
        i = i.split(', ')
        listsplit.append(i)
    print(listsplit)
    for i in listsplit:
        first.append(i[1])
        last.append(i[0])
    return [first, last]
print(lastfirst(['Gerber, Len', 'Fox, Kate', 'Dunn, Bob']))

############
### 5.30 ###
############
print('\nPP 5.30')


def many(file):
    """ Takes name of file in current directory (as a string) and outputs the number of words of length 1, 2, 3, and 4.

    """
    infile = open(file, 'r')
    content = infile.read()
    infile.close()

    table = str.maketrans('!,.:;?', 6 * ' ')
    content = content.translate(table)
    wordlist = content.split()

    word1 = 0
    word2 = 0
    word3 = 0
    word4 = 0
    for i in wordlist:
        if len(i) == 1:
            word1 += 1
        elif len(i) == 2:
            word2 += 1
        elif len(i) == 3:
            word3 += 1
        elif len(i) == 4:
            word4 += 1

    str_format = 'Words of length 1 : {}\nWords of length 2 : {}\nWords of length 3 : {}\nWords of length 4 : {}'
    result = str_format.format(word1, word2, word3, word4)
    return result
print(many('sample.txt'))

############
### 5.31 ###
############
print('\nPP 5.31')


def subsetsum(lst, n):
    """ Takes a list of positive numbers and a positive integer target. Your function should return True if there are
        three numbers in that list that add up tp target.
    """
    w = 0
    for i in range(len(lst)):
        for j in range(i):
            if lst[i] + lst[j] <= n:
                w += lst[i] + lst[j]
                for k in range(i):
                    if k + w == n:
                        return True
    return False
print(subsetsum([5, 4, 10, 20, 15, 19], 38))
print(subsetsum([5, 4, 10, 20, 15, 19], 10))

############
### 5.32 ###
############
print('\nPP 5.32')


def fib(n):
    """ Takes n and returns the nth fibonacci number

    """
    previous = 1
    current = 1
    for i in range(n - 1):
        previous, current = current, previous + current
    return current
print(fib(0))
print(fib(4))
print(fib(8))

############
### 5.33 ###
############
print('\nPP 5.33')


def mystery(n):
    """ Takes a positive integer n and answers this question: How many times can n be halved (using integer division,
        before reaching 1? That value is returned
    """
    count = 0
    while n / 2 >= 1:
        n /= 2
        count += 1
    return count
print(mystery(4))
print(mystery(11))
print(mystery(25))

############
### 5.34 ###
############
print('\nPP 5.34')


def statement(lst):
    """ Takes a list of floating-point numbers, with  positive numbers representing deposits and negative numbers
        representing withdrawals from a bank account. Function returns a list of two floats; first is sum of deposits,
        (positive) second is sum of withdrawals (negative).
    """
    w = 0
    d = 0
    for i in lst:
        if i > 0:
            w += i
        else:
            d += i
    return [w, d]
print(statement([30.95, -15.67, 45.56, -55.00, 43.78]))

############
### 5.35 ###
############
print('\nPP 5.35')


def pixels(lst):
    """ Takes as input a 2D list of non-negative integer entries (representing the values of pixels in an image) and
        returns the number of entries that are positive (i.e. number of pixels that are not dark). Your function should
        word on 2D lists of any size
    """
    count = 0
    for i in lst:
        for j in i:
            if j > 0:
                count += 1
    return count
print(pixels([[0, 156, 0, 0], [34, 0, 0, 0], [23, 123, 0, 34]]))
print(pixels([[123, 56, 255], [34, 0, 0], [23, 123, 0], [3, 0, 0]]))

############
### 5.36 ###
############
print('\nPP 5.36')


def prime(n):
    """ Takes a positive integer n as input and returns True if it is a prime number and false otherwise.

    """
    for i in range(2, n - 1):
        if n % i == 0 and n > 1:
            return False
    return True
print(prime(2))
print(prime(17))
print(prime(21))

############
### 5.37 ###
############
print('\nPP 5.37')


def mssl(lst):
    """ Takes a list of integers, then computes and returns sum of the maximum sum sub-list of the input list.
        The maximum sum sub-list is a sub-list (slice) of input list whose sum of entries is largest.
    """
    best = 0
    current = 0
    for i in lst:
        current = max(current + i, 0)
        best = max(best, current)
    return best
print(mssl([4, -2, -8, 5, -2, 7, 7, 2, -6, 5]))
print(mssl([3, 4, 5]))
print(mssl([-3, -4, -5]))

############
### 5.38 ###
############
print('\nPP 5.38')


def collatz(x):
    """ Takes positive integer x as input and prints the Collatz sequence starting at x. A Collatz sequence is obtained
        by repeatedly apply this rule to the previous number x in the sequence:
        x = x / 2 (if even)
        x = 3x + 1 (if odd)
        The function stops when the sequence gets to number 1.
    """
    while x != 1:
        print(x)
        if x % 2 == 0:
            x /= 2
        else:
            x = 3 * x + 1
    return 1
print(collatz(10))
print(collatz(20))

############
### 5.39 ###
############
print('\nPP 5.39')


def exclamation(s):
    """ Takes a string and returns it with this mod: Every vowel is replaced by four consecutive copies of itself and
        an exclamation mark is added to the end.
    """
    y = 0
    vowel = 'aeiouAEIOU'
    for i in s:
        if i in vowel:
            s = s.replace(i, i * 4)
            y += 1
    if y > 0:
        s += '!'
    return s
print(exclamation('argh'))
print(exclamation('hello'))

############
### 5.40 ###
############
print('\nPP 5.40')


def approxpi(error):
    """ Takes error and approximates pi within error by computing the preceding sum, term by term, until a difference
        between the current sum and the previous sum is no greater than error.
        pi =
    """
    prev = 4                                        # Term 0
    current = 4 - (4 / 3)                           # Term 1
    n = 2                                           # Term index 2
    while abs(prev - current) > error:              # While diff between Current and prev is larger than error
        prev = current                              # Current replace prev
        current += (4 / (2.0 * n + 1) * (-1) ** n)  # Calculate new Current
        n += 1
    return current
print(approxpi(0.01))
#print(approxpi(0.000001))

############
### 5.41 ###
############
print('\nPP 5.41')


def poly(lst, x):
    """ Hi

    """
    current = lst[0] + lst[1] * x + lst[2] * x ** 2
    n = 3
    for i in range(len(lst) - 3):
        current += (lst[n] * x ** n)
        n += 1
    return current
print(poly([1, 2, 1], 2))
print(poly([1, 0, 1, 0, 1], 2))
print(poly([1, 0, 1, 0, 1], 3))

############
### 5.42 ###
############
print('\nPP 5.42')


def primefac(n):
    """ Takes as input a positive integer n and returns a list containing all the numbers in the prime factorization of
         n. (The prime factorization of a positive integer n is the unique list of prime numbers whose product is n.)
    """
    primes = []
    i = 2
    while i * i <= n:
        while (n % i) == 0:
            primes.append(i)
            n /= i
        i += 1
    if n > 1:
        primes.append(n)
    return primes

print(primefac(5))
print(primefac(72))

############
### 5.43 ###
############
print('\nPP 5.43')


def evenrow(table):
    """ Takes a 2D list of integers and returns true if each row of tables sums up to an even number, False otherwise

    """
    for i in table:
        lst = []
        for j in i:
            lst.append(j)
        if sum(lst) % 2 != 0:
            return False
    return True
print(evenrow([[1, 3], [2, 4], [0, 6]]))
print(evenrow([[1, 3], [3, 4], [0, 5]]))
print(evenrow([[1, 3, 2], [3, 4, 7], [0, 6, 2]]))
print(evenrow([[1, 3, 2], [3, 4, 7], [0, 5, 2]]))

############
### 5.44 ###
############
print('\nPP 5.44')


def cipher(key, s):
    """ Encrypts string s with key
    """
    if len(key) != 10:
        return 'Key is not 10 characters long'
    table = str.maketrans('0123456789', key)
    s = s.translate(table)
    return s
print(cipher('3941068257', '132'))
print(cipher('3941068257', '111'))

############
### 5.45 ###
############
print('\nPP 5.45')


def avavg(table):
    """ Takes a list whose items are lists of three numbers. Each three-number list represents the three grades
        a particular student received for a course. Function should print two lines. THe first line contains a list
        containing every student's average grade. The second line will contain just one number: the average class grade,
        defined as the average of all student grades.
    """
    student_avg = []
    for i in table:
        student_avg.append(sum(i) / len(i))
    print(student_avg)
    return sum(student_avg) / len(student_avg)

print(avavg([[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]]))

############
### 5.46 ###
############
print('\nPP 5.46')


def inversions(s):
    """ Takes a string of upper case letters and returns the amount of inversions in the string

    """
    count = 0
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if s[i] > s[j]:
                count += 1
    return count
print(inversions('ABBFHDL'))
print(inversions('ABCD'))
print(inversions('DCBA'))

############
### 5.47 ###
############
print('\nPP 5.47')


def d2x(n, x):
    """ Takes a non-negative integer (n) and an integer (x) and returns a string of digits that
        represents the base-x representation of n
    """
    s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    places = 0
    result = ''
    while n - x ** places > 0:
        places += 1
    places -= 1
    while places > -1:
        result += (s[n // (x ** places)])
        n -= (n // x ** places) * x ** places
        places -= 1
    return result
print(d2x(10, 2))
print(d2x(10, 3))
print(d2x(10, 8))
print(d2x(231, 16))

############
### 5.48 ###
############
print('\nPP 5.48')


def sublist(lst1, lst2):
    """
    :param lst1: List 1
    :param lst2: List 2
    :return: T/F : True if List 1 is sub-list of lst 2; False otherwise
    """
    prev = 0
    current = 0
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if lst1[i] == lst2[j]:
                current = j
        if current <= prev:
            return False
        prev = current
    return True
print(sublist([15, 1, 100], [20, 15, 30, 50, 1, 100]))
print(sublist([15, 50, 20], [20, 15, 30, 50, 1, 100]))

############
### 5.49 ###
############
print('\nPP 5.49')


def heron(n, error):
    """
    :param n:
    :param error:
    :return: sqrt of n within error
    """
    prev = 1.0
    current = 1 / 2 * (prev + n / prev)
    while abs(current - prev) >= error:
        prev = current
        current = (1/2 * (prev + n / prev))
    return current
print(heron(4.0, 0.5))
print(heron(4.0, 0.1))