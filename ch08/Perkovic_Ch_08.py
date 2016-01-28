__author__ = 'Rolando'
#############################################
### Perkovic Intro to Python              ###
#### CH 8: Object-Oriented Programming   ####
##### PG 251 CH 8                       #####
#############################################

""" REFERENCE
    x + y     : x.__add__(y)       : Addition                           : Concatenation
    x - y     : x.__sub__(y)       : Subtraction                        :
    x * y     : x.__mul__(y)       : Multiplication                     : Self-concatenation
    x / y     : x.__truediv__(y)   : Division                           :
    x // y    : x.__floordiv__(y)  : Integer division                   :
    x % y     : x.__mod__(y)       : Modulus                            :

    x == y    : x.__eq__(y)        : Equal to                           :
    x != y    : x.__ne__(y)        : Unequal to                         :
    x > y     : x.__gt__(y)        : Greater than                       :
    x >= y    : x.__ge__(y)        : Greater than or equal to           :
    x < y     : x.__lt__(y)        : Less than                          :
    x <= y    : x.__le__(y)        : Less than or equal to              :

    repr(x)   : x.__repr__()       : Canonical string representation    :
    str(x)    : x.__str__()        : Informal string representation     :
    len(x)    : x.__len__()        :                                    : Collection size
    <type>(x) : <type>.__init__(x) : Constructor                        :
"""

import math


class Point:
    """ Class that represents points in the plane
    """

    def __init__(self, xcoord=0, ycoord=0):
        """ Initializes point coordinates to(xcoord, ycoord)
        """
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        """ Set x coordinate of point to xcoord
        """
        self.x = xcoord

    def sety(self, ycoord):
        """ Set y coordinate to point ycoord
        """
        self.y = ycoord

    def get(self):
        """ Return a tuple with x and y coordinates of the point
        """
        return self.x, self.y

    def move(self, dx, dy):
        """ Change the x and y coordinates by dx and dy
        """
        self.x += dx
        self.y += dy

    def up(self):
        """ Moves object up by 1 point in plane
        """
        self.move(0, 1)

    def down(self):
        """ Moves object down by 1 point in plane
        """
        self.move(0, -1)

    def left(self):
        """ Moves object left by 1 point in plane
        """
        self.move(-1, 0)

    def right(self):
        """ Moves object right by 1 point in plane
        """
        self.move(1, 0)

    def getx(self):
        """ Return x coordinate
        """
        return self.x

    def distance(self, other):
        """ Return the distance of point self from point other
        """
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)

    def __eq__(self, other):
        """ self == other is they have the same coordinates
        """
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        """ Return canonical string representation of Point(x, y)
        """
        return 'Point({}, {})'.format(self.x, self.y)


class Animal:
    """ Represent an animal
    """

    def __init__(self, species='animal', language='make sounds', age='0'):
        """ Initializes animals info species and language
        """
        self.spec = species
        self.lang = language
        self.age = age

    def setspecies(self, species):
        """ Sets the animal species
        """
        self.spec = species

    def setlanguage(self, language):
        """ Sets the animal language
        """
        self.lang = language

    def setage(self, age):
        """ Sets the animal age
        """
        self.age = age

    def getage(self):
        """ Prints the age of the animal
        """
        return self.age

    def speak(self):
        """ Prints a sentence by the animal
        """
        if self.spec[0] in 'aeiouAEIOU':
            print('I am an {} and I {}'.format(self.spec, self.lang))
        else:
            print('I am a {} and I {}'.format(self.spec, self.lang))


class Card:
    """ Represents a playing card
    """

    def __init__(self, rank, suit):
        """ Initialize rank and suit of playing card
        """
        self.rank = rank
        self.suit = suit

    def get_rank(self):
        """ Return rank
        """
        return self.rank

    def get_suit(self):
        """ Return suit
        """
        return self.suit

    def __eq__(self, other):
        """ self == other if rank and suit are the same
        """
        return self.rank == other.rank and self.suit == other.suit

    def __repr__(self):
        """ Return canonical string representation of Card(rank, suit)
        """
        return "Card('{}', '{}')".format(self.rank, self.suit)

    def __gt__(self, other):
        """ self > other (suit hierarchy: spade > heart > diamond > club
        """
        if self.rank == other.rank:
            return self.suit < other.suit
        return self.rank > other.rank

    def __ge__(self, other):
        """ self >= other
        """
        if self.rank == other.rank:
            return self.suit <= other.suit
        return self.rank >= other.rank

    def __lt__(self, other):
        """ self < other
        """
        if self.rank == other.rank:
            return self.suit > other.suit
        return self.rank < other.rank

    def __le__(self, other):
        """ self <= other
        """
        if self.rank == other.rank:
            return self.suit >= other.suit
        return self.rank <= other.suit

