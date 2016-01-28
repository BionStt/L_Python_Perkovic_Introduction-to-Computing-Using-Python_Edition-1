import turtle

__author__ = 'Rolando'

####################################
### Perkovic Intro to Python     ###
#### CH 2: Python Data types    ####
##### PG 41 CH 2               #####
####################################


s = turtle.Screen()

t = turtle.Turtle()
t.forward(100)
t.left(90)

u = turtle.Turtle()
u.left(90)
u.forward(100)
t.forward(100)
u.right(45)
s.bye()

''' REFERENCE
    t.forward(distance) = Move turtle in the direction the turtle is headed by distance pixels
    t.left(angle) = Rotate turtle counterclockwise by angle degrees
    t.right(angle) = Rotate turtle clockwise by angle degrees
    t.undo() = Undo the previous move
    t.goto(x, y) = Move turtle to coordinates defined by x and y; if pen is down, draw line
    t.setx(x) = Set the turtle's first coordinate to x
    t.sety(y) = Set the turtle's second coordinate to y
    t.setheading(angle) = Set orientation of turtle angle, given in degrees; angle 0 means east, 90 is north, and so on
    t.circle(radius) = Draw a circle with the given radius; the center of the circle is radius pixels to the left of
                       the turtle
    t.circle(radius, angle) = Draw only the part of the circle (see above) corresponding to angle
    t.dot(diameter, color) = Draw a dot with given diameter and color
    t.penup() = Pull pen up; no drawing when moving
    t.pendown() = Put pen down; drawing when moving
    t.pensize(width) = Set the line thickness to width
    t.pencolor(color) = Set the pen color to the color described by string color


    s.bgcolor(color) = Changes the background color of screen s to color described by string color
    s.clearscreen() = Clears screen s
    s.turtles() = Returns a list of all turtles in the screen s
    s.bye() = Close the screen s window
'''

s = turtle.Screen()
t = turtle.Turtle()
t.pensize(3)
x = -100
y = 100
t.goto(x, y)

# oops
t.undo()
t.penup()
t.goto(x, y)
t.pendown()

# head
t.circle(100)

# lef eye
t.penup()
t.goto(x - 35, y + 120)
t.pendown()
t.dot(25)

# right eye
t.penup()
t.goto(x + 35, y + 120)
t.pendown()
t.dot(25)

# smile
t.penup()
t.goto(x - 60.62, y + 65)
t.pendown()
t.setheading(-60)
t.circle(60, 120)

# close
s.bye()

############
### 2.11 ###
############
print('\nPP 2.11')

# Make pen a turtle
s = turtle.Screen()
t = turtle.Turtle(shape='turtle')
t.penup()
t.goto(-300, 0)
t.pendown()

# Circle on left 300, 0
t.pensize(2)
t.circle(50)

# Waves
t.penup()
t.goto(-400, -200)
t.pendown()
t.right(45)
for wave in range(9):
    t.circle(50, 90)
    t.right(90)

# put turtle under waves
t.penup()
t.goto(-100, -300)
t.left(90)

s.bye()

############
### 2.26 ###
############
print('\nPP 2.26')

# Square
s = turtle.Screen()
t = turtle.Turtle()
for square in range(4):
    t.forward(100)
    t.left(90)

s.bye()

############
### 2.27 ###
############
print('\nPP 2.27')

# Diamond
s = turtle.Screen()
t = turtle.Turtle()
t.left(45)
for diamond in range(4):
    t.forward(100)
    t.left(90)

s.bye()

############
### 2.28 ###
############
print('\nPP 2.28')

# Pentagon
s = turtle.Screen()
t = turtle.Turtle()
for pentagon in range(5):
    t.forward(100)
    t.left(360 / 5)

s.bye()

# Hexagon
s = turtle.Screen()
t = turtle.Turtle()
for hexagon in range(6):
    t.forward(100)
    t.left(360 / 6)

s.bye()

# Heptagon
s = turtle.Screen()
t = turtle.Turtle()
for heptagon in range(7):
    t.forward(100)
    t.left(360 / 7)

s.bye()

# Octagon
s = turtle.Screen()
t = turtle.Turtle()
for octagon in range(8):
    t.forward(100)
    t.left(360 / 8)

s.bye()

############
### 2.29 ###
############
print('\nPP 2.29')

