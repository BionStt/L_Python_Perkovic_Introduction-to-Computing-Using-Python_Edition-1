__author__ = 'Rolando'
#############################################
### Perkovic Intro to Python              ###
#### CH 7: Namespaces                    ####
##### PG 215 CH 7                       #####
#############################################

#############
### NOTES ###
#############
# import turtle

''' REFERENCE
    Code Reuse - a fragment of code that is used multiple times in a program cna be packages in a function
    Modularity - the complexity of developing a large program can be dealt with by breaking it into smaller and simpler
                 self-contained pieces. Each smaller piece can be designed, implemented, tested, and debugged
                 independently
    Encapsulation - Hiding details of program in a function for cleaner code
    Local Variables - Variable in a function can only be called from within the running function

'''


def jump(w, x, y):
    """
    :param w: turtle
    :param x: x coordinate
    :param y: y coordinate
    :return:  makes turtle w jump to coordinates (x, y)
    """
    w.penup()
    w.goto(x, y)
    w.pendown()


def emoticon(w, x, y):
    """
    :param w: turtle
    :param x: x coordinate
    :param y: y coordinate
    :return: directs turtle t to draw a smiley fave with chin a (x, y)
    """
    w.pensize(3)            # set pensize
    w.setheading(0)         # set heading

    jump(w, x, y)           # Draw head (and set position)
    w.circle(100)

    jump(w, x + 35, y + 120)    # Right eye
    w.dot(25)

    jump(w, x - 35, y + 120)    # Left eye
    w.dot(25)

    jump(w, x - 60.62, y + 65)  # Smile
    w.setheading(-60)
    w.circle(70, 120)

# s = turtle.Screen()
# t = turtle.Turtle()
#
# print(emoticon(t, 0, 0))
#
# s.bye()
#
#
# def double(y):
#     x = 2
#     print('x = {}, y = {}'.format(x, y))
#
# print(double(3))
#
# # Stack
#
#
# def h(n):
#     print('Start h')
#     print((1 / n))
#     print(n)
#
#
# def g(n):
#     print('Start g')
#     h(n - 1)
#     print(n)
#
#
# def f(n):
#     print('Start f')
#     g(n - 1)
#     print(n)
#
# try:
#     print(f(4))
#     print(f(2))
# except:
#     print('Caught Division by Zero')
#
# # Scope 1
#
#
# def f(b):                           # f has global scope, b has local scope
#     a = 6                           # this a has scope local to function call f()
#     return a * b                    # this is the local a
#
# a = 0                               # this a has global scope
# print(('f(3) = {}'.format(f(3))))
# print('a is {}'.format(a))          # global a is still 0
#
# # Scope 2
#
#
# def f2(b):
#     return a * b
#
# a = 0
# print('f2(3) = {}'.format(f(3)))
# print('a is {}'.format(a))
#
# # Scope 3
#
#
# def f3(b):
#     global a                        # all references to a in f() are to the global a
#     a = 6                           # global a is changed
#     return a * b                    # this a is the global a
#
# a = 0                               # this a has global scope
# print('f(3) = {}'.format(f(3)))
# print('a is {}'.format(a))          # global a has been changed to 6
#
# # Exceptional Control Flow
#
# # Age 1
#
#
# strAge = input('Enter your age: ')
# intAge = int(strAge)
# print('You are {} years old.'.format(intAge))
#
# # Age 2
#
#
# try:
#     # try block - executed first; if exception is raised, the execution of the try block is interrupted
#     strAge = input('Enter your age: ')
#     intAge = int(strAge)
#     print('You are {} years old.'.format(intAge))
# except:
#     # except block executed only if an exception is raised while executing the try block
#     print('Enter your age using digits 0-9!')
#
# # Age 3
#
#
# try:
#     # try block
#     strAge = input('Enter your age: ')
#     intAge = int(strAge)
#     print('You are {} years old.'.format(intAge))
# except ValueError:
#     # except block --- executed only if a ValueError
#     # exception is raised in the try block
#     print('Enter your age using digits 0-9!')


