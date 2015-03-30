__author__ = 'Rolando'
#############################################
### Perkovic Intro to Python              ###
#### CH 6: Containers and Randomness     ####
##### PG 171 CH 6                       #####
#############################################

# Dictionaries
days = {'Mo': 'Monday',         # A dictionary is a container (a class, like a list) that stores items
        'Tu': 'Tuesday',        # that are accessible using "user-specified" indexes.
        'We': 'Wednesday',
        'Th': 'Thursday',
        'Fr': 'Friday'}

print(days)                     # Dictionaries are not ordered the same way they are listed
print(days['We'])               # Values are accessed by keys, not by index (but still use same operator d[k]

days['Sa'] = 'Saturday'         # Dictionaries are mutable
days['Su'] = 'Sunday'
print(days['Sa'], days['Su'])
print(days)

print(len(days))                # Operator len() can still be used on dictionaries

print('Fr' in days)             # so can k in d (key in dictionary)
print('Ja' in days)
print('Feb' not in days)        # and k not in d

favorites = {'Th': 'Thrusday',  # other operators are not applicable to dictionaries
             'Fr': 'Friday',    # such as +, *, max(), min(), and sum(), among others
             'Sa': 'Saturday'}
days.pop('Su')                  # and dictionaries share very few operators with lists as well
days.pop('Sa')                  # such as d.pop(k)
print(days)

days['Sa'] = 'Sat'              # another method is d1.update(d2)
print(days)                     # Which updates d1 with d2
days.update(favorites)          # New entries from d2 are added if not present in d1
print(days)                     # Old keys are kept unless they are present in both
                                # values in d1 that have the same key as those on d2 are replaced by d2 values
print(days.keys())              # other operators are useful in representing dictionaries as well
print(days.values())
print(days.items())

for key in days.keys():
    print(key, end=' ')
print()
for value in days.values():
    print(value, end=', ')
print()
for item in days.items():
    print(item, end='; ')
print()
""" REFERENCE
    d.items() : Returns a view of (key, value) pairs in d as tuples
    d.get(k) : Returns the value of key k, equivalent to d[k]
    d.keys() : Returns a view of keys in d
    d.pop(k) : Removes the (key, value) pair with key k form d and returns the value
    d.update(d2) : Adds the (key, value) pairs of dictionary d2 to d
    d.values() Returns a view of the values of d
    [] = lst
    {:} = dict
    (,) = tuple
    {,} = set
"""

###########
### 6.1 ###
###########
print('\nPP 6.1')


def birthstate(s):
    """
    :param s: Name of president (Key)
    :return: State of birth for s president (Value)
    """
    presidents = {'Barrack Hussein Obama II': 'Hawaii',
                  'George Walker Bush': 'Connecticut',
                  'William Jefferson Clinton': 'Arkansas',
                  'George Herbert Walker Bush': 'Massachusetts',
                  'Ronald Wilson Reagan': 'Illinois',
                  'James Earl Carter, Jr': 'Georgia'}
    return presidents[s]
print(birthstate('Ronald Wilson Reagan'))


###########
### 6.2 ###
###########
print('\nPP 6.2')

rphonebook = {'(123)456-78-90': ['Anna', 'Karenina'],
              '(901)234-56-78': ['Yu', 'Tsun'],
              '(321)908-76-54': ['Hans', 'Castorp']}


def rlookup(d):
    """
    :param d: Dictionary (Phone-book) of Phone-numbers and Individuals
    :input number: Phone number (Key)
    :return: Name of individual (Value)
    """
    number = input('Enter a number in the format (xxx)xxx-xx-xx: ')
    if number not in d:
        return 'Incorrect number format, or the number you entered is not in use.'
    return d[number]
#print(rlookup(rphonebook))