# 3 intersecting circles
s = turtle.Screen()
t = turtle.Turtle()
t.left(90)
for circles in range(3):
    t.left(360 / 3)
    t.circle(100)
    t.penup()
    t.forward(100)
    t.pendown()

s.bye()

############
### 2.30 ###
############
print('\nPP 2.30')

# Dartboard
s = turtle.Screen()
t = turtle.Turtle()
size = 0
for dartboard in range(4):
    size += 50
    t.circle(size)
    t.penup()
    t.right(90)
    t.forward(50)
    t.left(90)
    t.pendown()

s.bye()

############
### 2.31 ###
############
print('\nPP 2.31')

# Make 3 pens a turtle
s = turtle.Screen()
t = turtle.Turtle(shape='turtle')
u = turtle.Turtle(shape='turtle')
v = turtle.Turtle(shape='turtle')

t.penup()
t.goto(-300, 0)
t.pendown()

# Sun
t.pensize(2)
t.circle(50)

# Waves
t.penup()
t.goto(-400, -200)
t.pendown()
t.right(45)
for wave1 in range(9):
    t.circle(50, 90)
    t.right(90)

# put turtle t under waves
t.penup()
t.goto(-100, -300)
t.left(90)

# put turtle u under waves
u.penup()
u.goto(-200, -300)
u.left(45)

# put turtle v under waves
v.penup()
v.goto(0, -300)
v.left(45)

s.bye()
############
### 2.32 ###
############
print('\nPP 2.32')

s = turtle.Screen()
t = turtle.Turtle()

# Earth
t.circle(1)
# Sun
t.penup()
t.left(180)
t.forward(120)
t.left(180)
t.pendown()
t.circle(109)

s.bye()

####################################
### 2.33 NEED TO DO 6 POINT STAR ###
####################################
print('\nPP 2.33')

# 5 point star
s = turtle.Screen()
t = turtle.Turtle()

for star5 in range(5):
    t.forward(100)
    t.right(144)

s.bye()

# 6 point star
s = turtle.Screen()
t = turtle.Turtle()

for star6 in range(6):
    t.forward(100)
    t.right(155)
s.bye()

############
### 2.34 ###
############
print('\nPP 2.34')

# Side 1
s = turtle.Screen()
t = turtle.Turtle()

for dice1 in range(4):
    t.forward(100)
    t.left(90)

# Dot 1-1
t.penup()
t.goto(50, 50)
t.pendown()
t.dot(10)

s.bye()

# Side 2
s = turtle.Screen()
t = turtle.Turtle()

for dice2 in range(4):
    t.forward(100)
    t.left(90)

# Dot 2-1
t.penup()
t.goto(25, 75)
t.pendown()
t.dot(15)

# Dot 2-2
t.penup()
t.goto(75, 25)
t.pendown()
t.dot(15)

s.bye()

# Side 3
s = turtle.Screen()
t = turtle.Turtle()

for side3 in range(4):
    t.forward(100)
    t.left(90)

# Dot 3-1
t.penup()
t.goto(25, 75)
t.pendown()
t.dot(15)

# Dot 3-2
t.penup()
t.goto(50, 50)
t.pendown()
t.dot(15)

# Dot 3-3
t.penup()
t.goto(75, 25)
t.pendown()
t.dot(15)

s.bye()

# Side 4
s = turtle.Screen()
t = turtle.Turtle()

for side4 in range(4):
    t.forward(100)
    t.left(90)

# Dot 4-1
t.penup()
t.goto(25, 75)
t.pendown()
t.dot(15)

# Dot 4-2
t.penup()
t.goto(75, 75)
t.pendown()
t.dot(15)

# Dot 4-3
t.penup()
t.goto(25, 25)
t.pendown()
t.dot(15)

# Dot 4-4
t.penup()
t.goto(75, 25)
t.pendown()
t.dot(15)

s.bye()
# Side 5
s = turtle.Screen()
t = turtle.Turtle()

for side5 in range(4):
    t.forward(100)
    t.left(90)

# Dot 5-1
t.penup()
t.goto(25, 75)
t.pendown()
t.dot(15)

# Dot 5-2
t.penup()
t.goto(75, 75)
t.pendown()
t.dot(15)

# Dot 5-3
t.penup()
t.goto(25, 25)
t.pendown()
t.dot(15)

# Dot 5-4
t.penup()
t.goto(75, 25)
t.pendown()
t.dot(15)