import random


class Deck:
    """ Represents a deck of 52 cards
    """

    # ranks and suits are Deck class variables
    ranks = {'2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'}

    # suits is a set of 4 unicode symbols representing the 4 suits
    suits = {'\u2660', '\u2661', '\u2662', '\u2663'}

    def __init__(self, cardlist=None):
        """ Create a  deck using list of input cards or
           Initialize deck of 52 cards if None
        """
        if cardlist is None:                            # no input deck
            self.deck = []                              # deck is initially empty
            for suit in Deck.suits:                     # class variables
                for rank in Deck.ranks:
                    self.deck.append(Card(rank, suit))  # add Card with given rank and suit to deck
        else:
            self.deck = cardlist

    def deal_card(self):
        """ Deal (pop and return) card from the top of the deck
        """
        return self.deck.pop()

    def shuffle(self):
        """ Shuffle the deck
        """
        random.shuffle(self.deck)

    def __eq__(self, other):
        """ Return True if deck self and other contain the same items
        """
        return self.deck == other.deck

    def __len__(self):
        """ Returns number of items in deck
        """
        return len(self.deck)

    def __repr__(self):
        """ Returns
        """
        return 'Deck({})'.format(self.deck)


class Queue:
    """ A classic queue class
    """

    def __init__(self, q=None):
        """ Instantiate queue based on list q, default is empty queue
        """
        if q is None:
            self.q = []
        else:
            self.q = q

    def isempty(self):
        """ Returns True if queue is empty, False otherwise
        """
        return len(self.q) == 0

    def enqueue(self, item):
        """ Insert item at rear of queue
        """
        return self.q.append(item)

    def dequeue(self):
        """ Remove and return item at front of queue
        """
        return self.q.pop(0)

    def __eq__(self, other):
        """ Returns True if queues self and other contain the same items in the same order
        """
        return self.q == other.q

    def __len__(self):
        """ Returns number of items in queue
        """
        return len(self.q)

    def __repr__(self):
        """ Return canonical string representation of queue
        """
        return 'Queue({})'.format(self.q)

    def __getitem__(self, key):
        return self.q[key]

    # def __setitem__(self, key, item):
    #     self.q[key] = item

    def __contains__(self, key):
        return key in self.q

    def __iter__(self):
        """ Returns Queue iterator
        """
        return QueueIterator(self)


class QueueIterator:
    """ Iterator for Queue container class
    """

    def __init__(self, q):
        """ Constructor
        """
        self.index = len(q) - 1
        self.q = q

    def __next__(self):
        """ Returns next queue item; if no next item, raises StopIteration exception
        """
        if self.index < 0:
            raise StopIteration()

        # Return next item
        res = self.q[self.index]
        self.index -= 1
        return res


class MyList(list):
    """ A subclass of list that implements method choice
    """

    def choice(self):
        """ Return item from list chosen uniformly at random
        """
        return random.choice(self)

    def sort(self, **kwargs):
        """ Replaces sort function with the following string
        """
        return 'You wish ...'


class Bird(Animal):
    """ Represent a bird
    """

    def speak(self):
        """ Prints bird sounds
        """
        print('{}! '.format(self.lang) * 3)


class Super:
    """ A generic class with one method
    """

    def method(self):
        print('in Super.method')


class Inheritor(Super):
    """ Class that inherits method
    """

    pass


class Replacer(Super):
    """ Class that overrides method
    """

    def method(self):
        print('in Replacer.method')


class Extender(Super):
    """ Class that extends method
    """

    def method(self):
        print('starting Extender.method')
        Super.method(self)                  # Calling Super method
        print('ending Extender.method')


class Queue2(list):
    """ A queue class, subclass of list
    """

    def isempty(self):
        """ Returns true id queue is empty, False if otherwise
        """
        return len(self) == 0

    def dequeue(self):
        """ Remove and return item at front of queue
        """
        return self.pop(0)

    def enqueue(self, item):
        """ Insert item at rear of queue
        """
        return self.append(item)