def complete(abbreviation):
    """
    :param abbreviation: abbreviation which actually refers to key in day dictionary (Key)
    :return: day of the week corresponding to abbreviation (Value)
    """
    days2 = {'Mo': 'Monday',
             'Tu': 'Tuesday',
             'We': 'Wednesday',
             'Th': 'Thursday',
             'Fr': 'Friday',
             'Sa': 'Saturday',
             'Su': 'Sunday'}
    if abbreviation not in days2:
        return False
    return days2[abbreviation]
print(complete('Mo'))
print(complete('Su'))
print(complete('Ja'))


def frequency(itemlist):
    """
    :param itemlist: Takes list of items (list)
    :return: frequency of items on list (dict)
    """
    counters = {}                       # Initialize dictionary of counters
    for item1 in itemlist:
        if item1 in counters:            # Counter for item already exits
            counters[item1] += 1         # so increment it
        else:                           # If not, Counter for item is created
            counters[item1] = 1          # and initialized to 1
    return counters
students = ['Cindy', 'John', 'Cindy', 'Adam', 'Adam', 'Jimmy', 'Joan', 'Cindy', 'Joan']
print(frequency(students))

#################################
### 6.3 does not ask for code ###
#################################
print('\nPP 6.3')
print('No code needed')

###########
### 6.4 ###
###########
print('\nPP 6.4')


def wordcount(s):
    """
    :param s: (string)
    :return: frequency of each word on the text (dict)
    """
    counters = {}
    wordlist = s.split()
    for word in wordlist:
        if word in counters:
            counters[word] += 1
        else:
            counters[word] = 1
    for word in counters:
        if counters[word] == 1:
            print('{:8} appears {} time.'.format(word, counters[word]))
        else:
            print('{:8} appears {} times.'.format(word, counters[word]))
    return ''
text = 'all animals are equal but some animals are more equal than others'
print(wordcount(text))

###########
### 6.5 ###
###########
print('PP 6.5')

# Tuples
phonebook = {('Anna', 'Karenina'): '(123)456-78-90',    # In the function rlookup(), if we switch up keys and values
             ('Yu', 'Tsun'): '(901)234-56-78',          # an error occurs because the names are list objects
             ('Hans', 'Castorp'): '(321)908-76-54'}     # therefore a new class must b used called the tuple
print(phonebook)                                        # tuples behave as lists in almost every way except they are
                                                        # immutable, and use () instead of []


def lookup(d):
    """
    :param d: Dictionary (Phone-book) of Phone-numbers and Individuals
    :return: Phone Number (Value)
    """
    first = input('Enter the first name: ')
    last = input('Enter the last name: ')
    person = (first, last)
    if person not in d:
        return 'Name could not be found'
    return d[person]
#print(lookup(phonebook))

# Sets
phonebook1 = {'123-45-67', '234-56-78', '345-67-89'}
print(phonebook1)                                           # Sets have the same properties as mathematical sets
phonebook1 = {'123-45-67', '234-56-78', '345-67-89',        # Duplicates are ignored
              '123-45-67', '234-56-78'}                     # Which make sets useful for removing duplicates
print(phonebook1)                                           # But as with dictionaries, they are out of order as well

phonebook2 = set()                                          # Empty sets cannot be represented with braces since those
print(type(phonebook2))                                     # are use by dictionaries, so it must be called implicitly

print('123-45-67' in phonebook1)                            # set class supports operators that correspond to ususal
print('456-78-90' in phonebook1)                            # mathematical types and operations, as well as a few that
print('456-78-90' not in phonebook1)                        # can be used in lst, str, and dict

print(len(phonebook1))

phonebook3 = {'345-67-89', '456-78-90'}                     # Comparison operators are supported for sets
print(phonebook1 == phonebook3)
print(phonebook1 != phonebook3)

print({'123-45-67', '345-67-89'} <= phonebook1)
print(phonebook1 < phonebook1)
                                                            # Mathematical set operators can be used too such as
print(phonebook1 | phonebook3)                              # Union
print(phonebook1 & phonebook3)                              # Intersection
print(phonebook1 - phonebook3)                              # difference between sets
print(phonebook1 ^ phonebook3)                              # symmetrical difference

