def complete(abbreviation):
    'returns day of the week corresponding to abbreviation'

    days = {'Mo': 'Monday', 'Tu':'Tuesday', 'We': 'Wednesday',
            'Th': 'Thursday', 'Fr': 'Friday', 'Sa': 'Saturday',
            'Su':'Sunday'}

    return days[abbreviation]



def frequency(itemList):
    'returns frequency of items in itemList'
    counters = {}            # initialize dictionary of counters

    for item in itemList:
        
        if item in counters:     # counter for item already exists
            counters[item] += 1      # so increment it 
        else:                    # counter for item is created
            counters[item] = 1       # and initialized to 1

    return counters



##################################
# Solutions to Practice Problems #
##################################



def birthState(president):
    'returns the birth state of the given president'

    states = {'Barack Hussein Obama II':'Hawaii',
              'George Walker Bush':'Connecticut',
              'William Jefferson Clinton':'Arkansas',
              'George Herbert Walker Bush':'Massachussetts',
              'Ronald Wilson Reagan':'Illinois',
              'James Earl Carter, Jr':'Georgia'}

    return states[president]



def rlookup(phonebook):
    '''implements an interactive reverse phone book lookup service
        phonebook is a dictionary mapping phone numbers to names'''
    while True:
        number = input('Enter phone number in the\
                        format (xxx)xxx-xx-xx: ')
        if number in phonebook:
            print(phonebook[number])
        else:
            print('The number you entered is not in use.')



def wordCount(text):
    'prints frequency of each word in text' 
    wordList = text.split()  # split text into list of words
    counters ={}             # dictionary of counters
    for word in wordList:   
        if word in counters: # counter for word exists
            counters[word] += 1
        else:                # counter for word doesn't exist
            counters[word] = 1
    for word in counters:    # print word counts
        if counters[word] == 1:
            print('{:8} appears {} time.'.format(word,\
                                                 counters[word]))
        else:
            print('{:8} appears {} times.'.format(word,\
                                                  counters[word]))



def lookup(phonebook):
    '''implements interactive phone book service using the input
       phonebook dictionary'''
    while True:
        first = input('Enter the first name: ')
        last = input('Enter the last name: ')

        person = (first, last)    # construct the key

        if person in phonebook:   # if key is in dictionary
            print(phonebook[person])  # print value
        else:                     # if key not in dictionary
            print('The name you entered is not known.')



def sync(phonebooks):
    'returns the union of sets in phonebooks' 
    res = set()  # initialize the accumulator

    for phonebook in phonebooks:
        res = res | phonebook # accumulate phonebook into res
    return res



def encoding(text):
    'prints ASCII codes of characters in S, one per line'
    print('Char Decimal  Hex   Binary') # print column headings

    for c in text:
        code = ord(c)   # compute ASCII code
        # print character and its code in decimal, hex, and binary
        print(' {}   {:7} {:4x}  {:7b}'.format(c, code, code, code))



def char(low, high):
    '''prints the characters with ASCII codes
       in the range from low to high'''
    for i in range(low, high+1):
        # print integer ASCII code and corresponding character
        print('{} : {}'.format(i, chr(i)))



import random
def guess(n):
    'an interactive number guessing game'
    secret = random.randrange(0,n)   # generate secret number

    while True:
        # user enters a guess
        guess = eval(input('Enter your guess: '))
        if guess == secret:
            print('You got it!')
            break
        elif guess < secret:
            print('Too low.')
        else: # guess > secret
            print('Too high.')



import random
def approxPi(total):
    'return approximate value of pi based on "dart throwing"'
    count = 0                # counts darts hitting dartboard
    for i in range(total):
        x = random.uniform(-1,1) # x-coordinate of dart
        y = random.uniform(-1,1) # y coordinate of dart
        if x**2+y**2 <= 1:       # if dart hit dartboard:
            count += 1               # increment count
    return 4*count/total