class EmptyQueueError(Exception):
    pass


point = Point()

point.setx(3)
point.sety(4)
print(point.get())

point.move(0, -3)
print(point.get())

point.sety(-2)
print(point.get())

a = Point()
a.setx(3)
a.sety(4)
print(a.get())

print(a.getx())

b = Point()
b.setx(5)
b.sety(-2)
print(b.get())

print(a.x)
print(dir(a))

snoopy = Animal()
snoopy.setspecies('dog')
snoopy.setlanguage('bark')
print(snoopy.speak())

ini = int(93)
print(ini)

import fractions

fract = fractions.Fraction(3, 4)
print(fract)

card = Card('3', '\u2660')
print(card.get_rank())
print(card.get_suit())

deck = Deck()
deck.shuffle()
print(deck.deal_card())

fruit = Queue()
fruit.enqueue('apple')
fruit.enqueue('banana')
fruit.enqueue('coconut')
print(fruit.q)
fruit.dequeue()
print(fruit.q)
fruit.dequeue()
print(fruit.q)
fruit.dequeue()
print(fruit.isempty())

print(point)
point == Point(3, -2)

print(card)

mylst = MyList()

mylst.append(2)
mylst.append(3)
mylst.append(5)
mylst.append(3)

print(len(mylst))
print(mylst.count(3))
print(mylst.choice())

daffy = Bird()
daffy.setspecies('duck')
daffy.setlanguage('quack')
print(daffy.speak())


###########
### 8.1 ###
###########
print('\nPP 8.1')

# Function is in class Point : getx()

print(point.getx())

###########
### 8.2 ###
###########
print('\nPP 8.2')


class Test:
    """ This is a test class
    """
    version = 1.02

a = Test()
b = Test()

print(a.version)
print(b.version)
print(Test.version)
Test.version = 1.03
print(a.version)
# print(Point.version)
a.version = 'Latest!!'
# print(Point.version)
print(b.version)
print(a.version)

###########
### 8.3 ###
###########
print('\nPP 8.3')


class Rectangle:
    """ Represents rectangles
    """
    def __init__(self, width=0, length=0):
        """ Initialize rectangle with width and length 0, 0
        """
        self.width = width
        self.length = length

    def setsize(self, width, length):
        """ Sets the size of width and length sides
        """
        self.width = width
        self.length = length

    def perimeter(self):
        """ Returns the perimeter of the rectangle
        """
        return self.width * 2 + self.length * 2

    def area(self):
        """ Returns the area of the rectangle
        """
        return self.width * self.length

rectangle = Rectangle()
rectangle.setsize(3, 4)
print(rectangle.perimeter())
print(rectangle.area())

###########
### 8.4 ###
###########
print('\nPP 8.4')

# Function is in class Animal: __init__

snoopie = Animal('dog', 'bark')
print(snoopie.speak())

tweety = Animal('canary')
print(tweety.speak())

animal = Animal()
print(animal.speak())

###########
### 8.5 ###
###########
print('\nPP 8.5')

deck = Deck(['1', '2', '3', '4'])
deck.shuffle()
print(deck.deal_card())

###########
### 8.6 ###
###########
print('\nPP 8.6')

# Function is in class Card : __eq__ and __repr__

print(card)
print(Card('3', '♠') == Card('3', '♠'))
print(Card('3', '♠') == eval(repr(Card('3', '♠'))))

###########
### 8.7 ###
###########
print('\nPP 8.7')

# Function is in class Deck : __eq__, __repr__ and __len__

print(len(Deck()))
print(Deck() == Deck())
print(Deck() == eval(repr(Deck())))

###########
### 8.8 ###
###########
print('\nPP 8.8')


class Vector(Point):
    """ Inherits class Point and adds vector attributes
    """

    def __add__(self, other):
        """ Vector addition
        """
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        """ Vector product multiplication
        """
        return self.x * other.x + self.y * other.y

    def __repr__(self):
        """ Return canonical sting representation of Vector(x, y)
        """
        return 'Vector{}'.format(self.get())

v1 = Vector(1, 3)
v2 = Vector(-2, 4)

print(v1 + v2)
print(v1 * v2)

###########
### 8.9 ###
###########
print('\nPP 8.9')