phonebook3.add('123-45-67')                                 # sets support their own methods as well
print(phonebook3)
phonebook3.remove('123-45-67')
print(phonebook3)
phonebook3.clear()
print(phonebook3)

''' REFERENCE
    x in s : True if x in ser s, else False
    x not in s : False if x is in set s, else True
    len(s) : Returns size of set x
    s == t : True if set s and t contain same elements, else False
    s != t : True if set s and t do not contain the same elements, else False
    s <= t : True if ever element of set s is in set t, else False
    s < t  : True if s <= t and s != t
    s | t : Returns the union of sets s and t (both sets combined into a single set)
    s & t : Returns the intersection of sets s and t (all elements that are in both sets)
    s - t : Returns the difference between sets s and t (set s with elements from set t removed)
    s ^ t : Returns the symmetric difference between sets s and t (Elements not shared by both sets)

    s.add(v) : adds v to set s
    s.remove(v) : removes v from set s
    s.clear() : removes all elements from set s and makes it an empty set
'''
###########
### 6.6 ###
###########
print('\nPP 6.6')


def sync(lst):
    """
    :param lst: list of phone-books (lst)
    :return: phone-book containing the union of all the phone-books (set)
    """
    pbl = set()
    for pb in lst:
        pbl = pbl | pb
    return pbl
phonebook4 = {'234-56-78', '456-78-90'}
phonebooks = [phonebook1, phonebook2, phonebook3, phonebook4]
print(sync(phonebooks))


###########
### 6.7 ###
###########
print('\nPP 6.7')


def encoding(s):
    """
    :param s: (str)
    :return: prints ASCII C code in decimal, hex, and binary notation for every character
    """
    print('Char Decimal Hex   Binary')         # Column headings
    for c in s:
        code = ord(c)                           # Compute ASCII code
        print(' {} {:7} {:4x} {:9b}'.format(c, code, code, code))
print(encoding('dad'))

###########
### 6.8 ###
###########
print('\nPP 6.8')


def char(low, high):
    """
    :param low: lowest ASCII value
    :param high: highest ASCII value
    :return: prints characters corresponding to ASCII decimal codes i for all values of i from low up to and including
             high
    """
    for i in range(low, high + 1):
        print('{} : {}'.format(i, chr(i)))
print(char(62, 67))

import random                           # Python has an RNG (random number generator)

print(random.randrange(1, 7))           # randrange() allows you to RNG within a range of integers
print(random.randrange(1, 7))
print(random.randrange(1, 7))
print(random.randrange(1, 7))
print(random.randrange(1, 7))

print(random.uniform(0, 1))             # uniform() allows you to RNG within a range of floats
print(random.uniform(0, 1))

rlst = [1, 2, 3, 4, 5]
print(random.shuffle(rlst))             # shuffle() lets you shuffle the order of a sequence
print(random.shuffle(rlst))

print(random.choice(rlst))              # choice() allows you to choose an item at random from a sequence
print(random.choice(rlst))

print(random.sample(rlst, 2))           # sample() allows you to choose multiple items from a container at random
print(random.sample(rlst, 3))
print(random.sample(rlst, 3))

###########
### 6.9 ###
###########
print('\nPP 6.9')


def guess(n):
    answer = random.randrange(1, n)
    while True:
        input1 = eval(input('Enter your guess: '))
        if input1 == answer:
            return 'You got it!'
        elif input1 == 'I quit':
            return 'Better luck next time!'
        elif input1 < answer:
            print('Too low.')
        else:
            print('Too high.')
#print(guess(100))

############
### 6.10 ###
############
print('\nPP 6.10')


def approxpi(n):
    count = 0
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x ** 2 + y ** 2 <= 1:
            count += 1
    return 4 * count / n
print(approxpi(1000))
print(approxpi(10000))

#####################################################################
### There is a case study file for chapter 6 - "Percovic Ch 06 CS ###
#####################################################################

