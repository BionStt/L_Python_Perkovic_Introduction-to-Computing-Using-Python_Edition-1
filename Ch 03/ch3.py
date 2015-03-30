def f(x):
    """returns x**2 + 1"""
    return x**2+1   # compute x**2 + 1 and return obtained value


def hello(name):
    """a personalized hello function"""
    print('Hello, ' + name + '!')


def g(x):
    x = 5


def h(lst):
    lst[0] = 5


##################################
# Solutions to Practice Problems #
##################################


def average(x, y):
    """returns average of x and y"""
    return (x + y) / 2


def perimeter(radius):
    """returns perimeter of circle of given radius"""
    import math
    return 2 * math.pi * radius


def negatives(lst):
    """prints the negative numbers in list lst"""
    for i in lst:
        if i < 0:
            print(i)


def swapfl(lst):
    """swaps first and last item in list lst"""
    lst[0], lst[-1] = lst[-1], lst[0]


def olympic(t):
    """has turtle t draw the olympic rings"""
    import turtlefunctions
    t.pensize(3)
    turtlefunctions.jump(t, 0, 0)   # bottom of top center circle
    t.setheading(0)

    t.circle(100)  # top center circle
    turtlefunctions.jump(t, -220, 0)
    t.circle(100)  # top left circle
    turtlefunctions.jump(t, 220, 0)
    t.circle(100)  # top right circle
    turtlefunctions.jump(t, 110, -100)
    t.circle(100)  # bottom right circle
    turtlefunctions.jump(t, -110, -100)
    t.circle(100)  # bottom left circle
