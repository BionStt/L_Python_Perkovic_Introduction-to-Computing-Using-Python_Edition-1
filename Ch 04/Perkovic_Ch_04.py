__author__ = 'Rolando'
##################################################
### Perkovic Intro to Python                   ###
#### CH 4: Text Data, Files, and exceptions   ####
##### PG 95 CH 4                             #####
##################################################

excuse = 'I\'m "sick"'
print(excuse)

poem = '''
To make a prairie it takes a clover  and one bee, -
One clover and a bee,
And revery.
The revery alone alone will do
If bees are few
'''
poem2 = '\nTo make a prairie it takes a clover and one bee, -\nOne clover, and a bee,\nAnd revery.\nThe revery alone ' \
        'will do\nIf bees are few.\n'
print(poem)
print(poem2)

''' REFERENCE
    s.find() == The index of the first occurrence of substring target in string s
    s.count(target) == The number of occurrences of substring target in string
    s.capitalize() == A copy of string with the first character capitalized if in alphabet
    s.upper() ==  A copy of string converted to uppercase
    s.lower() == A copy of string converted to lowercase
    s.split(sep) == A list of substring of string, obtained using delimiter string sep; the default delimiter is blank
    s.replace(old, new) ==  A copy of string with each occurrence of old is replaced by new
    s.strip() == A copy of string with leading and trailing blank spaces removed
    s.translate(table) == A copy of string s in which characters have been replaced by table
'''
###########
### 4.1 ###
###########
print('\nPP 4.1')

s = '0123456789'
# A
print(s[2:5])
# B
print(s[7:9])
# C
print(s[1:8])
# D
print(s[0:4])
# E
print(s[-3:])

###########
### 4.2 ###
###########
print('\nPP 4.2')

forecast = 'It will be sunny today'
# A
count = forecast.count('day')
print(count)
# B
weather = forecast.index('sunny')
print(weather)
# C
change = forecast.replace('sunny', 'cloudy')
print(change)

###########
### 4.4 ###
###########
print('\nPP 4.3')

last = 'Smith'
first = 'John'
middle = 'Paul'

print(last, first, middle, sep='\t')

###########
### 4.4 ###
###########
print('\nPP 4.4')


def even(n):
    """
    :param n: number
    :return:  all numbers in between and including 2 and n, that are divisible by 2 or 3
    """
    for i in range(1, n + 1):
        if i % 2 == 0 or i % 3 == 0:
            print(i, end=', ')

print(even(17))

###########
### 4.5 ###
###########
print('\nPP 4.5')
first = 'John'
last = 'Doe'
street = 'Main Street'
number = 123
city = 'AnyCity'
state = 'AS'
zipcode = '09876'

print('{0} {1}\n{3} {2}\n{4}, {5} {6}'.format(first, last, street, number, city, state, zipcode))

''' REFERENCE
    {:b} == Outputs the number in binary
    {:c} == Outputs the Unicode character corresponding to the integer value
    {:d} == Outputs the number in decimal notation (default)
    {:o} == Outputs the number in base 8
    {:x} == Outputs the number in base 16, using lower case letters for the digits above 9
    {:X} == Outputs the number in base 16, using uppercase letters for the digits above 9
'''


def growthrates(n):
    """prints values of below 3 function for i = 1, .., n"""
    print('  i   i**2    i**3    2**i')
    format_str = '{0:3d} {1:6d} {2:7d} {3:7d}'
    for i in range(2, n + 1):
        print(format_str.format(i, i ** 2, i ** 3, 2 ** i))

print(growthrates(12))

###########
### 4.6 ###
###########
print('\nPP 4.6')


def roster(l):
    """prints roster based on student info"""
    print('Last       First      Class      Average Grade')
    format_str = '{0:10} {1:10} {2:10} {3:8.2f}'
    for i in l:
        print(format_str.format(i[0], i[1], i[2], i[3]))

students = []
students.append(['DeMoines', 'Jim', 'Sophomore', 3.45])
students.append(['Pierre', 'Sophie', 'Sophomore', 4.0])
students.append(['Columbus', 'Maria', 'Senior', 2.5])
students.append(['Phoenix', 'River', 'Junior', 2.45])
students.append(['Olympis', 'Edgar', 'Junior', 3.99])
print(roster(students))