# Dot 5-5
t.penup()
t.goto(50, 50)
t.pendown()
t.dot(15)

s.bye()

# Side 6
s = turtle.Screen()
t = turtle.Turtle()

for side6 in range(4):
    t.forward(100)
    t.left(90)

# Dot 6-1
t.penup()
t.goto(25, 75)
t.pendown()
t.dot(15)

# Dot 6-2
t.penup()
t.goto(75, 75)
t.pendown()
t.dot(15)

# Dot 6-3
t.penup()
t.goto(25, 25)
t.pendown()
t.dot(15)

# Dot 6-4
t.penup()
t.goto(75, 25)
t.pendown()
t.dot(15)

# Dot 6-5
t.penup()
t.goto(25, 50)
t.pendown()
t.dot(15)

# Dot 6-6
t.penup()
t.goto(75, 50)
t.pendown()
t.dot(15)

s.bye()

############
### 2.35 ###
############
print('\nPP 2.35')

# NBA field
s = turtle.Screen()
t = turtle.Turtle()

# Outer Rectangle
t.penup()
t.goto(-235, 0)
t.pendown()

for NBA1 in range(2):
    t.forward(94 * 5)
    t.left(90)
    t.forward(50 * 5)
    t.left(90)

# Middle Line
t.left(90)
t.penup()
t.goto(0, 0)
t.pendown()
t.forward(50 * 5)

# Middle Inner Circle
t.penup()
t.goto(10, 125)
t.pendown()
t.circle(2 * 5)

# Middle Outer Circle
t.penup()
t.goto(30, 125)
t.pendown()
t.circle(30)

# Left Court Half-ring
t.penup()
t.goto(-235, 15)
t.pendown()
t.right(90)
t.forward(14 * 5)
t.circle(110, 180)
t.forward(14 * 5)
t.left(180)

# Left Outer Court Box
t.penup()
t.goto(-235, 85)
t.pendown()
t.forward(19 * 5)
t.left(90)
t.forward(16 * 5)
t.left(90)
t.forward(19 * 5)
t.left(180)

# Left Court Inner Box
t.penup()
t.goto(-235, 95)
t.pendown()
t.forward(19 * 5)
t.left(90)
t.forward(12 * 5)
t.left(90)
t.forward(19 * 5)
t.left(180)

# Left Court Ring
t.penup()
t.goto(-140, 95)
t.pendown()
t.circle(30)
t.left(180)

# Right Court Half-ring
t.penup()
t.goto(235, 235)
t.pendown()
t.forward(14 * 5)
t.circle(110, 180)
t.forward(14 * 5)
t.left(180)

# Right Court Outer Box
t.penup()
t.goto(235, 85)
t.pendown()
t.forward(19 * 5)
t.right(90)
t.forward(16 * 5)
t.right(90)
t.forward(19 * 5)
t.left(180)

# Right Court Outer Box
t.penup()
t.goto(235, 95)
t.pendown()
t.forward(19 * 5)
t.right(90)
t.forward(12 * 5)
t.right(90)
t.forward(19 * 5)
t.right(180)

# Right Court Small Ring

t.penup()
t.goto(140, 155)
t.pendown()
t.circle(30)

s.bye()

############
### 2.36 ###
############
print('\nPP 2.36')

# Moon Phases

# Waxing Crescent
s = turtle.Screen()
t = turtle.Turtle()

t.circle(100, 180)
t.right(50)
t.circle(155, -81)

s.bye()

# First Quarter
s = turtle.Screen()
t = turtle.Turtle()

t.circle(100, 180)
t.left(90)
t.forward(200)

s.bye()

# Waxing Gibbous
s = turtle.Screen()
t = turtle.Turtle()

t.circle(100, 180)
t.left(50)
t.circle(155, 81)
s.bye()

# Full
s = turtle.Screen()
t = turtle.Turtle()

t.circle(100)

s.bye()

# Waning Gibbous
s = turtle.Screen()
t = turtle.Turtle()

t.circle(100, -180)
t.right(50)
t.circle(155, -81)

s.bye()

# Third Quarter
s = turtle.Screen()
t = turtle.Turtle()

t.circle(100, -180)
t.left(90)
t.forward(200)

s.bye()

# Waning Crescent
s = turtle.Screen()
t = turtle.Turtle()

t.circle(100, -180)
t.left(50)
t.circle(155, 81)
