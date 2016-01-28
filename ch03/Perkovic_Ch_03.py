__author__ = 'Rolando'
#######################################
### Perkovic Intro to Python        ###
#### CH 3: Imperative Programming  ####
##### PG 54 CH 3                  #####
#######################################


''' NOTES
    print() == prints object
    input() == prints and asks for input
    eval() == inputs are treated as strings, use eval to evaluate expressions (math, lsts, etc) in inputs
    FORMAT
    eval(input())
    print(eval())
'''
###########
### 3.1 ###
###########
print('\nPP 3.1')
''' Reference
    c = 5/9 * (f - 32)
'''
f = eval(input('Enter the temperature in degrees Fahrenheit: '))    # Asks for temp in Fahrenheit
c = (f - 32) * 5 / 9                                                # Converts Fahrenheit into Celsius
print('The temperature in degrees Celsius is: ', c)

###########
### 3.2 ###
###########
print('\nPP 3.2')

# A
age = eval(input('Please enter your age: '))    # Asks for age
if age > 62:                                    # If age is greater than 62, 'You can get your pension benefits'
    print('You can get your pension benefits')

# B
bbgreats = ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth']
bbplayer = input('Name a baseball player: ')

if bbplayer in bbgreats:                                # If bbplayer in bbgreats, print
    print('One of the top 5 baseball players, ever!')   # If bbplayer in bbgreats, print

# C
hits = eval(input('How many hits did you take: '))
shield = eval(input('What is your shield: '))

if hits > 10 and shield == 0:   # If hits is greater than 10 and shield is 0. print 'You are dead...'
    print('You are dead...')

# D
direction = input('What is you Cardinal direction: ')

if direction is 'north' or 'south' or 'east' or 'west':
    print('I can escape!')  # If at least one of the Boolean variables north, south, east, and west is True, print
# 'I can escape.'

###########
### 3.3 ###
###########
print('\nPP 3.3')

# A
year = eval(input('What year is it: '))   # Asks for year

if year % 4 == 0:
        print('Could be a leap year.')    # If year is divisible by 4, print 'Could be a leap year.';
else:
    print('Definitely not a leap year.')  # otherwise, print 'Definitely not a leap year.'

# B
ticket = [1, 2, 3]
lottery = [1, 2, 4]

if ticket == lottery:
    print('You won!')                # If list ticket is equal to list lottery, print 'You, won!';
else:
    print('Better luck next time')   # else print 'Better luck next time...'

###########
### 3.4 ###
###########
print('\nPP 3.4')

users = ['joe', 'sue', 'hani', 'sophie']
ids = input('Login: ')                  # Asks for user ID

if ids in users:
    print('You are in!')                # if ID is valid, prints 'You are in!'
else:
    print('User unknown.')              # else print 'User unknown.'
print('Done.')                          # Either way, print 'Done.'

###########
### 3.5 ###
###########
print('\nPP 3.5')
words = eval(input('Enter word list: '))    # Requests list of words

for i in words:                             # Prints all four-letter strings in list
    if len(i) == 4:
        print(i)

###########
### 3.6 ###
###########
print('\nPP 3.6')

# A
for i in range(10):
    print(i)
# B
for i in range(2):
    print(i)

###########
### 3.7 ###
###########
print('\nPP 3.7')

# A
for i in range(3, 13):
    print(i)
# B
for i in range(0, 9, 2):
    print(i)
# C
for i in range(0, 24, 3):
    print(i)
# D
for i in range(3, 12, 5):
    print(i)

###########
### 3.8 ###
###########
print('\nPP 3.8')


def average(x, y):
    """
    :param x: float 1
    :param y: float 2
    :return:  average of x and y
    """
    return (x + y) / 2

print(average(2, 3.5))

###########
### 3.9 ###
###########
print('\nPP 3.9')


def perimeter(r):
    """
    :param r: radius
    :return:  perimeter
    """
    import math
    return 2 * math.pi * r

print(perimeter(1))

############
### 3.10 ###
############
print('\nPP 3.10')


def negatives(lst1):
    """
    :param lst1: list of numbers
    :return:  negative values in list only
    """
    for j in lst1:
        if j < 0:
            print(j)

print(negatives([4, 0, -1, -3, 6, -9]))

##########################################
##### 3.11 & 3.12 don't ask for code #####
##########################################
print('\nPP 3.11')
print('No Code')
print('\nPP 3.12')
print('No Code')

############
### 3.13 ###
############
print('\nPP 3.13')

team = ['Ava', 'Eleanor', 'Claire', 'Sarah']
print(team)
team[0], team[-1] = team[-1], team[0]           # team with first and last item switched
print(team)

############
### 3.14 ###
############
print('\nPP 3.14')


def swapfl(lst2):
    """
    :param lst2: list
    :print: list with lst[0] swapped with lst[-1]
    """
    lst2[0], lst2[-1] = lst2[-1], lst2[0]
    print(lst2)