###########
### 4.7 ###
###########
outfile0 = open('example.txt', 'w')
exampletext = 'The 3 lines in this file end with the new line character.\n\nThere is a blank line above this line.\n'
outfile0.write(exampletext)
outfile0.close()

""" REFERENCE
    open('example.txt', 'r')
    r == Reading mode (default)
    w == Writing mode; if the file already exists, its content is wiped
    a == Append mode; writes are appened to the end of the file
    r+ == Reading and writing mode
    t == Text mode (default)
    b == binary mode

    infile = open('example.txt')
    infile.read(n) == Read n characters from the file or until the end of the file is reached; return characters as str
    infile.read() == Read characters from file infile until the end of the file and return characters read as str
    infile.readline() == Read file until (and including) the new line character or until end of file, and return str
    infile.readlines() == Read file until the end of the file and return the characters read as a list lines
    file.close() == Close the file
"""

infile = open('example.txt')
print(infile.read(1))
print(infile.read(5))
print(infile.readline())
print(infile.read())
infile.close()


def numchars(filename):
    """
    :param filename: txt file
    :return: number of characters in file
    """
    infile1 = open(filename, 'r')
    content1 = infile1.read()
    infile1.close()

    return len(content1)
print(numchars('example.txt'))

print('\nPP 4.7')


def stringcount(filename, s2):
    """
    :param filename: txt file
    :param s2: target string
    :return: number of occurrences of string
    """
    infile2 = open(filename, 'r')
    content2 = infile2.read()
    infile2.close()

    return content2.count(s2)
print(stringcount('example.txt', 'line'))

###########
### 4.8 ###
###########


def numwords(filename):
    """
    :param filename: txt file
    :return: list and number of words in filename
    """
    infile3 = open(filename, 'r')
    content3 = infile3.read()
    infile3.close()

    wordlist = content3.split()
    print(wordlist)
    return len(wordlist)
print(numwords('example.txt'))

print('\nPP 4.8')


def numwords2(filename):
    """
    :param filename: txt file
    :return: list and number of words in filename without punctuation symbols
    """
    infile4 = open(filename, 'r')
    content4 = infile4.read()
    infile4.close()

    table = str.maketrans('!,.:;?', 6 * ' ')
    content4 = content4.translate(table)
    wordlist2 = content4.split()
    print(wordlist2)
    return len(wordlist2)
print(numwords2('example.txt'))

###########
### 4.9 ###
###########


def numlines(filename):
    """
    :param filename: txt file
    :return: number of lines in the file
    """
    infile5 = open(filename, 'r')
    linelist = infile5.readlines()
    infile5.close()

    print(linelist)
    return len(linelist)
print(numlines('example.txt'))

infile6 = open('example.txt')
for line in infile6:                        # ^ Saves Active memory
    print(line, end='')
infile6.close()

print('\nPP 4.9')


def mygrep(filename, s3):
    """
    :param filename: txt file
    :param s3: target string
    :return: each line in file that contains the target string
    """
    infile7 = open(filename, 'r')
    linelist2 = infile7.readlines()
    infile7.close()
    for line1 in linelist2:
        if s3 in line1:
            print(line1, end='')
print(mygrep('example.txt', 'line'))

############
### 4.10 ###
############
outfile = open('test.txt', 'w')
outfile.write('T')
outfile.write('his is the first line.')
outfile.write(' Still the first line...\n')
outfile.write('Now we are in the second line.\n')
outfile.write('Non string value like ' + str(5) + ' must be converted first. \n')
outfile.write('Non string value like {} must be converted first.\n'.format(5))
outfile.close()
infile8 = open('test.txt', 'r')
infile8.close()
print('\nPP 4.10')

# A
print(3 + 4)
# B
# C
lst = [4, 5, 6]
# D
for t in range(10):
    print(t)

""" REFERENCE
    KeyboardInterrrupt == Raised when the user hits Ctrl-C, the interrupt key
    OverflowError == Raised when a floating-point expression evaluates to a value that is too large
    IOError == Raised when an I/O operation fails for an I/O-related reason
    IndexError == Raised when a sequence index is outside the range of valid indexes
    Name Error == Raised whn attempting too evaluate an unassigned identifier
    TypeError == Raised when an operation of function is applied to an object of the wrong type
    ValueError ==  Raised when operation or function has an argument
"""
##################################################################
##### 4.11 based on Case study, done in "Perkovic Ch 4 - CS" #####
##################################################################