############
### 6.11 ###
############
print('\nPP 6.11')


def easycrypto(s):
    """
    :param s: (str)
    :return: Every character at an odd position i in the alphabet will be encrypted with the character at position
             i + 1, and every character at an even position i will be encrypted with the character at position i - 1.
    """
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alpha2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alpha3 = alpha + alpha2
    al3 = list(alpha3)

    ad = {}
    nd = {}
    count = 0
    for letter in al3:
        count += 1
        ad[letter] = count
    count = 0
    for letter in al3:
        count += 1
        nd[count] = letter
    sl = list(s)
    for i in range(len(sl)):
        if sl[i] in al3:
            ch = sl[i]
            num = ad[ch]
            if num % 2 == 0:
                sl[i] = nd[num - 1]
            else:
                sl[i] = nd[num + 1]
    return ''.join(sl)


print(easycrypto('abc'))
print(easycrypto('ZOO'))

############
### 6.12 ###
############
print('\nPP 6.12')


def letter2number(s):
    """ Takes a letter grade (A, B, C, D, F, with + or -) and returns corresponding number grade. The numeric values
        for A, B, C, D, and F are 4, 3, 2, 1, 0, a + increases number grade value by 0.3 and a - decreases it by 0.3
    """
    grades = {'A': 4,
              'A-': 3.7,
              'B+': 3.3,
              'B': 3.0,
              'B-': 2.7,
              'C+': 2.3,
              'C': 2.0,
              'C-': 1.7,
              'D': 1.0,
              'F': 0}
    if s in grades:
        return grades[s]
    else:
        return 0

print(letter2number('A'))
print(letter2number('B+'))
print(letter2number('F'))

#####################
### 6.13 and 6.14 ###
#####################
print('\nPP 6.13')

agencies = {'CCC': 'Civilian Conservation Corps',
            'FCC': 'Federal Communications Board',
            'FDIC': 'Federal Deposit Insurance Corporation',
            'SSB': 'Social Security Board',
            'WPA': 'Works Progress Administration'}
print(agencies)
acronyms = agencies.keys()
print(acronyms)
# A
agencies['SEC'] = 'Securities and Exchange Commission'
print(agencies)
# B
agencies['SSB'] = 'Social Security Administration'
print(agencies)
# C
agencies.pop('CCC')
agencies.pop('WPA')
print(agencies)

############
### 6.14 ###
############
print('\nPP 6.14')

print(acronyms)

############
### 6.15 ###
############
print('\nPP 6.15')
phonebook5 = {('Anna', 'Karenina'): ['(123)456-78-90', '(777)777-77-77'],
              ('Yu', 'Tsun'): '(901)234-56-78',
              ('Hans', 'Castorp'): '(321)908-76-54'}
print(phonebook5)


#print(lookup(phonebook5))

############
### 6.16 ###
############
print('\nPP 6.16')

l3 = []
m3 = 3
count3 = 1
while m3 < 100:
    count3 += 1
    l3.append(m3)
    m3 = 3 * count3
mult3 = set(l3)
print(mult3)

l5 = []
m5 = 5
count5 = 1
while m5 < 100:
    count5 += 1
    l5.append(m5)
    m5 = 5 * count5
mult5 = set(l5)
print(mult5)

l7 = []
m7 = 7
count7 = 1
while m7 < 100:
    count7 += 1
    l7.append(m7)
    m7 = 7 * count7
mult7 = set(l7)
print(mult7)

multa = mult3 | mult5 | mult7
print(multa)

# A


def m35():
    mult35 = []
    for i in multa:
        if i % 35 == 0:
            mult35.append(i)
    return set(mult35)
print(m35())
# B


def m105():
    mult105 = []
    for i in multa:
        if i % 105 == 0:
            mult105.append(i)
    return set(mult105)
print(m105())
# C


def m3or7():
    mult3or7 = mult3 | mult7
    return mult3or7
print(m3or7())
# D