def readage(filename):
    """
    :param filename: file
    :return: converts first line of file filename to in integer and print it'''
    """
    try:
        infile = open(filename)
        strage = infile.readline()
        age = int(strage)
        print('age is', age)
    except IOError:
        # executed only if IOError exception is raised
        print('Input/Output error')
    except ValueError:
        # executed only of a ValueError exception is raised
        print('Value cannot be converted to integer')
    except:
        # executed if an exception other than IOError ir ValueError is raised
        print('Other Error')

print(readage('agg.txt'))
print(readage('age.txt'))

print('My name is {}'.format(__name__))

import os
path = os.getcwd()

import sys
print(sys.path)

sys.path.append(path)

# from example import f
#
# print(f())
###########
### 7.1 ###
###########
print('\nPP 7.1')


# def f(y):
#     x = 2
#     print('In f(): x = {}, y = {}'.format(x, y))
#     g(3)
#     print('In f(): x = {}, y = {}'.format(x, y))
#
#
# def g(y):
#     x = 4
#     print('In g(): x = {}, y = {}'.format(x, y))
#
# print(f(1))

###########
### 7.2 ###
###########
print('\nPP 7.2')


# def f(y):             # f is global, y i local to f()
#     x = 2             # x iis local to f()
#     return g(x)       # g is global, x is local to f()
#
#
# def g(y):             # g is global, y is local to g()
#     global x          # x is global
#     x = 4             # x is global
#     return x * y      # x is global, y is global to g()
#
#
# x = 0                 # x is global
# res = f(x)            # res, f, and x are global
# print('x = {}, f(0) = {}'.format(x, res))

###########
### 7.3 ###
###########
print('\nPP 7.3')


def safeopen(file, mode):
    """
    :return:
    """
    try:
        infile = open(file, mode)
        return infile
    except:
        return 'File does not exist in current directory'

print(safeopen('ch7.py', 'r'))
print(safeopen('ch7.px', 'r'))

###########
### 7.4 ###
###########
# print('\nPP 7.4')
#
#
# def h(n):                       # Ex: if exception wraps print(1 / 2) line in h(),
#     print('Start h')            # h is terminated at error, but f() and g() resume
#     print(1 / n)                # A: if exception wraps print(1 / 0) line in h(),
#     print(n)                    # line print(1 / 0) does not execute, but the rest of g() and f() are executed
#
#
# def g(n):                       # B: if exception wraps of g() inside g
#     print('Start g')            # end statements of g() and h() are not executed, rest of f() is executed
#     h(n - 1)                    # C: if exception wraps line h(n - 1) in g,
#     print(n)                    # h is terminated at error but rest of g() and f() are executed
#
#
# def f(n):
#     print('Start f')
#     g(n - 1)
#     print(n)
#
#
# try:
#     f(2)
#
# except:                         # if wraps f(), f() will terminate at error and not finish
#     print('Caught!')
#

###########
### 7.5 ###
###########
print('\nPP 7.5')


import random
print(dir(random))

#########################
### 7.6 in example.py ###
#########################


#################################
### 7.7 does not ask for code ###
#################################

###########
### 7.8 ###
###########


# # probA
# # in probA, function f() is called before it is defined, so NameError occurs

# print(f(3))
# def f(x):
#     return 2*x+1


# # probB
# # probB does not have this issue because although f() is not defined when g() is created, it is defined when g() is
# # run

# def g(x):
#     print(f(x))
#
# def f(x):
#     return 2*x+1
#
# g(3)

#################################
### 7.9 does not ask for code ###
#################################

##################################
### 7.10 does not ask for code ###
##################################

############
### 7.11 ###
############

# if one is not run, the namespace for two is not created. therefore, two must me imported separately, or one must be
# run for two to have a namespace