################
##### 4.12 #####
################
print('\nPP 4.12')

s = 'abcdefghijklmnopqrstuvwxyz'

print(s[1:4])
print(s[0:3])
print(s[3:-2])
print(s[-4:-1])
print(s[-4:])

############
### 4.13 ###
############
print('\nPP 4.13')

s1 = 'goodbye'
# A
print(s1[1:3] == 'bc')
# B
print(s1[0:14] == 'abcdefghijklmn')
# C
print(s1[14:] == 'opqrstuvwxyz')
# D
print(s1[1:-1] == 'bcdefghijklmnopqrstuvwxy')

############
### 4.14 ###
############
print('\nPP 4.14')

# A
log = '128.0.0.1 - - [12/Feb/2011:10:31:08 -0600] "GET /docs/test.txt HTTP/1.0"'
print(log)
# B
address = log[0:14]
print(address)
# C
date = log[15:41]
print(date)

############
### 4.15 ###
############
print('\nPP 4.15')

ss = '10 20 30 40 50 60'
print(ss.split())
ss = '10,20,30,40,50,60'
print(ss.split(','))
ss = '10&20&30&40&50&60'
print(ss.split('&'))
ss = '10 - 20 - 30 - 40 - 50 - 60'
print(ss.split(' - '))

############
### 4.16 ###
############
print('\nPP 4.16')

first1 = input('Enter first word: ')
second1 = input('Enter second word: ')
third1 = input('Enter third word: ')
fst = [first1, second1, third1]
fsta = sorted(fst)
print(fst == fsta)

############
### 4.17 ###
############
print('\nPP 4.17')

# A
message1 = 'The secret of this message is that it is secret.'
print(message1)
# B
length = len(message1)
print(length)
# C
count = message1.count('secret')
print(count)
# D
censored = message1.replace('secret', 'xxxxx')
print(censored)

############
### 4.18 ###
############
print('\nPP 4.18')

sss = '''It was the best of times, it was the worst of times; it
was the age of wisdom, it was the age of foolishness; it was the
epoch of belief, it was the epoch of incredulity; it was ...'''
print(sss)

# A
table1 = str.maketrans('.,,, ;,\n', '        ')
newS = sss.translate(table1)
print(newS)
# B
newS = newS.strip()
print(newS)
# C
newS = newS.lower()
print(newS)
# D
print(newS.count('it was'))
# E
newS = newS.replace('it was', 'it is')
print(newS)
# F
listS = newS.split()
print(listS)

############
### 4.19 ###
############
print('\nPP 4.19')

first2 = 'Marlena'
last2 = 'Sigel'
middle2 = 'Mae'

# A
print('{1}, {0} {2}'.format(first2, last2, middle2))
# B
print('{1}, {0} {2}.'.format(first2, last2, middle2[0]))
# C
print('{0} {2}. {1}'.format(first2, last2, middle2[0]))
# D
print('{0}. {2}. {1}'.format(first2[0], last2, middle2[0]))

############
### 4.20 ###
############
print('\nPP 4.20')

sender = 'tim@abc.com'
recipient = 'tom@xyz.org'
subject = 'Hello!'
print('From: {0}\nTo: {1}\nSubject: {2}'.format(sender, recipient, subject))

############
### 4.21 ###
############
print('\nPP 4.21')

import math
pi = math.pi
e = math.e
# A
print('pi = {0:.2}, e = {1:.2}'.format(pi, e))
# B
print('pi = {0:.3}, e = {1:.2}'.format(pi, e))
# C
print('pi = {0:e}, e = {1:e}'.format(pi, e))
# D
print('pi = {0:.6}, e = {1:.6}'.format(pi, e))

############
### 4.22 ###
############
print('\nPP 4.22')


def month(m):
    """
    :param m: month Number
    :return:  month Word
    """
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov' 'Dec']
    return months[m - 1]

print(month(4))

############
### 4.23 ###
############
print('\nPP 4.23')