# class Queue3(Queue):
#     """ Modified Queue class
#     """
#
#     def dequeue(self):
#         """
#         """
#         if len(self) == 0:
#             raise KeyboardInterrupt('dequeue from empty queue')
#         return self.q.pop(0)
#
# queue3 = Queue3()
# queue3.dequeue()
#
#
# class Queue4(Queue):
#     """ Modified Queue class
#     """
#
#     def dequeue(self):
#         """
#         """
#         if len(self) == 0:
#             raise EmptyQueueError('dequeue from empty queue')
#         return self.q.pop(0)
#
# queue4 = Queue4()
# queue4.dequeue()

############
### 8.10 ###
############
print('\nPP 8.10')


q1 = Queue()
q1.enqueue(5)
q1.enqueue(7)
q1.enqueue(9)
print(q1[1])
print()

for item1 in q1:
    print(item1)
print()

for i in range(len(q1)):
    print(q1[i])
print()

############
### 8.11 ###
############
print('\nPP 8.11')


class OddList(list):
    """ Behaves just as list except iteration patterns skip every other object
    """

    def __iter__(self):
        """ return list iterator object
        """
        return OddListIterator(self)


class OddListIterator(object):
    """ Odd iterator for OddList class
    """
    def __init__(self, lst):
        """ Constructor
        """
        self.lst = lst
        self.index = 0

    def __next__(self):
        """ Returns next oddlist item
        """
        if self.index >= len(self.lst):
            raise StopIteration

        res = self.lst[self.index]
        self.index += 2
        return res

