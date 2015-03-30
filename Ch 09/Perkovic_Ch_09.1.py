__author__ = 'Rolando'
#############################################
### Perkovic Intro to Python              ###
#### CH 9: Graphical User Interfaces     ####
##### PG 309 CH 9                       #####
#############################################

from tkinter import Tk, Label, Button, Entry, PhotoImage, Text, TOP, BOTTOM, LEFT, RIGHT, RIDGE, BOTH, RAISED, END

from tkinter.messagebox import showinfo

root = Tk()
root.mainloop()                                             # Make window


root = Tk()
hello = Label(master=root, text='Hello GUI world!')
hello.pack()
root.mainloop()


root = Tk()
# transform GIF image to format tkinter can display
photo = PhotoImage(file='peace.gif')
peace = Label(master=root,
              image=photo,
              width=300,
              height=180)
peace.pack()
root.mainloop()


root = Tk()
# label with text "Peace begins with a smile
text = Label(root,
             font=('Helvetica', 16, 'bold italic'),
             foreground='white',                        # letter color
             background='black',                        # background color
             padx=25,                                   # widen label 25 pixels left and right
             pady=10,                                   # widen label 10 pixels up and down
             text='Peace begins with a smile.')
text.pack(side=BOTTOM)
# label with peace symbol image
peace = PhotoImage(file='peace.gif')
peaceLabel = Label(root,
                   borderwidth=3,                       # label border width
                   relief=RIDGE,                        # label border style
                   image=peace)
peaceLabel.pack(side=LEFT)                              # push label left
# label with smiley face image
smiley = PhotoImage(file='smiley.gif')
smileyLabel = Label(root,
                    image=smiley)
smileyLabel.pack(side=RIGHT)                            # push label right
root.mainloop()


root = Tk()
labels = [['1', '2', '3'],                      # phone dial label texts
          ['4', '5', '6'],                      # organized in a grid
          ['7', '8', '9'],
          ['*', '0', '#']]

for r in range(4):                              # for every row r = 0, 1, 2, 3
    for c in range(3):                          # for every row c = 0, 1, 2
        # create label for row r and column c
        label = Label(root,
                      relief=RAISED,            # raised border
                      padx=10,                  # make label wide
                      text=labels[r][c])        # label text
        # place label in row r and column c
        label.grid(row=r, column=c)

root.mainloop()


from time import strftime, strptime,  localtime, gmtime


# def clicked():
#     """ prints day and time info
#     """
#     time = strftime('Day:  %d %b %Y\nTime: %H:%M:%S %p\n',
#                     localtime())
#     print(time)
#
# root = Tk()

def clicked():
    """ Prints day and time info in GUI box
    """
    time = strftime('Day:  %d %b %Y\nTime: %H:%M:%S %p\n',
                    localtime())
    showinfo(message=time)

root = Tk()

# create button labeled 'Click it' and event handler clicked()
button = Button(root,
                text='Click it',    # text on top of button
                command=clicked)    # button click event handler
button.pack()
root.mainloop()


def compute():
    """ Display day of the week corresponding to date in dateEnt;
        date must have format MMM DD, YYYY (e.g., Jan 21, 1967)
    """
    global dateEnt      # dateEnt is a global variable

    # read date from entry dateEnt
    date = dateEnt.get()

    # compute weekday corresponding to date
    weekday = strftime('%A', strptime(date, '%b %d, %Y'))

    # display the weekday in a pop-up window
    showinfo(message='{} was a {}'.format(date, weekday))

    # delete date from entry dateEnt
    dateEnt.delete(0, END)

root = Tk()

# label
label = Label(root, text='Enter date')
label.grid(row=0, column=0)

# entry
dateEnt = Entry(root)
dateEnt.grid(row=0, column=1)

# button
button = Button(root, text='Enter', command=compute)
button.grid(row=1, column=0, columnspan=2)

root.mainloop()


def record(event):
    """ Event handling function for key press event;
        input event is of type tkinter.Event
    """
    print('char = {}'.format(event.keysym))     # print key symbol

root = Tk()

text = Text(root,
            width=20,
            height=5)

# Bind a key press event with the event handling function record()
text.bind('<KeyPress>', record)

# widget expands if the master does
text.pack(expand=True, fill=BOTH)

root.mainloop()

# draw.py

from tkinter import Canvas

# event handlers begin and draw here


def begin(event):
    """ Initiate the start of the curve to mouse position
    """

    global oldx, oldy
    oldx, oldy = event.x, event.y


def draw(event):
    """ Draws a line segment from old mouse position to new one
    """
    global oldx, oldy, canvas       # oldx and oldy will be modified
    newx, newy = event.x, event.y   # new mouse position

    # connect previous mouse position to current one
    canvas.create_line(oldx, oldy, newx, newy)

    oldx, oldy = newx, newy


root = Tk()

oldx, oldy = 0, 0           # mouse coordinates (global variables)

# canvas
canvas = Canvas(root, height=100, width=150)

# bind left mouse button click event to function begin()
canvas.bind("<Button-1>", begin)

# bind mouse motion while pressing left button event
canvas.bind("<Button1-Motion>", draw)

canvas.pack()
root.mainloop()


###########
### 9.1 ###
###########
print('\nPP 9.1')

root = Tk()

text = Label(root,
             font=('Helvetica', 18, 'bold italic'),
             foreground='white',
             background='black',
             width=20,
             height=5,
             text='Peace & Love')
text.pack(side=LEFT)

peace = PhotoImage(file='peace.gif')
peaceLabel = Label(root,
                   image=peace)
peaceLabel.pack(side=RIGHT,
                fill=BOTH,
                expand=True)