ingredients = ['flour', 'sugar', 'butter', 'apples']
print(swapfl(ingredients))
##################################################################
##### 3.15 based on Case study, done in "Perkovic Ch 3 - CS" #####
##################################################################

############
### 3.16 ###
############
print('\nPP 3.16')

'''
    input(eval())
    print(eval())
'''

# A
print(eval('2 * 3 + 1'))
# B
# print(eval('hello'))              Error
# C
print(eval("'hello' + ' ' + 'world!'"))
# D
print(eval("'ASCII'.count('I')"))
# E
# print(eval('x = 5'))              Error

############
### 3.17 ###
############
print('\nPP 3.17')

a, b, c, = 3, 4, 5

# A
if a < b:
    print('OK A')                   # Print 'OK' if statement is true;
else:
    print('NOT OK A')               # otherwise print false
# B
if c < b:
    print('OK B')
else:
    print('NOT OK B')
# C
if a + b == c:
    print('OK C')
else:
    print('NOT OK C')
# D
if a ** 2 + b ** 2 == c ** 2:
    print('OK D')
else:
    print('NOT OK D')
########################
##### 3.18 in 3.17 #####
########################

############
### 3.19 ###
############
print('\nPP 3.19')

lst = ['January', 'February', 'March']
for i in lst:                            # Print first 3 characters (abbreviations) of lst
    print(i[0] + i[1] + i[2])

############
### 3.20 ###
############
print('\nPP 3.20')

lst = [2, 3, 4, 5, 6, 7, 8, 9]
for i in lst:                            # Print numbers whose square is divisible by 8
    if (i ** 2) % 8 == 0:
        print(i)

############
### 3.21 ###
############
print('\nPP  3.21')

# A
for i in range(0, 2):
    print(i)
# B
for i in range(0, 1):
    print(i)
# C
for i in range(3, 7):
    print(i)
# D
for i in range(1, 2):
    print(i)
# E
for i in range(0, 4, 3):
    print(i)
# F
for i in range(5, 22, 4):
    print(i)

############
### 3.22 ###
############
print('\nPP 3.22')

lst = eval(input('Enter a list of words: '))
for i in lst:                       # Requests a list of words
    if i != 'secret':               # prints each word that is not 'secret'
        print(i)

############
### 3.23 ###
############
print('\nPP 3.23')

lst = eval(input('Enter list: '))             # Requests list of names
for i in lst:                                 # Prints names that start with A-M
    if i[0] in 'abcdefghijklmABCDEFGHIJKLM':
        print(i)

############
### 3.24 ###
############
print('\nPP 3.24')

lst = eval(input('Enter a list: '))             # Asks for list
print('The first list element is', lst[0])      # Returns First element on list
print('The last list element is', lst[-1])      # Then last element on list

############
### 3.25 ###
############
print('\nPP 3.25')

n = eval(input('Enter a positive number: '))    # Asks for positive #
for i in range(4):                              # Prints first 4 multiples
    print(eval('i * n'))

############
### 3.26 ###
############
print('\nPP 3.26')

n2 = eval(input('Enter a integer: '))            # Asks for integer
for i in range(n2):                              # Prints squares up to, but not including, n
    print(eval('i ** 2'))

############
### 3.27 ###
############
print('\nPP 3.27')

n3 = eval(input('Enter a positive integer: '))   # Asks for positive integer
for i in (range(n3, 0, -1)):                     # Prints positive divisors of n
    if n3 % i == 0:
        print(i)

############
### 3.28 ###
############
print('\nPP 3.28')

a1 = eval(input('Enter first number: '))         # Asks for 4 numbers
a2 = eval(input('Enter second number: '))
a3 = eval(input('Enter third number: '))
a4 = eval(input('Enter last number: '))
if a4 == (a1 + a2 + a3) / 3:                     # Prints 'Equal' if the average of first 3 numbers equals last number
    print('Equal')

############
### 3.29 ###
############
print('\nPP 3.29')

hc, kc, rc, = 0, 0, 8
xc = eval(input('Enter x: '))                       # Asks for x
yc = eval(input('Enter y: '))                       # Asks for y
if (xc - hc) ** 2 + (yc - hc) ** 2 < rc ** 2:       # Prints if coordinate is in circle with r = 8
    print('It is in!')

############
### 3.30 ###
############
print('\nPP 3.30')