def m3or7nb():
    mult3or7nb = mult3 ^ mult7
    return mult3or7nb
print(m3or7nb())
# E


def m7not3():
    mult7not3 = mult7 - mult3
    return mult7not3
print(m7not3())

############
### 6.17 ###
############
print('\nPP 6.17')


def hexascii():
    """
    :return: prints the correspondence between the lowercase characters in the alphabet with their hexdecimal
             representation of their ASCII code. (using format str method)
    """
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    al = list(alpha)
    for letter in al:
        code = ord(letter)
        print('{}:{:2x}'.format(letter, code), end=' ')
print(hexascii())

############
### 6.18 ###
############
print('\nPP.6.18')


def coin():
    """
    :return: Flips a coin. Returns either heads or tails, with equal probability
    """
    answer = random.randrange(0, 2)
    if answer == 0:
        return 'Heads'
    else:
        return 'Tails'
print(coin())

############
### 6.19 ###
############
print('\nPP 6,19')

arabic = 'اسمي ادا'
japanese = '私の名前はエイダです'
serbian = 'Моје име је Ада'


def ut(s):
    """
    :param s: untranslated string
    :return: unicode code point for each char in str
    """
    for i in s:
        code = ord(i)
        print('{}{}'.format(i, code), end=' ')

print(ut(arabic))
print(ut(japanese))
print(ut(serbian))

############
### 6.20 ###
############
print('\nPP 6.20')

phonebook7 = {'Smith, Jane': '123-45-67',
              'Doe, John': '987-65-43',
              'Baker, David': '567-89-01'}


def reverse(d):
    """
    :param d: dictionary
    :return: reversed keys - values mapping of dict to values - keys
    """
    keys = []
    values = []
    d1 = {}
    for key1 in d.keys():
        keys.append(key1)
    for value1 in d.values():
        values.append(value1)
    for i in range(len(keys)):
        d2 = {values[i]: keys[i]}
        d1.update(d2)
    return d1
print(reverse(phonebook7))

############
### 6.21 ###
############
print('\nPP 6.21')


def ticker(file):
    """
    :param file: file
    :input: Company Name
    :return: Company Abbreviation
    """
    infile = open(file)
    content = infile.read()
    infile.close()
    content = content.replace('\t', '')
    content = content.replace('  ', '')
    content = content.strip()
    content = content.split('\n')
    company = []
    abrv = []
    d1 = {}
    for i in range(0, len(content), 2):
        company.append(content[i])
    for i in range(1, len(content), 2):
        abrv.append(content[i])
    for i in range(len(abrv)):
        d2 = {company[i]: abrv[i]}
        d1.update(d2)
    name = input('Enter Company name: ')
    if name not in company:
        return "Company not in file."
    return d1[name]
# print(ticker('nasdaq.txt'))

############
### 6.22 ###
############
print('\nPP 6.22')


def mirror(s):
    """
    :param s: string that has mirror image possible in alphabet
    :return: returns mirror image, else 'INVALID'
    """
    nomirror = 'acefghjklmnrstuyzBCDEFGJKLNPQRSZ'
    for i in s:
        if i in nomirror:
            return 'INVALID'
    table = str.maketrans('bdpq', 'dbqp')
    txt = s.translate(table)
    reversetxt = txt[:: -1]
    return reversetxt
print(mirror('vow'))
print(mirror('wood'))
print(mirror('bed'))

############
### 6.23 ###
############
print('\nPP 6.23')


def scarydict(file):
    """
    :param file: txt file
    :return: prints each word, line by line, removing duplicates, punctuation, and any word with 2 or less characters
    """
    infile = open(file)
    content = infile.read()
    infile.close()
    table = str.maketrans('''1234567890.,,, ;,`()-:!?"\n'[]_''', '                              ')
    content = content.translate(table)
    content = content.lower()
    contentlist = content.split()
    contentlist = list(set(contentlist))
    contentlist.sort()
    for i in contentlist:
        if len(i) < 3:
            contentlist.remove(i)
        else:
            print(i)
    return 'DONE'