def average():
    """
    :return:
    """
    a = 0
    s6 = input('Enter a sentence: ')
    list1 = s6.split()
    for i in list1:
        a += len(i)
    return a / len(list1)

print(average())

############
### 4.24 ###
############
print('\nPP 4.24')


def cheer(team):
    """
    :param team: team name
    :return:     team cheer
    """
    teamu = team.upper()
    teaml = list(teamu)
    result = ''
    for ch in teaml:
        result = result + (ch + ' ')
    teamsep = result.strip()
    end = ("How do you spell winner?\nI know, I know!\n{0} !\n"
           "And that's how you spell winner!\nGo Huskies!".format(teamsep))
    return end

print(cheer('Huskies'))

############
### 4.25 ###
############
print('\nPP 4.25')


def vowelcount(vphrase):
    """
    :param vphrase: string
    :return:        time vowels appear in 'format_str' format
    """
    lower = vphrase.lower()
    nospace = lower.replace(' ', '')
    vphraselst = list(nospace)
    result = ''
    for ch in vphraselst:
        if ch in 'aeiouAEIOU':
            result = result + ch
    ac = result.count('a')
    ec = result.count('e')
    ic = result.count('i')
    oc = result.count('o')
    uc = result.count('u')
    format_str = 'a, e, i, o, and u appear, respectively, {}, {}, {}, {}, {} times.'
    end = format_str.format(ac, ec, ic, oc, uc)
    return end
print(vowelcount('Le Tour de France'))

############
### 4.26 ###
############
print('\nPP 4.26')


def crypto(file):
    infile11 = open(file, 'r')
    content = infile11.read()
    infile11.close()
    end = content.replace('Secret' and 'secret', 'xxxxx')
    return end
print(crypto('crypto.txt'))

############
### 4.27 ###
############
print('\nPP 4.27')


def fcopy(file, file2):
    input12 = open(file, 'r')
    output = open(file2, 'w')
    incontent = input12.read()
    input12.close()
    output.write(incontent)
    output.close()
    outputagain = open(file2, 'r')
    outcontent = outputagain.read()
    outputagain.close()
    return outcontent


print(fcopy('example.txt', 'output.txt'))

############
### 4.28 ###
############
print('\nPP 4.28')


def links(html):
    infile13 = open(html, 'r')
    content = infile13.read()
    linknum = content.count('</a>')
    infile13.close()
    return linknum

print(links('twolinks.html'))

############
### 4.29 ###
############
print('\nPP 4.29')


def stats(file):
    infile14 = open(file, 'r')
    content = infile14.read()
    linec = content.count('\n') + 1
    wordlist = content.split()
    wordc = len(wordlist)
    characterc = len(content)
    infile14.close()
    format_str = 'line count: {}\nwordcount: {}\ncharacter count: {}'
    end = format_str.format(linec, wordc, characterc)
    return end

print(stats('example.txt'))

############
### 4.30 ###
############
print('\nPP 4.30')


def distribution(file):
    infile15 = open(file, 'r')
    content = infile15.read()
    infile15.close()
    gradeslist = content.split()
    ac = gradeslist.count('A')
    amc = gradeslist.count('A-')
    bpc = gradeslist.count('B+')
    bc = gradeslist.count('B')
    bmc = gradeslist.count('B-')
    cpc = gradeslist.count('C+')
    cc = gradeslist.count('C')
    cmc = gradeslist.count('C-')
    fc = gradeslist.count('F')
    str_format = ('{} Students got A\n{} Students got A-\n{} Students got B+\n{} Students got B\n{} Students got B-'
                  '{} Students got C+\n{} Students got C\n{} Students got C-\n{} Students got F')
    end = str_format.format(ac, amc, bpc, bc, bmc, cpc, cc, cmc, fc)
    return end
print(distribution('grades.txt'))

############
### 4.31 ###
############
print('\nPP 4.31')


def duplicate(file):
    infile16 = open(file, 'r')
    content = infile16.read()
    infile16.close()
    table = str.maketrans('!,.:;?', 6 * ' ')
    content = content.translate(table)
    wordlist = content.split()
    truelist = []
    for word in wordlist:
        if wordlist.count(word) > 1:
            truelist.append('True')
    return 'True' in truelist


print(duplicate('Duplicates.txt'))
print(duplicate('noDuplicates.txt'))