n4 = eval(input('Enter a four digit number: '))   # Asks for a mulit-digit number
for i in range(len(str(n4)) - 1, -1, -1):         # Prints each digit individually
    print((n4 // (10 ** i)) % 10)

############
### 3.31 ###
############
print('\nPP 3.31')


def reverse_string(s):
    """
    :param s: string
    :return:  reversed string
    """
    return s[::-1]

print(reverse_string('dna'))

############
### 3.32 ###
############
print('\nPP 3.32')


def pay(w, t):
    """
    :param w: wages (per hour)
    :param t: time  (per hour)
    :return:  total pay
    """
    if t <= 40:
        return w * t
    else:
        return (w * 40) + ((t - 40) * w * 1.5)

print(pay(10, 10))
print(pay(10, 35))
print(pay(10, 45))

############
### 3.33 ###
############
print('\nPP 3.33')


def prob(n1):
    """
    :param n1: Number of times the coin is flipped
    :return: Probability of getting same result n times
    """
    print(1 / (2 ** n1))

print(prob(1))
print(prob(2))
print(prob(3))


############ xxx
### 3.34 ### xxx
############
print('\nPP 3.34')


# def reverse_int(i1):
#    """
#    :param i1: integer
#    :return:   integer with digits reversed
#    """
#    result = 0
#    for i in range(len(str(i1)) - 1, -1, -1):         # Prints each digit individually
#        result = result + (i1 // (10 ** i))
#    return result

# print(reverse_int(123))

############
### 3.35 ###
############
print('\nPP 3.35')

'''
    REFERENCE
    slope = (y2 - y1) / (x2 - x1)
    distance = math.sqrt((x2 - x1) + (y2 - y1))
'''


def points(x1, y1, x2, y2):
    """
    :param x1: x1
    :param y1: y1
    :param x2: x2
    :param y2: y2
    :return:   The slope is 's' and the distance is 'd'
    """
    import math
    if x1 != x2:
        m = (y2 - y1) / (x2 - x1)
    else:
        m = 'infinity'
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return 'The slope is ' + str(m) + ' and the distance is ' + str(d)

print(points(0, 0, 1, 1))
print(points(0, 0, 0, 1))

############
### 3.36 ###
############
print('\nPP 3.36')


def abbreviation(s1):
    """
    :param s1: String
    :return:   Abbreviation with first two letters of string
    """
    return s1[0] + s1[1]

print(abbreviation('Monday'))
print(abbreviation('Tuesday'))
print(abbreviation('Wedding'))

############
### 3.37 ###
############
print('\nPP 3.37')


def collision(x1, y1, r1, x2, y2, r2):
    """
    :param x1:
    :param y1:
    :param r1:
    :param x2:
    :param y2:
    :param r2:
    :return:    Boolean stating whether or not there was a collision
    """
    import math
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return d <= (r1 + r2)

print(collision(0, 0, 3, 0, 5, 3))
print(collision(0, 0, 1.4, 2, 2, 1.4))

############
### 3.38 ###
############
print('\nPP 3.38')


def partition(l):
    """
    :param l: list
    :return:  List with strings that start with letter A - M
    """
    nl = []
    for s in l:
        if s[0] in 'abcdefghijklmABCDEFGHIJKLM':
            nl.append(s)
    return nl

print(partition(['Eleanor', 'Evelyn', 'Sammy', 'Owen', 'Gavin']))

############
### 3.39 ###
############
print('\nPP 3.39')


def lastf(s3):
    """
    :param s3: String in format 'FirstName LastName'
    :return:   String in format 'LastName, F.'
    """
    nnl = s3.split()
    return nnl[0] + ' ' + nnl[1][0] + '.'
print(lastf('John Locke'))
print(lastf('Albert Camus'))

############
### 3.40 ###
############
print('\nPP 3.40')


def avg(l):
    """
    :param l: list of numbers
    :return:  Average value of list(s)
    """
    for u in l:
        print((sum(u)) / len(u))

print(avg([[95, 92, 86, 87], [66, 54], [89, 72, 100], [33, 0, 0]]))

############
### 3.41 ###
############
print('\nPP 3.41')


def hit(h, k, r, x, y):
    """
    :param h:
    :param k:
    :param r:
    :param x:
    :param y:
    :return:    Boolean stating whether or not point (x, y) is in circle (h, k, r)
    """
    import math
    d = math.sqrt((h - x) ** 2 + (k - y) ** 2)
    return d <= r

print(hit(0, 0, 3, 3, 0))
print(hit(0, 0, 3, 4, 0))

############
### 3.42 ###
############
print('\nPP 3.42')


def ion2e(s):
    """
    :param s: string
    :return:  if word ends in 'tion', change suffix to 'te'; else return original str
    """
    if s[-3:] == 'ion':
        return s[:-3] + 'e'
    else:
        return s
print(ion2e('congratulation'))
print(ion2e('marathon'))

############
### 3.43 ###
############
print('\nPP 3.43')

''' REFERENCE
    Speed Of Sound == 340.29 m / s
    1 KM == 1000 m
    v = d / t
'''


def distance(t):
    """
    :param t: time
    :return:  distance
    """
    v = 340.29
    return v * (t / 1000)

print(distance(3))
print(distance(6))

##################################################################
##### 3.44 based on Case study, done in "Perkovic Ch 3 - CS" #####
##################################################################