print(scarydict('frankenstein.txt'))

############
### 6.24 ###
############
print('\nPP 6.24')


def names():
    """
    :input: Student name
    :return: while input isn't empty str, continue to ask for name of student; else print for every name the number of
             students with that name
    """
    studentlist = []
    input1 = input('Enter first student name: ')
    while input1 != '':
        studentlist.append(input1)
        input1 = input('Enter next name: ')
    counters = {}                       # Initialize dictionary of counters
    for item1 in studentlist:
        if item1 in counters:            # Counter for item already exits
            counters[item1] += 1         # so increment it
        else:                           # If not, Counter for item is created
            counters[item1] = 1          # and initialized to 1
    studentlist = list(set(studentlist))
    studentlist.sort()
    for item1 in studentlist:
        if counters[item1] == 1:
            print('There is {} student named {}'.format(counters[item1], item1))
        else:
            print('There are {} students named {}'.format(counters[item1], item1))
#print(names())

############
### 6.25 ###
############
print('\nPP 6.25')


def different(t):
    """
    :param t: table (2D list)
    :return: the number of unique entries in each
    """
    counters = {}
    for i in t:
        for j in i:
            if j in counters:
                counters[j] += 1
            else:
                counters[j] = 1
    return len(counters)

t1 = [[1, 0, 1], [0, 1, 0]]
t2 = [[32, 12, 52, 63], [32, 64, 67, 52], [64, 64, 17, 34], [34, 17, 76, 98]]

print(different(t1))
print(different(t2))

############
### 6.26 ###
############
print('\nPP 6.26')


def week():
    """
    :input: 2 letter abbreviation of day of the week
    :return: Name of day represented by input abbreviation
    """
    days1 = {'Mo': 'Monday',
             'Tu': 'Tuesday',
             'We': 'Wednesday',
             'Th': 'Thursday',
             'Fr': 'Friday',
             'Sa': 'Saturday',
             'Su': 'Sunday'}
    while True:
        input1 = input('Enter day abbreviation: ')
        if input1 in days1:
            print(days1[input1])
        else:
            break
    return 'DONE'
#print(week())

############
### 6.27 ###
############
print('\nPP 6.27')


def index(file, lst):
    """
    :param file: txt file
    :param lst: list of str
    :return: the lines in 'file' where each item in 'lst' appears
    """
    infile = open(file)
    content = infile.read()
    infile.close()
    table = str.maketrans('''.,,, ;,`()-:!?"'[]_''', '                   ')
    content = content.translate(table)
    content = content.lower()
    contentlist = content.split('\n')
    words = sorted(lst)
    wdic = {}
    for word in words:
        counter = 0
        for line in contentlist:
            counter += 1
            if word in line:
                if word in wdic:
                    wdic[word].append(counter)
                else:
                    wdic[word] = [counter]
    for word in words:
        print('{:10}{}'.format(word, ', '.join(str(x) for x in wdic[word])))

print(index('raven.txt', ['raven', 'mortal', 'dying', 'ghost', 'ghastly', 'evil', 'demon']))

############
### 6.28 ###
############
print('\nPP 6.28')


def translate(d):
    """
    :param d: translation dictionary (e.g. English - Spanish)
    :return: translation from one language (keys) to the other (values)
    """
    phrase = input('Please enter your phrase: ')
    wlist = phrase.split()
    alist = []
    for word in wlist:
        if word in d:
            alist.append(d[word])
        else:
            alist.append('____')
    return ' '.join(alist)
dt = {'I': 'Me',
      'like': 'gusta',
      'boobs': 'chichis'}

#print(translate(dt))

############
### 6.29 ###
############
print('\nPP 6.29')