lst0 = OddList(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
for item0 in lst0:
    print(item0, end=' ')

############
### 8.12 ###
############
print('\n\nPP 8.12')

c = Point()
c.setx(0)
c.sety(1)
d = Point()
d.setx(1)
d.sety(0)
print(c.distance(d))

############
### 8.13 ###
############
print('\nPP 8.13')

flipper = Animal()
flipper.setspecies('dolphin')
flipper.setage(3)
print(flipper.getage())

############
### 8.14 ###
############
print('\nPP 8.14')

a = Point(3, 4)
a.left()
print(a.get())

############
### 8.15 ###
############
print('\nPP 8.15')

rectangle = Rectangle(2, 4)
print(rectangle.perimeter())

rectangle = Rectangle()
print(rectangle.area())

############
### 8.16 ###
############
print('\nPP 8.16')

# x.__gt__(y)
# x.__ne__(y)
# x.__mod__(y)
# x.__floordiv__(y)
# x.__or__(y)


############
### 8.17 ###
############
print('\nPP 8.17')

print(Card('3', '♠') < Card('8', '♦'))
print(Card('3', '♠') > Card('8', '♦'))
print(Card('3', '♠') <= Card('8', '♦'))
print(Card('3', '♠') >= Card('8', '♦'))

############
### 8.18 ###
############
print('\nPP 8.18')


class MyInt(int):
    """ Subset of int class with addition changed
    """
    def __add__(self, other):
        """ Returns whatever when the operator + is directly used on self
        """
        return 'Whatever ...'

x = MyInt(5)
print(x * 4)
print(x * (4 + 6))
print(x + 6)

############
### 8.19 ###
############
print('\nPP 8.19')


class MyStr(str):
    """ Subset of str class with addition and multiplication changed
    """
    def __add__(self, other):
        """ Returns the sum of lengths of self and other (strings)
        """
        return len(self) + len(other)

    def __mul__(self, other):
        """ Returns the product of the lengths of the two strings
        """
        return len(self) * len(other)


x = MyStr('hello')
print(x + 'universe')
print(x * 'universe')

############
### 8.20 ###
############
print('\nPP 8.20')

x = MyList([1, 2, 3])
print(x)
print(x.reverse())
print(x[2])
print(x.sort())

############
### 8.21 ###
############
print('\nPP 8.21')

# eval makes the function call a global variable instead of a local one

############
### 8.22 ###
############
print('\nPP 8.22')

# Just change 2 to 3 in the class variable

############
### 8.23 ###
############
print('\nPP 8.23')


class NegativeBalanceError(Exception):
    pass


class OverdraftError(Exception):
    pass


class DepositError(Exception):
    pass


class BankAccount:
    """ creates a bank account
    """
    def __init__(self, bal=0):
        """ Constructor: Initializes bank account with bal as starting balance
        """

        # if bal < 0:
        #     raise ValueError('Illegal Balance')

        if bal < 0:
            raise NegativeBalanceError('Account created with negative balance: {}'.format(bal))
        self.bal = bal

    def __repr__(self):
        """
        """
        return '{0:.2f}'.format(self.bal)

    def withdraw(self, n):
        """ Removes n value from balance
        """

        # if n > self.bal:
        #     raise ValueError('Overdraft')
        # elif n < 0:
        #     raise ValueError('Negative Withdrawal')

        if n > self.bal:
            raise OverdraftError('Operation would result in negative balance: {}'.format(self.bal - n))

        self.bal -= n

    def deposit(self, n):
        """ Adds n value from balance
        """

        # if n < 0:
        #     raise ValueError('Negative Deposit')

        if n < 0:
            raise DepositError('Negative deposit: {}'.format(n))

        self.bal += n

    def balance(self):
        """ Returns the balance on the account
        """
        return eval('{0:.2f}'.format(self.bal))

x = BankAccount(700)
print(x.balance())
x.withdraw(70)
print(x.balance())
x.deposit(7)
print(x.balance())
x.withdraw(6.9801)
print(x.balance())

############
### 8.24 ###
############
print('\nPP 8.24')


class Polygon:
    """ Abstracts regular polygons and supports class methods
    """

    def __init__(self, n=0, s=0):
        """ Constructor: initializes polygon with sides length (len) and number of sides (n)
        """
        self.length = s
        self.sides = n

    def perimeter(self):
        """ Returns the perimeter of the polygon
        """
        return self.length * self.sides

    def area(self):
        """ Returns the area of the polygon
        """
        return (self.length ** 2 * self.sides) / (4 * math.tan(math.pi / self.sides))

p2 = Polygon(6, 1)
print(p2.perimeter())
print(p2.area())

############
### 8.25 ###
############
print('\nPP 8.25')


class Worker:
    """ Creates a basic worker namespace
    """
    def __init__(self, name='Unknown', rate=0.0):
        """ Constructor: takes name and the hourly pay rate of worker
        """
        self.name = name
        self.rate = rate

    def changerate(self, newrate):
        """ Takes the new pay rate as input and changes the worker's pay rate to the new hourly rate
        """
        self.rate = newrate

    def pay(self, hours):
        """ Takes the number of hours worked as input and prints 'Not Implemented'
        """
        return 'Not Implemented'


class HourlyWorker(Worker):
    """ inherits class worker; Overloads pay to compute the pay of the worker per hour
    """
    def pay(self, hours):
        """ Takes number of hours worked as input and returns the wage; any hours above 40 are paid double
        """
        if hours > 40:
            return 40 * self.rate + (hours - 40) * self.rate * 2
        return self.rate * hours


class SalariedWorker(Worker):
    """ Inherits class Worker; Overloads pay to compute the wage of the worker on a firm salary
    """
    def pay(self, hours=40):
        """ Returns the pay for 40 hours, regardless of how many hours were actually worked
        """
        return 40 * self.rate

w1 = Worker('Joe', 15)
print(w1.pay(35))

w2 = SalariedWorker('Sue', 14.50)
print(w2.pay())
print(w2.pay(60))

w3 = HourlyWorker('Dana', 20)
print(w3.pay(25))
w3.changerate(35)
print(w3.pay(25))

############
### 8.26 ###
############
print('\nPP 8.26')


class Segment:
    """ Represents a line segment in a Cartesian plane
    """
    def __init__(self, a1=(0, 0), b1=(0, 0)):
        """ Constructor: takes a pair of Point objects that represent the endpoints of the line segment to make line
        """
        self.a = a1
        self.b = b1

    def length(self):
        """ Returns the length of the line segment
        """
        return Point.distance(self.a, self.b)

    def slope(self):
        """ Returns the slope of segment or None of the slope is unbounded
        """
        y3 = self.a.y - self.b.y
        x3 = self.a.x - self.b.x
        if x3 == 0:
            return 'Division by Zero'
        return y3 / x3

p1 = Point(3, 4)
p2 = Point()
s1 = Segment(p1, p2)
print(s1.length())
print(s1.slope())

############
### 8.27 ###
############
print('\nPP 8.27')

import time


class Person:
    """ abstracts a person
    """
    def __init__(self, name='Unknown', age=0):
        """ Constructor: takes a person's name and age and initializes person
        """
        self.n = name
        self.yr = age

    def age(self):
        """ Returns the age of the person
        """
        localtime = time.localtime()
        localyear = eval(time.strftime('%Y', localtime))
        age3 = localyear - self.yr
        return age3

    def name(self):
        """ Returns the name of the person
        """
        return self.n

    def __repr__(self):
        """ Returns
        """
        return '{} is {} years old'.format(self.n, self.age())

john = Person('John', 1990)
print(john.name())
print(john.age())

############
### 8.28 ###
############
print('\nPP 8.28')


class Textfile:
    """ Provides methods to analyze a text file
    """
    def __init__(self, file):
        """ Constructor
        """
        self.infile = open(file, 'r')
        self.content = self.infile.read()
        self.infile.close()
        self.infile = open(file, 'r')
        self.lines = self.infile.readlines()
        self.infile.close()

    def read(self):
        """ Reads and returns text in file
        """
        return self.content

    def readlines(self):
        """ Reads and returns list of lines in file
        """
        return self.lines

    def nchars(self):
        """ Returns the number of characters in file
        """
        return len(self.content)

    def nwords(self):
        """ Returns the number of words in file
        """
        # table = str.maketrans('!,.:;?', 6 * ' ')
        # content = self.content.translate(table)
        wordlst = self.content.split()

        return len(wordlst)

    def nlines(self):
        """ Returns the amount of lines in file
        """
        return len(self.lines)

    def grep(self, s):
        """ Takes a string and prints the lines in which sting s appears
        """
        counter = 0
        for line in self.lines:
            if s in line:
                print('{}: {}'.format(counter, line), end='')

            counter += 1

    def words(self):
        """ returns a list of words in the file with no duplicates
        """
        table = str.maketrans('''1234567890.,,, ;,`()-:!?"\n'[]_''', '                              ')
        content = self.content.translate(table)
        content = content.lower()
        contentlist = content.split()
        contentlistset = list(set(contentlist))
        words = sorted(contentlistset)

        return words

    def occurrences(self):
        """ Returns a dictionary mapping each word in file to the number of times it occurs on the file
        """
        table = str.maketrans('''1234567890.,,, ;,`()-:!?"\n'[]_''', '                              ')
        content = self.content.translate(table)
        content = content.lower()
        contentlist = content.split()
        contentlistset = list(set(contentlist))
        words = sorted(contentlistset)
        wdic = {}

        for word in words:
            counter = 0
            for j in contentlist:
                if word == j:
                    counter += 1
                    wdic[word] = counter

        return wdic

    def average(self):
        """ Returns a tuple with
            1. The average number of words per sentence in the file
            2. Th number of words in the sentence with the most words
            3. The number of words in the sentence with the fewest words
            Delimiters '!?.' are used
        """
        table = str.maketrans('''!?.`-'"\n''', '!!!     ')
        content = self.content.translate(table)
        content = content.split('!')

        words = 0
        sentences = len(content)
        most = 0
        least = 10000000

        for j in content:
            jsplit = j.split()
            words += len(jsplit)
            if len(jsplit) > most:
                most = len(jsplit)
            elif 0 < len(jsplit) < least:
                least = len(jsplit)

        avg = words / sentences

        return avg, most, least

t = Textfile('raven.txt')
print(t.nchars())
print(t.nwords())
print(t.nlines())
print(t.grep('nevermore'))
print(t.read())

############
### 8.29 ###
############
print('\nPP 8.29')

print(t.words())

############
### 8.30 ###
############
print('\nPP 8.30')

print(t.occurrences())

############
### 8.31 ###
############
print('\nPP 8.31')

print(t.average())

############
### 8.32 ###
############
print('\nPP 8.32')


class Hand:
    """ Represents a hand of playing cards
    """
    def __init__(self, pid=''):
        """ Constructor: player ID
        """
        self.id = pid
        self.hand = []

    def add_card(self, card1):
        """ Takes a card and adds it to the hand
        """
        self.hand.append(card1)
        return card1

    def show_hand(self):
        """ Displays player hand
        """
        print('House: ', end=' ')
        for icard in self.hand:
            print(icard.get_rank(), icard.get_suit(), end='   ')

    def total(self):
        """ Takes the hand and returns total value
        """

        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                  '9': 9, '1': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
        result = 0
        num_aces = 0

        for card1 in self.hand:
            result += values[card1.get_rank()[0]]       # add up the values of the cards in the hand
            if card1.get_rank()[0] == 'A':              # also add up the number of aces
                num_aces += 1

        while result > 21 and num_aces > 0:
            result -= 10
            num_aces -= 1
        return result

    def __len__(self):
        return len(self.hand)

hand = Hand('House')
deck = Deck()
deck.shuffle()
hand.add_card(deck.deal_card())
hand.add_card(deck.deal_card())
hand.add_card(deck.deal_card())

hand.show_hand()


############
### 8.33 ###
############
print('\nPP 8.33')

# Answer in "Perkovic_Ch_08_8.33"

############
### 8.34 ###
############
print('\nPP 8.34')


class Date:
    """
    """
    def __init__(self):
        """ Constructor: initializes date
        """
        self.date = time.localtime()

    def display(self, form):
        """ Takes form and returns sting based on form
        """
        intmonth = time.strftime('%m', self.date)
        abrevmonth = time.strftime('%b', self.date)
        intday = time.strftime('%d', self.date)
        intyear = time.strftime('%y', self.date)
        fullyear = time.strftime('%Y', self.date)
        formats = {'MDY': '{}/{}/{}'.format(intmonth, intday, intyear),
                   'MDYY': '{}/{}/{}'.format(intmonth, intday, fullyear),
                   'DMY': '{}/{}/{}'.format(intday, intmonth, intyear),
                   'DMYY': '{}/{}/{}'.format(intday, intmonth, fullyear),
                   'MODY': '{} {}, {}'.format(abrevmonth, intday, fullyear)}

        return formats[form]

x = Date()
print(x.display('MDY'))
print(x.display('MODY'))

############
### 8.35 ###
############
print('\nPP 8.35')

# Answer in "Perkovic_Ch_08_8.35"

############
### 8.36 ###
############
print('\nPP 8.36')


class Pseudorandom:
    """ Generates a sequence of pseudo-random integers using linear congruential generator
    """
    def __init__(self, ap, xp, cp, mp):
        """ Constructor: takes a, x, c, and m and initializes a Pseudo-random object
        """
        self.a = ap
        self.x = xp
        self.c = cp
        self.m = mp
        self.result = (self.a * self.x + self.c) % self.m

    def next(self):
        """ Generates and returns the next number in the Pseudo-random sequence
        """
        firstresult = self.result
        self.x = (self.a * self.x + self.c) % self.m
        self.result = (self.a * self.x + self.c) % self.m
        return firstresult

x = Pseudorandom(17, 12, 7, 31)
print(x.next())
print(x.next())
print(x.next())

############
### 8.37 ###
############
print('\nPP 8.37')


class Stat:
    """ Stores a sequence of numbers and provides stats about the numbers.
        Supports overloaded constructor that initializes container and methods shown
    """
    def __init__(self, nlst=list()):
        """ Constructor: initializes list of numbers
        """
        self.lst = nlst

    def add(self, n):
        """ Adds n to stat
        """
        self.lst.append(n)

    def min(self):
        """ Returns minimum value in container
        """
        return min(self.lst)

    def max(self):
        """ Returns maximum value in container
        """
        return max(self.lst)

    def sum(self):
        """ Return sum of values in container
        """
        return sum(self.lst)

    def mean(self):
        """ Return the average of items on container
        """
        return sum(self.lst) / len(self.lst)

    def clear(self):
        """ Empties the sequence
        """
        self.lst = []

    def __len__(self):
        """ Returns the number of container items without having to
        """
        return len(self.lst)

    def __contains__(self, item):
        """ Returns True if in container
        """
        return item in self.lst


st = Stat()
st.add(2)
st.add(4)
st.add(6)
st.add(8)

print(st.min())
print(st.max())
print(st.sum())
print(len(st))
print(st.mean())
print(4 in st)
st.clear()

############
### 8.38 ###
############
print('\nPP 8.38')


class Stack(object):
    """ A container that support very restrictive access methods:
        All insertions and removals are from one end of the stack.
    """

    def __init__(self, stack=list()):
        """ Constructor: create stack
        """
        self.stack = stack

    def push(self, other):
        """ Takes an item as input and pushes it on top of the stack
        """
        self.stack.append(other)

    def pop(self):
        """ Remove and return the item at the top of the stack
        """
        return self.stack.pop()

    def isempty(self):
        """ Return True if the stack is empty, false otherwise
        """
        return self.stack == [] or self.stack is None

    def __len__(self):
        """ Returns length of stack
        """
        return len(self.stack)

    def __repr__(self):
        return '{}'.format(self.stack)

stk = Stack()
stk.push('plate 1')
stk.push('plate 2')
stk.push('plate 3')

print(stk)
print(len(stk))
print(stk.pop())
print(stk.pop())
print(stk.pop())
print(stk.isempty())

############
### 8.39 ###
############
print('\nPP 8.39')


class PriorityQueue:
    """
    """

    def __init__(self, pqueue=list()):
        """
        """
        self.pq = pqueue

    def insert(self, other):
        """ Takes a number as input and adds it to the container
        """
        self.pq.append(other)

    def min(self):
        """ Returns the smallest number in the container
        """
        return min(self.pq)

    def removemin(self):
        """ Removes the smallest number in the container
        """
        self.pq.remove(min(self.pq))

    def isempty(self):
        """ Returns True if container is empty
        """
        return self.pq == [] or self.pq is None

    def __len__(self):
        """ Returns number of objects in pq
        """
        return len(self.pq)

pq = PriorityQueue()
pq.insert(3)
pq.insert(1)
pq.insert(5)
pq.insert(2)

print(pq.min())
pq.removemin()
print(pq.min())
print(len(pq))
print(pq.isempty())

############
### 8.40 ###
############
print('\nPP 8.40')


class Square(Polygon):
    """ Abstracts a square using class polygon
    """

    def __init__(self, sl=0):
        """ Initialize square with width and length 0, 0
        """
        self.sl = sl
        Polygon.__init__(self, 4, sl)

    def area(self):
        """ Returns area of square
        """
        return self.sl ** 2


class Triangle(Polygon):
    """ Abstracts a triangle using class polygon
    """

    def __init__(self, sl=0):
        """ Initalize triangle with width and length 0, 0
        """
        self.sl = sl
        Polygon.__init__(self, 3, sl)

    def area(self):
        """ Returns area of triangle
        """
        return (math.sqrt(3) / 4) * self.sl ** 2

sq = Square(2)
print(sq.perimeter())
print(sq.area())

tr = Triangle(3)
print(tr.perimeter())
print(tr.area())

############
### 8.41 ###
############
print('\nPP 8.41')


class Mammal(Animal):
    """ Inherits Animal class
    """


class Cat(Mammal):
    """ Inherits Mammal class as Cat
    """

    def speak(self):
        """ Has Cat say "Meeow"
        """
        return 'Meeow'


class Dog(Mammal):
    """ Inherits Mammal class as Dog
    """

    def speak(self):
        """ Has Dogs say "Barrk"
        """
        return 'Barrk'


class Primate(Mammal):
    """ Inherits Mammal class as Primate
    """

    def speak(self):
        """ Has Primate say "Eeeek"
        """
        return 'Eeeek'


class Hacker(Primate):
    """ Inherits Primate class as Hacker
    """

    def speak(self):
        """ Has Hacker say "Hello World"
        """
        return 'Hello world!'

garfield = Cat()
print(garfield.speak())

sputnik = Dog()
print(sputnik.speak())

chimp = Primate()
print(chimp.speak())

dude = Hacker()
print(dude.speak())

############
### 8.42 ###
############
print('\nPP 8.42')


class Instructor(Person):
    """ Inherits Person class as Instructor
    """

    def __init__(self, name='Unknown', age=0, degree='Unknown'):
        """ Constructor: Takes name, age, and degree and initializes instructor
        """
        Person.__init__(self, name, age)
        self.deg = degree

    def degree(self):
        """ Returns the degree of the instructor
        """
        return self.deg


class Student(Person):
    """ Inherits Person class as Student
    """
    def __init__(self, name='Unknown', age=0, major='Unknown'):
        """ Constructor: Takes name, age, and major and initializes student
        """
        Person.__init__(self, name, age)
        self.maj = major

    def major(self):
        """ Returns the major of student
        """
        return self.maj


inst = Instructor('Smith', 1963, 'PhD')
print(inst.age())

stud = Student('Jones', 1987, 'Computer Science')
print(stud.age())

print(stud.major())
print(inst.degree())

############
### 8.43 ###
############
print('\nPP 8.43')

# bnk = BankAccount(-700)

# bnk = BankAccount()
# bnk.withdraw(2)

# bnk = BankAccount(200)
# bnk.deposit(-100)

############
### 8.44 ###
############
print('\nPP 8.44')