root.mainloop()

###########
### 9.2 ###
###########
print('\nPP 9.2')

from calendar import monthrange


def cal(year, month):
    """ Starts up a GUI window that shows the corresponding calendar
    """

    root1 = Tk()

    weekday, numdays = monthrange(year, month)

    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    # create and place weekday labels
    for i in range(7):
        label1 = Label(root1,
                       text=days[i])
        label1.grid(row=0,
                    column=i)

    # create a calendar starting with week (row) 1 and day (column) 1
    week = 1
    for i in range(1, numdays + 1):     # for i = 1, 2, ... numDays
        # create label i and place it in row week, column weekday
        label1 = Label(root1,
                       text=str(i))
        label1.grid(row=week,
                    column=weekday)

        # update weekday (column) and week (row)
        weekday += 1
        if weekday > 6:
            week += 1
            weekday = 0

    root1.mainloop()

print(cal(2015, 1))


###########
### 9.3 ###
###########
print('\nPP 9.3')


def clickedlocal():
    """ Prints local day and time info in GUI
    """
    time = strftime('Day: %d %b %Y\nTime: %H:%M:%S %p %Z\n',
                    localtime())
    showinfo(message=time)


def clickedgmt():
    """ Print greenwich day and time info on GUI
    """
    time = strftime('Day: %d %b %Y\nTime: %H:%M:%S %p Greenwich Mean Time\n',
                    gmtime())
    showinfo(message=time)

root = Tk()

buttonlc = Button(root,
                  text='   Local Time    ',
                  command=clickedlocal)

buttongw = Button(root,
                  text='Greewich Time',
                  command=clickedgmt)

buttonlc.pack(side=TOP)
buttongw.pack(side=TOP)
root.mainloop()

#################
### 9.4 + 9.5 ###
#################
print('\nPP 9.4 + 9.5')


def compute2():
    """ Display day of the week corresponding to date in dateEnt;
        date must have format MMM DD, YYYY
    """

    global dateEnt      # dateEnt is a global variable

    # read date from entry dateEnt
    date = dateEnt.get()

    # compute weekday corresponding to date
    weekday = strftime('%A', strptime(date, '%b %d, %Y'))

    # display the weekday in a pop-up window
    showinfo(message='{} was a {}'.format(date, weekday))


def clear2():
    """ Clears entry dateEnt
    """
    global dateEnt
    dateEnt.delete(0, END)


def compute3(event):
    compute2()


root = Tk()

# label
label = Label(root, text='Enter date')
label.grid(row=0, column=0)

# entry
dateEnt = Entry(root)
dateEnt.grid(row=0, column=1)

# Enter key command
dateEnt.bind('<Return>', compute3)

# Enter button
button = Button(root, text='Enter', command=compute2)
button.grid(row=1, column=0)

# Clear button
button = Button(root, text='Clear', command=clear2)
button.grid(row=1, column=1)

root.mainloop()

###########
### 9.6 ###
###########
print('\nPP 9.6')


def begin2(event):
    """ Initializes the start of the curve to mouse position
    """

    global oldx2, oldy2, curve
    oldx2, oldy2 = event.x, event.y
    curve = []


def draw2(event):
    """ Draws a line segment from old mouse position to new one
    """

    global oldx2, oldy2, canvas, curve    # oldx and oldy will be modified
    newx2, newy2 = event.x, event.y       # new mouse position

    # connect previous  mouse position to current one
    curve.append(canvas.create_line(oldx2, oldy2, newx2, newy2))

    oldx2, oldy2 = newx2, newy2


def delete2(event):
    """ Delete last curve drawn
    """

    global curve
    for segment in curve:
        canvas.delete(segment)


root = Tk()

oldx2, oldy2 = 0, 0     # mouse coordinates (global variables)

# canvas
canvas = Canvas(root, height=100, width=150)

# bind left mouse button click event to begin
canvas.bind("<Button-1>", begin2)

# bind mouse motion while pressing left button event to draw()
canvas.bind("<Button1-Motion>", draw2)

# bind Ctrl-Left button mouse click to delete()
canvas.bind("<Control-Button-1>", delete2)

canvas.pack()
root.mainloop()


###########
### 9.7 ###
###########
print('\nPP 9.7')

from tkinter import Frame, SUNKEN

# event handlers up(), down(), left(), right()


def up():
    """ Move pen up 10 pixels
    """

    global y, canvas                            # y is modified
    canvas.create_line(x, y, x, y - 10)
    y -= 10


def down():
    """ Move pen down 10 pixels
    """

    global y, canvas                            # y is modified
    canvas.create_line(x, y, x, y + 10)
    y += 10


def left():
    """ Move pen left 10 pixels
    """

    global x, canvas
    canvas.create_line(x, y, x - 10, y)
    x -= 10


def right():
    """ Move pen right 10 pixels
    """

    global x, canvas
    canvas.create_line(x, y, x + 10, y)
    x += 10


root = Tk()

# canvas with border size 100 x 150
canvas = Canvas(root, height=100, width=150,
                relief=SUNKEN, borderwidth=3)
canvas.pack(side=LEFT)

# frame to hold 4 buttons
box = Frame(root)
box.pack(side=RIGHT)

# the 4 button widgets have Frame widget box as their master
button = Button(box, text='up', command=up)
button.grid(row=0, column=0, columnspan=2)
button = Button(box, text='left', command=left)
button.grid(row=1, column=0)
button = Button(box, text='right', command=right)
button.grid(row=1, column=1)
button = Button(box, text='down', command=down)
button.grid(row=2, column=0, columnspan=2)

# pen position, initially in the middle o the canvas
x, y = 50, 70

root.mainloop()