def networks(n, lst):
    """
    :param n: number of networks
    :param lst: list of friend tuples (who is friends with who)
    :return:
    """
    groups = []                                     # Empty group list
    for i in range(n):                              # Make a group for every person (in range of n)
        groups.append({i})
    print(groups)

    for pair in lst:                                # For each tuple pair
        union = groups[pair[0]] | groups[pair[1]]   # Make union (variable) the union of the pair (tuple)
        for p in union:                             # for each person (value) in the union (set), the groups correspond
            groups[p] = union                       # to each person are
    print(groups)

    sets = set()
    for g in groups:
        sets.add(tuple(g))
    print(sets)

    i = 0
    for s in sets:
        print('Network {} is {}'.format(i, set(s)))
        i += 1
print(networks(5, [(0, 1), (1, 2), (3, 4)]))

############
### 6.30 ###
############
print('\nPP 6.30')


def simul(n):
    """
    :param n: number of times game of RPS is played
    :return:  simulated result of total games
              Rock = 0, Paper = 1, Scissors = 2
    """
    rounds = 0
    winner = 0
    for i in range(n):
        rounds += 1
        p1 = random.randrange(0, 3)
        p2 = random.randrange(0, 3)
        if p1 == p2:
            print('Round {}: Tie'.format(rounds))
        elif p1 == 0 and p2 == 1 or p1 == 1 and p2 == 2 or p1 == 2 and p2 == 0:
            winner += 1
            print('Round {}: Player 2 Wins'.format(rounds))
        else:
            winner -= 1
            print('Round {}: Player 1 Wins'.format(rounds))
    if winner == 0:
        return 'Overall result: Tie'
    elif winner > 0:
        return 'Overall result: Player 2'
    else:
        return 'Overall result: Player 1'
print(simul(1))
print(simul(1))
print(simul(10))

############
### 6.31 ###
############
print('\nPP 6.31')


def craps():
    """
    :return: Simulates a game of craps and returns 1 if player won and 0 if they lost
    """
    # first roll
    rounds = 1
    d1 = random.randrange(1, 7)
    d2 = random.randrange(1, 7)
    result1 = d1 + d2
    # print('Round {} roll: {}'.format(rounds, result1))
    if result1 == 7 or result1 == 11:
        return 1
    if result1 == 2 or result1 == 3 or result1 == 12:
        return 0

    # consecutive rolls
    result2 = 0
    while result2 != 7:
        d1 = random.randrange(1, 7)
        d2 = random.randrange(1, 7)
        result2 = d1 + d2
        rounds += 1
        # print('Round {} roll: {}'.format(rounds, result2))
        if result2 == result1:
            return 1
    return 0
print(craps())


def testcraps(n):
    counter = 0
    for i in range(n):
        counter += craps()
    return counter / n

print(testcraps(100))
print(testcraps(10000))

############
### 6.32 ###
############
print('\n6.32')


