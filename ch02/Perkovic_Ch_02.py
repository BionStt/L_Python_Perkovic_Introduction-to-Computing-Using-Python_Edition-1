import math
__author__ = 'Rolando'
####################################
### Perkovic Intro to Python     ###
#### CH 2: Python Data types    ####
##### PG 16 CH 2               #####
####################################


''' NOTES
    + ==    Addition
    - ==    subtraction
    * ==    Multiplication
    / ==    Division
    // ==   Floor Division (divide into whole number w/o remainder)
    % ==    Modulus (returns remainder)
    ** ==   Exponent

    a == b  Checks for equality
    a != b  and a <> b   check for inequality
    a > b   Checks if a is greater than b
    a < b   Checks if a is less than b
    a >= b  Checks if a is greater than or equal to b
    a <= b  Checks if a os less than or equal to b

    abs() == absolute value
    min == minimum in list
    max == max in list
'''

###########
### 2.1 ###
###########
print('\nPP 2.1')
# A
print(1 + 2 + 3 + 4 + 5)
# B
print((23 + 19 + 31) / 3)
# C
print(403 // 73)
# D
print(403 % 73)
# E
print(2 ** 10)
# F
print(abs(54 - 57))
# G
print(min(34.99, 29.95, 31.50))

###########
### 2.2 ###
###########
print('\nPP 2.2')
# A
print((2 + 2) < 4)
# B
print((7 // 3) == (1 + 1))
# C
print((3 ** 2) + (4 ** 2) == 25)
# D
print((2 + 4 + 6) > 12)
# E
print((1387 // 19) == 0)
# F
print(31 // 2 == 0)
# G
print(min(34.99, 29.95, 31.50) < 30)

###########
### 2.3 ###
###########
print('\nPP 2.3')
# A
a = 3
# B
b = 4
# C
c = a * a + b * b
print(c)

### PG 23 CH 2.2 Strings

''' NOTES
    x in s ==       True if x is substring of s
    x not in s ==   False if c is substring of s
    s + t ==        Concatenation of string s and t
    s * n, n * s == Concatenation of n copies of s
    s[i] ==         Character of string s at index i
    len(s) ==       Length of string s

    s[0] ==         1st index
    s[1] ==         2nd index
    s[-1] ==        last index
    s[-2] ==        2nd to last index


'''

###########
### 2.4 ###
###########
print('\nPP 2.4')
s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

# A
print(s1 + s2 + s3)
# B
print(s1 * 10)
# C
print(s1 + (s2 * 2) + (s3 * 3))
# D
print((s1 + ' ' + s2 + ' ') * 7)
# E
print(((s2 * 2) + s3 + ' ') * 5)

###########
### 2.5 ###
###########
print('\nPP 2.5')
s = '0123456789'

# A
print(s[0])
# B
print(s[1])
# C
print(s[6])
# D
print(s[-2])
# E
print(s[-1])

### PG 27 CH 2.3 Lists

''' NOTES
    x in lst ==         True if object x is in t
    x not in lst ==     False if object c is in lst
    lstA + lstB ==      Concatenation of lists A and B
    lst * n, n * lst == Concatenation of n copies of lst
    lst[i] ==           Item at index i of lst
    len(lst) ==         Length of lst
    min(lst) ==         Smallest item in lst
    max(lst) ==         Largest item in lst
    sum(lst) ==         Sum of items in lst

    lst.append(item) ==         Adds item at the end of lst
    lst.count(item) ==          Returns the number of occurrences of item in lst
    lst.index(item) ==          Returns the index of the first occurrence of item in lst
    lst.insert(item, index) ==  Insets item into lst just before index
    lst.pop() ==                Removes last item in the lst
    lst.remove(item) ==         Removes first occurrence of item in the lst
    lst.reverse() ==            Reverses the order of items in the list
    lst.sort()                  Sorts the list
'''


###########
### 2.6 ###
###########
print('\nPP 2.6')

words = ['bat', 'ball', 'barn', 'basket', 'badminton']
print(words[0])
print(words[-1])

###########
### 2.7 ###
###########
print('\nPP 2.7')

grades = [9, 7, 7, 10, 3, 9, 6, 6, 2]
# A
print(grades.count(7))
# B
grades[-1] = 4
print(grades[-1])
# C
print(max(grades))
# D
grades.sort()
print(grades)
# E
print(sum(grades) / len(grades))

########################################
##### 2.8 & 2.9 don't ask for code #####
########################################
### PG 31 CH 2.4 Objects and Classes

''' NOTES
    For import math
    sqrt(x) ==      √x
    ceil(x) ==      [x] (i.e., the smallest integer >= x)
    floor(x) ==     [x] (i.e., the largest integer <=x)
    cos(x)
    sin(x)
    log(x, base) == logbase(x)
    pi ==           3.14...
    e ==            2.72...

    REFERENCE
    circle:
        area ==                 pi * r ** 2
        circumference ==        2 * pi * r
        locus from center ==    (x - h) ** 2 + (y - k) ** 2 = r ** 2
'''

############
### 2.10 ###
############
print('\nPP 2.10')

# import math       // at top of file

x = 1
y = 2
a = 3
b = 4
r = 5

# A
print(math.sqrt(a ** 2 + b ** 2))
# B
print(math.sqrt(a ** 2 + b ** 2) == 5)
# C
print(math.pi * a ** 2)
# D
print((x - a) ** 2 + (y - b) ** 2 < r ** 2)
##################################################################
##### 2.11 based on Case study, done in "Perkovic Ch 2 - CS" #####
##################################################################
### PG 48 Exercises
print('Exercises')

############
### 2.12 ###
############
print('\nPP 2.12')

# A
print(sum(range(0, 8)))
## or print(1 + 2 + 3 + 4 + 5 + 6 + 7)
# B
print((65 + 57 + 45) / 3)
# C
print(2 ** 20)
# D
print(4356 // 61)
# E
print(4358 % 61)

############
### 2.13 ###
############
print('\nPP 2.13')

s1 = '-'
s2 = '+'
# A
print(s1 + s2)
# B
print(s1 + s2)
# C
print(s2 + s1 * 2)
# D
print((s2 + s1 * 2) * 2)
# E
print((s2 + s1 * 2) * 10 + s2)
# F
print((s2 + s1 + s2 * 3 + s1 * 2) * 5)

############
### 2.14 ###
############
print('\nPP 2,14')
s = 'abcdefghijklmnopqrstuvwxyz'
print(s[0])
print(s[2])
print(s[-1])
print(s[-2])
print(s[-10])

############
### 2.15 ###
############
print('\nPP 2.15')
s = 'goodbye'

# A
print(s[0] == 'g')
# B
print(s[6] == 'g')
# C
print(s[0:2] == 'ga')
# D
print(s[-2] == 'x')
# E
print(s[3] == 'd')
# F
print(s[0] == s[-1])
# G
print(s[-4:] == 'tion')

############
### 2.16 ###
############
print('\nPP 2.16')

# A
a = 6
b = 7
print(a, b)
# B
c = (a + b) / 2
print(c)
# C
inventory = ['paper', 'staples', 'pencils']
print(inventory)
# D
first = 'John'
middle = 'Fitzgerald'
last = 'Kennedy'
print(first, middle, last)
# E
fullname = first + ' ' + middle + ' ' + last
print(fullname)

############
### 2.17 ###
############
print('\nPP 2.17')

# A
print(17 + (-9) < 10)
# B
print(len(inventory) > 5 * len(fullname))
# C
print(c <= 24)
# D
print(a < 6.75 < b)
# E
print(len(first) < len(middle) < len(last))
# F
(print(inventory == [] or len(inventory) > 10))

############
### 2.18 ###
############
print('\nPP 2.18')

# A
flowers = ['rose', 'bougainvillea', 'yucca', 'marigold', 'daylilly', 'lilly of the valley']
# B
print('potato' in flowers)
# C
thorny = flowers[0:3]
print(thorny)
# D
poisonous = flowers[-1]
print(poisonous)
# E
dangerous = thorny + [poisonous]
print(dangerous)

############
### 2.19 ###
############
print('\nPP 2.19')

h, k, r = 0, 0, 10

# A
x, y = 0, 0
print((x - h) ** 2 + (y - k) ** 2 < r ** 2)
# B
x, y = 10, 10
print((x - h) ** 2 + (y - k) ** 2 < r ** 2)
# C
x, y = 6, 6
print((x - h) ** 2 + (y - k) ** 2 < r ** 2)
# D
x, y, = 7, 8
print((x - h) ** 2 + (y - k) ** 2 < r ** 2)

############
### 2.20 ###
############
print('\nPP 2.20')

''' REFERENCE
    Trig
        l = h / sin(rad)
        rad = (pi * deg)/ 180
'''

# A
l = 16
deg = 75
rad = (math.pi * deg) / 180
print(l * math.sin(rad))
# B
l = 20
deg = 0
rad = (math.pi * deg) / 180
print(l * math.sin(rad))
# C
l = 24
deg = 45
rad = (math.pi * deg) / 180
print(l * math.sin(rad))
# D
l = 24
deg = 80
rad = (math.pi * deg) / 180
print(l * math.sin(rad))

############
### 2.21 ###
############
print('\nPP 2.21')

s = 'top'
print(s[::-1])

############
### 2.22 ###
############
print('\nPP 2.22')

s = 'Don Ron'
s = s.split()
print(s[0][0] + s[1][0])

############
### 2.23 ###
############
print('\nPP 2.23')

lst = [3, 7, -2, 12]
print((max(lst)) - (min(lst)))

############
### 2.24 ###
############
print('\nPP 2.24')

lst = [3, 7, -2, 12, 9]
# A
print(lst.index(sorted(lst)[len(lst) // 2]))
# B
print(sorted(lst)[len(lst) // 2])
# C
print(sorted(lst, reverse=True))

############
### 2.25 ###
############
print('\nPP 2.25')
print(0 == (1 == 2))
print(2 + (3 == 4) + 5 == 7)
print(1 < (-1) == (3 > 4))
###################################################################
##### 2.26+ based on Case study, done in "Perkovic Ch 2 - CS" #####
###################################################################
