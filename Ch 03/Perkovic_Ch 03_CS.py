__author__ = 'Rolando'
#######################################
### Perkovic Intro to Python        ###
#### CH 3: Imperative Programming  ####
##### PG 82 CH 3 Case Study       #####
#######################################

import turtle


def jump(w, x, y):
    """
    :param w: turtle
    :param x: x coordinate
    :param y: y coordinate
    :return: makes turtle t jump to coordinates (x, y)
    """

    w.penup()
    w.goto(x, y)
    w.pendown()


def emoticon(w, x, y):
    """
    :param w: turtle
    :param x: x coordinate
    :param y: y coordinate
    :return: turtle t draws a smiley face at coordinate (x, y)
    """

    # Set turtle direction and oen size
    w.pensize(3)
    w.setheading(0)

    # Move to (x, y) and draw head
    jump(w, x, y)
    w.circle(100)

    # Draw right eye
    jump(w, x + 35, y + 120)
    w.dot(25)

    # Draw left eye
    jump(w, x - 45, y + 120)
    w.dot(25)

    # Draw Smile
    jump(w, x - 60.62, y + 65)
    t.setheading(-60)           # Smile is 120 degree
    t.circle(70, 120)           # Section of a circle

s = turtle.Screen()
t = turtle.Turtle()

print(emoticon(t, -100, 100))
print(emoticon(t, 150, 100))

s.bye()

############
### 3.15 ###
############
print('\nPP 3.15')


def olympic(w):
    """
    :param w: turtle
    :return: 5 Olympic rings
    """

    w.pensize(2)

    jump(w, -220, 0)
    w.circle(100)

    jump(w, -110, -100)
    w.circle(100)

    jump(w, 0, 0)
    w.circle(100)

    jump(w, 110, -100)
    w.circle(100)

    jump(w, 220, 0)
    w.circle(100)

s = turtle.Screen()
t = turtle.Turtle()

print(olympic(t))

s.bye()

############
### 3.44 ###
############
print('\nPP 3.44')


def polygon(n):
    """
    :param n: number of sides in the polygon
    :return:  Polygon with n sides
    """
    s1 = turtle.Screen()
    t1 = turtle.Turtle()

    jump(t1, -50, 0)
    for side in range(n):
        t1.forward(100)
        t1.left(360 / n)

    s1.bye()

print(polygon(4))
print(polygon(7))

############
### 3.45 ###
############
print('\nPP 3.45')


def planets():
    """
    :return: rotation of Mercury, Venus, Earth, and Mars from sun
    """
    s1 = turtle.Screen()
    Me = turtle.Turtle()
    Ve = turtle.Turtle()
    Ea = turtle.Turtle()
    Ma = turtle.Turtle()

    jump(Me, 0, -58)
    jump(Ve, 0, -108)
    jump(Ea, 0, -150)
    jump(Ma, 0, -228)

    Me.circle(158, 360 * 7.5)
    Ve.circle(208, 360 * 3)
    Ea.circle(250, 360 * 2)
    Ma.circle(328, 350)

    s1.bye()

print(planets())