def manhattan(x, y):
    res = []
    for i in range(x):
        res.append([])
    for i in res:
        for j in range(y):
            i.append(0)
    position = (x // 2 + 1, y // 2 + 1)
    z = position[0]
    v = position[1]

    while z != -1 and z != x and v != -1 and v != y:
        res[z][v] += 1
        direction = random.randrange(1, 5)
        if direction == 1:
            v += 1
        elif direction == 2:
            z += 1
        elif direction == 3:
            v -= 1
        else:
            z -= 1
    for i in res:
        print(i)
print(manhattan(5, 11))

############
### 6.33 ###
############
print('\n6.33')

# import random


def shuffledeck():
    """
    :return: shuffled deck
    """
    suits = {'\u2660', '\u2661', '\u2662', '\u2663'}  # suits is a set od 4 unicode symbols: black spade and club,
    ranks = {'2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'}        # and white diamond and heart
    deck = []

    for suit in suits:                                  # Create a deck out of 52 cards
        for rank in ranks:                              # card is the concatenation
            deck.append(rank + ' ' + suit)              # of suit and rank

    random.shuffle(deck)                                # Shuffle the deck and return it
    return deck


def dealcard(deck, participant):
    """
    :param deck: deck from chuffledeck() (lst)
    :param participant: the hand of the participant (lst)
    :return: card dealt (added) to participant (a single card is dealt from the deck to the participant
    """
    card = deck.pop()
    participant.append(card)
    return card


def total(hand):
    """
    :param hand: the hand of participant (lst)
    :return: value of hand
    """
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
              '9': 9, '1': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    result = values[hand[0]]
    return result


def war():
    """
    :return: simulates a game of war and returns
    """
    # Step 1: Shuffle deck
    deck = shuffledeck()

    # Step 2: Split decks
    deck1 = deck[:int(len(deck) / 2)]
    deck2 = deck[int(len(deck) / 2):]
    hand1 = []
    hand2 = []

    # Step 3: Each player reveals top card of deck, player with higher card takes both cards and adds to his deck
    rounds = 0
    wars = 0
    while deck1 != [] and deck2 != []:
        rounds += 1
        winner = 0
        # Shuffle decks at start of each round
        random.shuffle(deck1)
        random.shuffle(deck2)

        play1 = deck1.pop()
        play2 = deck2.pop()

        # if cards have same value: war occurs
        if total(play1) == total(play2):
            wars += 1
            hand1.extend([play1] + deck1[-3:])
            deck1 = deck1[:-3]
            deck1.append(hand1.pop())

            hand2.extend([play2] + deck2[-3:])
            deck2 = deck2[:-3]
            deck.append(hand2.pop())
            winner = '\tWar'

        elif total(play1) > total(play2):
            deck1 = [play1, play2] + hand1 + hand2 + deck1
            hand1 = []
            hand2 = []
            winner = '\t1'

        elif total(play2) > total(play1):
            deck2 = [play2, play1] + hand2 + hand1 + deck2
            hand1 = []
            hand2 = []
            winner = '\t2'

        print('Round: {}, Player 1 card: {}, Player 2 card: {}'.format(rounds,
              play1, play2))
        print(winner)
    if deck2 is []:
        print('PLAYER 1 WINS WAR')
    else:
        print('PLAYER 2 WINS WAR')

    result = 'Total rounds: ' + str(rounds), 'Total wars: ' + str(wars)
    print(result)
    return rounds, wars

print(war())


def warstats(n):
    """
    :param n: The amount of times War is played
    :return: The average
    """
    trounds = 0
    twars = 0
    for i in range(n):
        wart = war()
        trounds += wart[0]
        twars += wart[1]
    arounds = trounds / n
    awars = twars / n
    return 'Average rounds: ' + str(arounds), 'Average wars: ' + str(awars)
print(warstats(10))

############
### 6.34 ###
############
print('\nPP 6.34')


def game(n):
    """
    :param n: Number of addition games
    :return: the amount of correct answers out of total
    """
    correct_answers = 0
    for i in range(n):
        a = random.randrange(0, 10)
        b = random.randrange(0, 10)
        answer = a + b
        print('{} + {} ='.format(a, b))
        kid = eval(input('Enter answer: '))
        if kid == answer:
            correct_answers += 1
            print('Correct.')
        else:
            print('Incorrect.')
    return 'You got {} correct answers out of {}'.format(correct_answers, n)
# print(game(3))

############
### 6.35 ###
############
print('\nPP 6.35')


def caesar(n, file):
    """
    :param n: key for caesar cipher
    :param file: text to be encrypted
    :return: encrypted text
    """
    infile = open(file)
    content = infile.read()
    infile.close()
    cipher = ''

    for i in content:
        c = ord(i)
        if 64 < c < 91 - n or 96 < c < 123 - n:
            cn = ord(i) + n
            cipher += chr(cn)
        elif 90 - n < c < 91 + n or 122 - n < c < 123 + n:
            cn = ord(i) + n - 26
            cipher += chr(cn)
        else:
            cipher += chr(c)

    return cipher
print(caesar(3, 'clear.txt'))

############
### 6.36 ###
############
print('\nPP 6.36')