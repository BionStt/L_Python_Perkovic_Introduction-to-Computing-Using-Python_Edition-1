__author__ = 'Rolando'
#############################################
### Perkovic Intro to Python              ###
#### CH 9: Graphical User Interfaces     ####
##### PG 331 CH 9                       #####
#############################################

from tkinter import Tk
from tkinter import Button, Frame
from tkinter.messagebox import showinfo
from time import strftime, localtime


class ClickIt(Frame):
    """ GUI that shows current time
    """

    def __init__(self, master):
        """ Constructor
        """

        Frame.__init__(self, master)
        self.pack()

        # button for time display
        button = Button(self, text="Click it",
                        command=self.clicked)
        button.pack()

    def clicked(self):
        """ Prints day and time info
        """

        # creates string for time display
        time = strftime('Day: %d %b %Y\nTime: %H:%M:%S %p\n', localtime())

        # display time in a pop-up window
        showinfo(message=time)


# root = Tk()
# clickit = ClickIt(root)
# clickit.pack()
# root.mainloop()


from tkinter import Entry, Label, END, CENTER
from time import strptime


class Day(Frame):
    """ An application that computes weekday corresponding to date
    """

    def __init__(self, master):
        """ Constructor
        """

        Frame.__init__(self, master)
        self.pack()

        # label for date
        label = Label(self, text='Enter Date')
        label.grid(row=0, column=0)

        # entry widget for date
        self.dateEnt = Entry(self)
        self.dateEnt.grid(row=0, column=1)

        # button for computing date to weekday
        button = Button(self, text='Enter',
                        command=self.compute)
        button.grid(row=1, column=0, columnspan=2)

    def compute(self):
        """ Display weekday corresponding to date in dateEnt;
            date must have format MMM SS, YYYY (eg, Jan 21 1967)
        """

        # read date from entry dateEnt
        date = self.dateEnt.get()

        # compute weekday corresponding to date
        weekday = strftime('%A', strptime(date, '%b %d %Y'))

        # display the weekday in a pop-up window
        showinfo(message='{} was a {}'.format(date, weekday))

        # delete date from entry dateEnt
        self.dateEnt.delete(0, END)

# root = Tk()
# day = Day(root)
# day.pack()
# clickit = ClickIt(root)
# clickit.pack()
# root.mainloop()

from tkinter import Canvas, BOTH


class Draw(Frame):
    """ A basic drawing application
    """

    def __init__(self, parent):
        """ Constructor - Canvas with mouse controlled pen
        """
        Frame.__init__(self, parent)
        self.pack()

        # mouse coordinates are instance variables
        self.oldx, self.oldy = 0, 0

        # create canvas and bind mouse events to handlers
        self.canvas = Canvas(self, height=100, width=150)
        self.canvas.bind("<Button-1>", self.begin)
        self.canvas.bind("<Button1-Motion>", self.draw)
        self.canvas.pack(expand=True, fill=BOTH)

    def begin(self, event):
        """ Handles left button click by recording mouse position
        """

        self.oldx, self.oldy = event.x, event.y

    def draw(self, event):
        """ Handles mouse motion while pressing left button, by
            connecting the previous mouse motion to the new one
        """

        newx, newy = event.x, event.y
        self.canvas.create_line(self.oldx, self.oldy, newx, newy)
        self.oldx, self.oldy = newx, newy

# root = Tk()
# canvas = Draw(root)
# canvas.pack()
# root.mainloop()

###########
### 9.8 ###
###########
print('\nPP 9.8')

from tkinter import Text


class KeyLogger(Frame):
    """ A basic editor that logs keystrokes
    """

    def __init__(self, master=None):
        """ Constructor - text widget and binds to keystrokes to handler record
        """

        Frame.__init__(self, master)
        self.pack()

        # bind a keypress event with the event handling function record()
        text = Text(width=20, height=5)
        text.bind('<KeyPress>', self.record)
        text.pack(expand=True, fill=BOTH)

    def record(self, event):
        """ Handles key stroke event by printing character associated with key
        """

        print('char={}'.format(event.keysym))

# root = Tk()
# keylog = KeyLogger(root)
# keylog.pack()
# root.mainloop()

###########
### 9.9 ###
###########
print('\nPP 9.9')

from tkinter import LEFT, RIGHT, SUNKEN, RIDGE, RAISED


class Plotter(Frame):
    """ A simple pen drawing app
    """

    def __init__(self, parent=None):
        """ Constructor - Arrange canvas and 4 button controlling pen
        """

        Frame.__init__(self, parent)
        self.pack()

        # initial coordinates of pen
        self.x = 75
        self.y = 50

        # create 100 x 150 canvas
        self.canvas = Canvas(self, height=100, width=150,
                             relief=SUNKEN, borderwidth=3)
        self.canvas.pack(side=LEFT)

        # frame to hold 4 buttons
        buttons = Frame(self)
        buttons.pack(side=RIGHT)

        # 4 button widgets that have Frame widget box as their master
        b = Button(buttons, text='up', command=self.up)
        b.grid(row=0, column=0, columnspan=2)
        b = Button(buttons, text='left', command=self.left)
        b.grid(row=1, column=0)
        b = Button(buttons, text='right', command=self.right)
        b.grid(row=1, column=1)
        b = Button(buttons, text='down', command=self.down)
        b.grid(row=2, column=0, columnspan=2)

    def up(self):
        """ Move pen up 10 pixels
        """

        self.canvas.create_line(self.x, self.y, self.x, self.y - 10)
        self.y -= 10

    def down(self):
        """ Move pen down 10 pixels
        """

        self.canvas.create_line(self.x, self.y, self.x, self.y + 10)
        self.y += 10

    def left(self):
        """ Move pen left 10 pixels
        """

        self.canvas.create_line(self.x, self.y, self.x - 10, self.y)
        self.x -= 10

    def right(self):
        """ Move pen right 10 pixels
        """

        self.canvas.create_line(self.x, self.y, self.x + 10, self.y)
        self.x += 10

# root = Tk()
# plot = Plotter(root)
# plot.pack()
# root.mainloop()

############
### 9.10 ###
############
print('\nPP 9.10')

from math import sqrt


class Calc(Frame):
    """ A Simple Calculator
    """

    def __init__(self, parent=None):
        """ Constructor - Calculator
        """

        Frame.__init__(self, parent)
        self.pack()

        # saved input data
        self.memory = ''                    # memory
        self.expr = ''                      # current expression
        self.startOfNextOperand = True      # start of new operand

        # entry widget for display
        self.entry = Entry(self, relief=RIDGE, borderwidth=3,
                           width=20, bg='gray',
                           font=('Helvetica', 18))
        self.entry.insert(END, '0')                                             # 9.28
        self.entry.grid(row=0, column=0, columnspan=5)

        # calculator button labels in 2D list
        buttons = [['MC',    'M+',       'M-',   'MR'],
                   ['C', '\u221a',  'x\u00b2',    '+'],
                   ['7',      '8',        '9',    '-'],
                   ['4',      '5',        '6',    '*'],
                   ['1',      '2',        '3',    '/'],
                   ['0',      '.',       '+-',    '=']]

        # place buttons in appropriate row and column
        for r in range(6):
            for c in range(4):
                # function cmd() is defined so that when it is
                # called without an input argument, it executes
                # self.click(buttons[r][c])
                def cmd(x=buttons[r][c]):
                    self.click(x)

                b = Button(self,                    # button for symbol buttons [r][c]
                           text=buttons[r][c],
                           width=3,
                           relief=RAISED,
                           command=cmd)             # cmd is handler
                b.grid(row=r + 1, column=c)           # entry is in row 0

    def click(self, key):
        """ Handler for event of pressing button labeled key
        """
        if self.entry.get() == '0':                                             # 9.28
            self.entry.delete(0, END)                                           #

        if key == '=':
            # evaluate expression, including the value
            # displayed in entry and display result
            try:
                result = eval(self.expr + self.entry.get())
                self.entry.delete(0, END)
                self.entry.insert(END, result)
                self.expr = ''
            except:
                self.entry.delete(0, END)
                self.entry.insert(END, 'Error')

        elif key in '+*-/':
            # add operand displayed in entry and operator key
            # to expression and and prepare for next operand
            self.expr += self.entry.get()
            self.expr += key
            self.startOfNextOperand = True

        elif key == '\u221a':
            # compute and display square root of entry
            result = sqrt(eval(self.entry.get()))
            self.entry.delete(0, END)
            self.entry.insert(END, result)

        elif key == 'x\u00b2':
            # compute and display number of squares in entry
            result = eval(self.entry.get()) ** 2
            self.entry.delete(0, END)
            self.entry.insert(END, result)

        elif key == 'C':
            # clear entry
            self.entry.delete(0, END)
            self.entry.insert(END, 0)                                           # 9.28

        elif key in {'M+', 'M-'}:
            # add or subtract entry value from memory
            self.memory = str(eval(self.memory + key[1] + self.entry.get()))

        elif key == 'MR':
            # replace value in entry with value stored in memory
            self.entry.delete(0, END)
            self.entry.insert(END, self.memory)

        elif key == 'MC':
            # clear memory
            self.memory = ''

        elif key == '+-':
            # switch entry from positive to negative and vice versa
            # if there is no value in entry, do nothing
            try:
                if self.entry.get()[0] == '-':
                    self.entry.delete(0)
                else:
                    self.entry.insert(0, '-')
            except IndexError:
                pass

        else:
            # insert digit at end of entry, or as the first
            # digit if start of next operand
            if self.startOfNextOperand:
                self.entry.delete(0, END)
                self.startOfNextOperand = False
            self.entry.insert(END, key)

# root = Tk()
# calcu = Calc(root)
# root.mainloop()

############
### 9.11 ###
############
print('\nPP 9.11')

from tkinter import PhotoImage


class Profile(Frame):
    """ Displays a user profile
    """

    def __init__(self, master=None):
        """ Constructor
        """

        Frame.__init__(self, master)
        self.grid(row=0, column=0)

        # label for profile photo
        self.photo = PhotoImage(file='profile_pic.gif')
        photo_label = Label(self,
                            borderwidth=3,
                            relief=RIDGE,
                            image=self.photo,
                            width=400,
                            height=400)
        photo_label.pack(side=LEFT)

        # label for info text
        self.text = 'Johnny Karate\nPawnee, Indiana\nJun 4, 1980'
        text_label = Label(self,
                           font=('Helvetica', 16),
                           text=self.text)
        text_label.pack(side=LEFT)

# root = Tk()
# prof = Profile(root)
# root.mainloop()

############
### 9.12 ###
############
print('\nPP 9.12')

# 9.12 already done in in 9.3???

############
### 9.13 ###
############
print('\nPP 9.13')


class PhoneDial(Frame):
    """ PhonePad widget
    """

    def __init__(self, parent=None):
        """ Constructor
        """

        Frame.__init__(self, parent)
        self.pack()

        # entry widget for display
        self.entry = Entry(self,
                           relief=RIDGE,
                           borderwidth=3,
                           width=10,
                           bg='gray',
                           font=('Helvetica', 18))
        self.entry.grid(row=0, column=0, columnspan=3)

        # numpad labels in 2D list
        self.numpad = [['1', '2', '3'],
                       ['4', '5', '6'],
                       ['7', '8', '9'],
                       ['*', '0', '#']]

        # place buttons in appropriate row and column
        for r in range(4):
            for c in range(3):
                # function cmd() is defined so that when it is
                # called without an input argument, it executes
                # self.click(buttons[r][c]
                def cmd(x=self.numpad[r][c]):
                    self.click(x)

                numpad_label = Button(self,
                                      relief=RAISED,
                                      padx=10,
                                      text=self.numpad[r][c],
                                      command=cmd)
                numpad_label.grid(row=r + 1, column=c)

    def click(self, key):
        """ Handler for event of pressing button labeled key
        """

        # insert digit at end of entry
        self.entry.insert(END, key)

# root = Tk()
# Phone = PhoneDial(root)
# root.mainloop()

############
### 9.14 ###
############
print('\nPP 9.14')


class PlotterArrow(Frame):
    """ A simple pen drawing app
    """

    def __init__(self, master=None):
        """ Constructor - Arrange pen canvas with arrow key controlling pen
        """

        Frame.__init__(self, master)
        self.pack()

        # initial coordinates of pen
        self.x = 75
        self.y = 50

        # create 100 x 150 canvas
        self.canvas = Canvas(self,
                             height=100,
                             width=150,
                             relief=SUNKEN,
                             borderwidth=3)

        #
        self.canvas.bind("<1>", lambda event: self.canvas.focus_set())
        # self.canvas.focus_set()
        self.canvas.bind("<Up>", self.cmd)
        self.canvas.bind("<Down>", self.cmd)
        self.canvas.bind("<Left>", self.cmd)
        self.canvas.bind("<Right>", self.cmd)

        self.canvas.pack(side=LEFT)

    def cmd(self, event):
        self.move(event.keysym)

    def up(self):
        """ Handles event of keypress up-arrow;
            moves pen up 10 pixels
        """

        self.canvas.create_line(self.x, self.y, self.x, self.y - 10)
        self.y -= 10

    def down(self):
        """ Handles event of keypress down-arrow;
            moves pen down 10 pixels
        """

        self.canvas.create_line(self.x, self.y, self.x, self.y + 10)
        self.y += 10

    def left(self):
        """ Handles event of keypress left-arrow;
            moves pen left 10 pixels
        """

        self.canvas.create_line(self.x, self.y, self.x - 10, self.y)
        self.x -= 10

    def right(self):
        """ Handles event of keypress right-arrow;
            moves pen right 10 pixels
        """

        self.canvas.create_line(self.x, self.y, self.x + 10, self.y)
        self.x += 10

    def move(self, key):
        if key == 'Up':
            self.up()
        elif key == 'Down':
            self.down()
        elif key == 'Left':
            self.left()
        elif key == 'Right':
            self.right()

# root = Tk()
# plot = PlotterArrow(root)
# root.mainloop()

############
### 9.15 ###
############
print('\nPP 9.15')


class PlotterEasy(Frame):

    def __init__(self, master):
        """ Constructor - Arrange pen canvas
        """

        Frame.__init__(self, master)
        self.pack()

        # initial coordinates of pen
        self.x = 75
        self.y = 50

        # create 100 x 150 canvas
        self.canvas = Canvas(self,
                             height=100,
                             width=150,
                             relief=SUNKEN,
                             borderwidth=3)
        self.canvas.pack(side=LEFT)

        # frame to hold 4 buttons
        buttons = Frame(self)
        buttons.pack(side=RIGHT)

        # 4 button widgets that have Frame widget box as their master
        def up(x=0, y=-10):
            self.move(x, y)
        b = Button(buttons, text='up', command=up)
        b.grid(row=0, column=0, columnspan=2)

        def left(x=-10, y=0):
            self.move(x, y)
        b = Button(buttons, text='left', command=left)
        b.grid(row=1, column=0)

        def right(x=10, y=0):
            self.move(x, y)
        b = Button(buttons, text='right', command=right)
        b.grid(row=1, column=1)

        def down(x=0, y=10):
            self.move(x, y)
        b = Button(buttons, text='down', command=down)
        b.grid(row=2, column=0, columnspan=2)

    def move(self, dx, dy):
        """ Handler function for movement inputs
        """

        self.canvas.create_line(self.x, self.y, self.x + dx, self.y + dy)
        self.y += dy
        self.x += dx

# root = Tk()
# plot = PlotterEasy(root)
# root.mainloop()

############
### 9.16 ###
############
print('\nPP 9.16')


class PlotterClear(Frame):
    def __init__(self, master):
        """ Constructor - Arrange pen canvas with arrow key controlling pen
        """

        Frame.__init__(self, master)
        self.pack()

        # initial coordinates of pen
        self.x = 75
        self.y = 50
        self.curve = []
        self.oldx = 75
        self.oldy = 50

        # create 100 x 150 canvas
        self.canvas = Canvas(self,
                             height=100,
                             width=150,
                             relief=SUNKEN,
                             borderwidth=3)
        self.canvas.pack(side=LEFT)

        # frame to hold 4 buttons
        buttons = Frame(self)
        buttons.pack(side=RIGHT)

        # 4 button widgets that have Frame widget box as their master
        def up(x=0, y=-10):
            self.move(x, y)
        b = Button(buttons, text='up', command=up)
        b.grid(row=0, column=0, columnspan=2)

        def left(x=-10, y=0):
            self.move(x, y)
        b = Button(buttons, text='left', command=left)
        b.grid(row=1, column=0)

        def right(x=10, y=0):
            self.move(x, y)
        b = Button(buttons, text='right', command=right)
        b.grid(row=1, column=1)

        def down(x=0, y=10):
            self.move(x, y)
        b = Button(buttons, text='down', command=down)
        b.grid(row=2, column=0, columnspan=2)

        b = Button(buttons, text='clear', command=self.clear)
        b.grid(row=4, column=0, columnspan=1)

        b = Button(buttons, text='delete', command=self.delete)
        b.grid(row=4, column=3, columnspan=3)

    def delete(self):
        """ Delete last curve drawn
        """

        self.canvas.delete(self.curve[-1])
        self.x = self.oldx
        self.y = self.oldy

    def clear(self):
        """ Clears frame of all curves
        """

        for segment in self.curve:
            self.canvas.delete(segment)
        self.x = 75
        self.y = 50

    def move(self, dx, dy):
        """ Handler function for movement input
        """

        self.curve.append(self.canvas.create_line(self.x, self.y, self.x + dx, self.y + dy))
        self.oldx = self.x
        self.oldy = self.y
        self.x += dx
        self.y += dy

# root = Tk()
# plot = PlotterClear(root)
# root.mainloop()


class PlotterDelete(Frame):
    def __init__(self, master):
        """ Constructor - Arrange pen canvas with arrow key controlling pen
        """

        Frame.__init__(self, master)
        self.pack()

        # initial coordinates of pen
        self.x = 75
        self.y = 50
        self.curve = []
        self.old_plots = []
        self.oldx = 75
        self.oldy = 50

        # create 100 x 150 canvas
        self.canvas = Canvas(self,
                             height=100,
                             width=150,
                             relief=SUNKEN,
                             borderwidth=3)
        self.canvas.pack(side=LEFT)

        # frame to hold 4 buttons
        buttons = Frame(self)
        buttons.pack(side=RIGHT)

        # 4 button widgets that have Frame widget box as their master
        def up(x=0, y=-10):
            self.move(x, y)
        b = Button(buttons, text='up', command=up)
        b.grid(row=0, column=0, columnspan=2)

        def left(x=-10, y=0):
            self.move(x, y)
        b = Button(buttons, text='left', command=left)
        b.grid(row=1, column=0)

        def right(x=10, y=0):
            self.move(x, y)
        b = Button(buttons, text='right', command=right)
        b.grid(row=1, column=1)

        def down(x=0, y=10):
            self.move(x, y)
        b = Button(buttons, text='down', command=down)
        b.grid(row=2, column=0, columnspan=2)

        b = Button(buttons, text='clear', command=self.clear)
        b.grid(row=4, column=0, columnspan=1)

        b = Button(buttons, text='delete', command=self.delete)
        b.grid(row=4, column=3, columnspan=3)

    def delete(self):
        """ Delete last curve drawn
        """

        self.canvas.delete(self.curve[-1])
        self.curve = self.curve[:-1]
        self.x = self.old_plots[-1][0]
        self.y = self.old_plots[-1][1]
        self.old_plots = self.old_plots[:-1]

    def clear(self):
        """ Clears frame of all curves
        """

        for segment in self.curve:
            self.canvas.delete(segment)
        self.old_plots = []
        self.x = 75
        self.y = 50

    def move(self, dx, dy):
        """ Handler function for movement input
        """

        self.curve.append(self.canvas.create_line(self.x, self.y, self.x + dx, self.y + dy))
        self.oldx = self.x
        self.oldy = self.y
        self.x += dx
        self.y += dy
        self.old_plots.append([self.oldx, self.oldy])

# root = Tk()
# plot = PlotterDelete(root)
# root.mainloop()

############
### 9.17 ###
############
print('\nPP 9.17')


class Calc2(Frame):
    """ A Simple Calculator
    """

    def __init__(self, master=None):
        """ Constructor - Calculator
        """

        Frame.__init__(self, master)
        self.pack()

        # saved input data
        self.memory = ''                    # memory
        self.expr = ''                      # current expression
        self.startOfNextOperand = True      # start of new operand
        self.operand_list = ['plus', 'minus', 'asterisk', 'slash', '-', '+', '*', '/']
        self.non_operand_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']

        # entry widget for display
        self.entry = Entry(self, relief=RIDGE, borderwidth=3,
                           width=20, bg='gray',
                           font=('Helvetica', 18))
        self.entry.bind("<1>", lambda event: self.entry.focus_set())
        self.entry.bind('<KeyPress>', self.click)

        self.entry.grid(row=0, column=0, columnspan=5)

        # calculator button labels in 2D list
        buttons = [['MC',    'M+',       'M-',   'MR'],
                   ['C', '\u221a',  'x\u00b2',    '+'],
                   ['7',      '8',        '9',    '-'],
                   ['4',      '5',        '6',    '*'],
                   ['1',      '2',        '3',    '/'],
                   ['0',      '.',       '+-',    '=']]

        # place buttons in appropriate row and column
        for r in range(6):
            for c in range(4):
                # function cmd() is defined so that when it is
                # called without an input argument, it executes
                # self.click(buttons[r][c])
                def cmd(x=buttons[r][c]):
                    self.click(x)

                b = Button(self,                    # button for symbol buttons [r][c]
                           text=buttons[r][c],
                           width=3,
                           relief=RAISED,
                           command=cmd)             # cmd is handler
                b.grid(row=r + 1, column=c)           # entry is in row 0

    def keypress(self, event):
        self.click(event.keysym)

    def click(self, key):
        """ Handler for event of pressing button labeled key
        """

        if key == '=' or key == 'equal' or key == 'Return':
            # evaluate expression, including the value
            # displayed in entry and display result
            try:
                result = eval(self.expr + self.entry.get())
                self.entry.delete(0, END)
                self.entry.insert(END, result)
                self.expr = ''
            except:
                self.entry.delete(0, END)
                self.entry.insert(END, 'Error')

        elif key in '+*-/' or key in self.operand_list:
            # add operand displayed in entry and operator key
            # to expression and and prepare for next operand
            self.expr += self.entry.get()
            self.expr += key
            self.startOfNextOperand = True

        elif key == '\u221a':
            # compute and display square root of entry
            result = sqrt(eval(self.entry.get()))
            self.entry.delete(0, END)
            self.entry.insert(END, result)

        elif key == 'x\u00b2':
            # compute and display number of squares in entry
            result = eval(self.entry.get()) ** 2
            self.entry.delete(0, END)
            self.entry.insert(END, result)

        elif key == 'C':
            # clear entry
            self.entry.delete(0, END)

        elif key in {'M+', 'M-'}:
            # add or subtract entry value from memory
            self.memory = str(eval(self.memory + key[1] + self.entry.get()))

        elif key == 'MR':
            # replace value in entry with value stored in memory
            self.entry.delete(0, END)
            self.entry.insert(END, self.memory)

        elif key == 'MC':
            # clear memory
            self.memory = ''

        elif key == '+-':
            # switch entry from positive to negative and vice versa
            # if there is no value in entry, do nothing
            try:
                if self.entry.get()[0] == '-':
                    self.entry.delete(0)
                else:
                    self.entry.insert(0, '-')
            except IndexError:
                pass
        elif key in self.non_operand_list:
            # insert digit at end of entry, or as the first
            # digit if start of next operand
            if self.startOfNextOperand:
                self.entry.delete(0, END)
                self.startOfNextOperand = False
            self.entry.insert(END, key)
        #
        # else:
        #     # insert digit at end of entry, or as the first
        #     # digit if start of next operand
        #     if self.startOfNextOperand:
        #         self.entry.delete(0, END)
        #         self.startOfNextOperand = False
        #     self.entry.insert(END, key)

# root = Tk()
# cal2 = Calc2(root)
# root.mainloop()


############
### 9.18 ###
############
print('\nPP 9.18')


class BMI(Frame):
    """ Basic BMI calculator
    """

    def __init__(self, master=None):
        """ Constructor - Takes height and weight and computes bmi
        """

        Frame.__init__(self, master)
        self.pack()

        # height label
        height_label = Label(self, text='Enter your height:')
        height_label.grid(row=0, column=0)

        # height entry
        self.height = Entry(self)
        self.height.grid(row=0, column=1)

        # weight label
        weight_label = Label(self, text='Enter your weight:')
        weight_label.grid(row=1, column=0)

        # weight entry
        self.weight = Entry(self)
        self.weight.grid(row=1, column=1)

        # bmi compute button
        button = Button(self, text='Compute BMI',
                        command=self.compute_bmi)
        button.grid(row=2, column=0, columnspan=2)

    def compute_bmi(self):
        """ Display BMI number and BMI scale corresponding to weight and height
        """

        # read weight and height from entry
        weight = eval(self.weight.get())
        height = eval(self.height.get())

        # calculate bmi number
        bmi_number = (weight * 703 / height ** 2)

        # determine bmi scale from bmi number
        bmi_scale = ''

        if bmi_number < 18.5:
            bmi_scale += 'Underweight'
        elif bmi_number <= 25:
            bmi_scale += 'Normal'
        else:
            bmi_scale += 'Overweight'

        # display bmi message in a pop-up window
        showinfo(message='Your BMI is {}\n you are {:.2f}'.format(bmi_number, bmi_scale))

        # delete entries from weight and height
        self.height.delete(0, END)
        self.weight.delete(0, END)

# root = Tk()
# bmicalc = BMI(root)
# root.mainloop()

############
### 9.19 ###
############
print('\nPP 9.19')


class Mortgage(Frame):
    """ Mortgage Calculator
    """

    def __init__(self, master=None):
        """ Constructor - Takes a Loan Amount, Interest Rate, and Loan Term
        """

        Frame.__init__(self, master)
        self.pack()

        # loan amount Label
        amount_label = Label(self, text='Loan Amount:')
        amount_label.grid(row=0, column=0)

        # loan amount entry
        self.amount = Entry(self)
        self.amount.grid(row=0, column=1)

        # interest rate label
        interest_label = Label(self, text='Interest Rate:')
        interest_label.grid(row=1, column=0)

        # interest rate entry
        self.interest = Entry(self)
        self.interest.grid(row=1, column=1)

        # loan term label
        term_label = Label(self, text='Loan Term:')
        term_label.grid(row=2, column=0)

        # loan term entry
        self.term = Entry(self)
        self.term.grid(row=2, column=1)

        # compute mortgage button
        button = Button(self, text='Compute Mortgage',
                        command=self.compute_mortgage)
        button.grid(row=3, column=0, columnspan=2)

    def compute_mortgage(self):
        """ Handler function for mortgage calculation
        """

        amount = eval(self.amount.get())
        interest = eval(self.interest.get())
        term = eval(self.term.get())
        c = interest / 1200

        mortgage_number = (amount * c * (1 + c) ** term) / ((1 + c) ** term - 1)

        # display monthly mortgage message in a pop-up window
        showinfo(message='Your Monthly Mortgage is ${:.2f}'.format(mortgage_number))

        # delete entries from weight and height
        self.amount.delete(0, END)
        self.interest.delete(0, END)
        self.term.delete(0, END)

# root = Tk()
# mortgagecalc = Mortgage(root)
# root.mainloop()

############
### 9.20 ###
############
print('\nPP 9.20')


class Finances(Frame):
    """ Finance applet with calculator and Mortgage widgets
    """

    def __init__(self, master=None):
        """ Constructor - combines mortgage and calculator widgets
        """

        Frame.__init__(self, master)
        self.pack()

        # Mortgage widget
        mg = Mortgage(self)
        mg.pack(side=LEFT)

        # Calculator widget
        cl = Calc(self)
        cl.pack(side=LEFT)

# root = Tk()
# fina = Finances(root)
# root.mainloop()

############
### 9.21 ###
############
print('\nPP 9.21')


class PointRec(Frame):
    """ creates a widget of siz 480 x 640 that prints the coordinates where the user has clicked
    """

    def __init__(self, master=None):
        """ Constructor - Creates canvas
        """

        Frame.__init__(self, master)
        self.pack()

        # Canvas
        self.canvas = Canvas(self, height=480, width=640)
        self.canvas.bind("<Button-1>", self.record)
        self.canvas.pack(expand=True, fill=BOTH)

    def record(self, event):
        """ Handles left button click and prints mouse position
        """

        print('you clicked at ({}, {})'.format(event.x, event.y))

# root = Tk()
# pr = PointRec(root)
# root.mainloop()


############
### 9.22 ###
############
print('\nPP 9.22')


class PhoneDialUS(Frame):
    """ Phone Pad widget
    """

    def __init__(self, parent=None):
        """ Constructor
        """

        Frame.__init__(self, parent)
        self.pack()

        # entry widget for display
        self.entry = Entry(self,
                           relief=RIDGE,
                           borderwidth=3,
                           width=10,
                           bg='gray',
                           font=('Helvetica', 18))
        self.entry.grid(row=0, column=0, columnspan=3)

        # numpad labels in 2D list
        self.num_pad = [['1', '2', '3'],
                       ['4', '5', '6'],
                       ['7', '8', '9'],
                       ['*', '0', '#']]

        # place buttons in appropriate row and column
        for r in range(4):
            for c in range(3):
                # function cmd() is defined so that when it is
                # called without and input argument, it executes
                # self.click(buttons[r][c])
                def cmd(x=self.num_pad[r][c]):
                    self.click(x)

                num_pad_label = Button(self,
                                       relief=RAISED,
                                       padx=10,
                                       text=self.num_pad[r][c],
                                       command=cmd)
                num_pad_label.grid(row=r + 1, column=c)

    def click(self, key):
        """ Handler for event of pressing button labeled key
        """

        # insert digit at end of entry
        self.entry.insert(END, key)

        # insert '-' every 3 numbers
        entry = self.entry.get()
        if len(entry) == 3:
            self.entry.insert(END, '-')

        if len(entry) == 7:
            self.entry.insert(END, '-')

# root = Tk()
# usphone = PhoneDialUS(root)
# root.mainloop()

####################
### 9.23  + 9.24 ###
####################
print('\nPP 9.23 + 9.24')

from random import randrange, choice


class Game(Frame):
    """ 1-10 guessing game widget
    """

    def __init__(self, master=None):
        """ Constructor
        """

        Frame.__init__(self, master)
        self.pack()

        # text for guess
        self.label = Label(self, text='Enter your guess:')
        self.label.grid(row=0, column=0)

        # entry widget for guess
        self.guess = Entry(self, width=14)
        self.guess.grid(row=1, column=0)

        # generates answer to guess
        self.answer = randrange(0, 10)

        # compute_guess button
        self.button = Button(self, text='Enter',
                             command=self.compute_guess)
        self.button.grid(row=2, column=0)

        # bind enter/return key to button
        def cmd(event):
            self.compute_guess()
        self.guess.bind("<Return>", cmd)

    def compute_guess(self):
        """ Display guess
        """

        # read guess from entry
        guess = eval(self.guess.get())

        # display if answer is correct in a pop-up window
        if guess == self.answer:
            showinfo(message='You are correct!')
        else:
            showinfo(message='Sorry, try again!')

        # delete entry from guess
        self.guess.delete(0, END)

# root = Tk()
# guessGame = Game(root)
# root.mainloop()

############
### 9.25 ###
############
print('\nPP 9.25')


class GameRefresh(Frame):
    """ 1-10 endless  guessing game
    """

    def __init__(self, master=None):
        """ Constructor
        """

        Frame.__init__(self, master)
        self.pack()

        # text for guess
        self.label = Label(self, text='Enter your guess:')
        self.label.grid(row=0, column=0)

        # entry widget for guess
        self.guess = Entry(self, width=14)
        self.guess.grid(row=1, column=0)

        # generate answer to guess
        self.answer = randrange(0, 10)

        # compute guess button
        self.button = Button(self, text='Enter',
                             command=self.compute_guess)
        self.button.grid(row=2, column=0)

        def cmd(event):
            self.compute_guess()
        self.guess.bind("<Return>", cmd)

    def compute_guess(self):
        """ Display guess
        """

        # read guess from entry
        guess = eval(self.guess.get())

        # display if answer is correct
        if guess == self.answer:
            showinfo(message="You are correct!\nLet's do this again...")
            self.answer = randrange(0, 10)
        else:
            showinfo(message='Sorry, try again!')

        # delete entry from guess
        self.guess.delete(0, END)

# root = Tk()
# guessGame2 = GameRefresh(root)
# root.mainloop()

############
### 9.26 ###
############
print('\nPP 9.26')


class Craps(Frame):
    """ Starts a text game of craps
    """

    def __init__(self, master=None):
        """ Constructor -
        """

        Frame.__init__(self, master)
        self.pack()

        # text for roll
        self.label = Label(self, text='Your roll:')
        self.label.grid(row=0, column=0, columnspan=3)

        # display widget for roll
        self.roll = Entry(self, justify=CENTER)
        self.result = 0
        self.roll.grid(row=1, column=0, columnspan=3)

        # new game button
        self.new_game_button = Button(self, text='New Game',
                                      command=self.new_game)
        self.new_game_button.grid(row=2, column=0)

        # roll for point button
        self.roll_for_point_button = Button(self, text='Roll for point',
                                            command=self.roll_for_point)
        self.roll_for_point_button.grid(row=2, column=1)

    def new_game(self):
        """ Handler for initialization of new game
        """

        # start first roll
        d1 = randrange(1, 7)
        d2 = randrange(1, 7)
        first_result = d1 + d2

        # check roll result
        if first_result in {7, 11}:
            # a roll of 7 or 11 wins first round
            self.roll.insert(END, first_result)
            showinfo(message='You won!')
            self.roll.delete(0, END)
        elif first_result in {2, 3, 12}:
            # a roll of 2, 3, or 12 loses first round
            self.roll.insert(END, first_result)
            showinfo(message='You lost!')
            self.roll.delete(0, END)
        else:
            # game proceeds to round 2 otherwise
            self.roll.delete(0, END)
            self.roll.insert(END, first_result)
            self.result = first_result

    def roll_for_point(self):
        """ Handler for re-roll after initial roll
        """

        # start next roll
        d1 = randrange(1, 7)
        d2 = randrange(1, 7)
        first_result = self.result
        next_result = d1 + d2

        # check roll result
        if next_result == 7:
            # a roll of 7 after round 1 loses game
            self.roll.delete(0, END)
            self.roll.insert(END, next_result)
            showinfo(message='You lost!')
        elif next_result == first_result:
            # a roll equal in value to round 1 roll wins
            self.roll.delete(0, END)
            self.roll.insert(END, next_result)
            showinfo(message='You won!')
            self.roll.delete(0, END)
            self.roll.delete(0, END)
        else:
            # game goes another round otherwise
            self.roll.delete(0, END)
            self.roll.insert(END, next_result)

# root = Tk()
# crap = Craps(root)
# root.mainloop()

############
### 9.27 ###
############
print('\nPP 9.27')

from time import time


class TypeSpeed(Frame):
    """ Records type speed
    """

    def __init__(self, master=None):
        """ Constructor -
        """

        Frame.__init__(self, master)
        self.pack()

        # text
        text = Text(width=20, height=5)
        text.bind('<KeyPress>', self.record)
        text.pack(expand=True, fill=BOTH)

        # instance variables for time stamps
        self.start_time = 0
        self.old_time = 0
        self.new_time = 0
        self.word_count = 0

    def record(self, event):
        """ records words-per-minute and time in between words
        """

        # record start time if no words have been typed yet
        if self.start_time == 0:
            self.start_time = time()

        # when space key is pressed
        if event.keysym == 'space':

            # unless it the first character entered
            if self.word_count == 0:
                self.new_time = 0
                self.start_time = 0
                return

            # add to word count
            self.word_count += 1

            # record end of current word
            self.new_time = time() - self.start_time

            # print time taken to type current word and average words per minute
            print(self.new_time - self.old_time)
            print(self.word_count / self.new_time * 60)

            # end of current word now start of new word
            self.old_time = self.new_time

        if self.word_count == 0:
            self.word_count += 1

# root = Tk()
# timestamp = TypeSpeed(root)
# root.mainloop()

############
### 9.28 ###
############
print('\nPP 9.28')

# Done in 9.10

###################
### 9.29 + 9.30 ###
###################
print('\nPP 9.29')


class Ed(Frame):
    """ basic arithmetic game
    """

    def __init__(self, master=None):
        """ Constructor -
        """

        Frame.__init__(self, master)
        self.pack()

        # define first problem in entry
        self.a = 0
        self.b = 0
        self.op = ''
        self.problem = ''
        self.generate_new_problem()
        self.problem_list = []

        # label for problem
        self.problem_label = Label(self, text='      Problem: ')
        self.problem_label.grid(row=0, column=0)

        # entry widget for problem
        self.problem_entry = Entry(self)
        self.problem_entry.grid(row=0, column=1)
        self.problem_entry.insert(END, self.problem)

        # label for answer
        self.answer_label = Label(self, text='Your answer: ')
        self.answer_label.grid(row=1, column=0)

        # entry widget for answer
        self.answer_entry = Entry(self)
        self.answer_entry.grid(row=1, column=1)

        # check answer button
        self.button = Button(self, text='Enter',
                             command=self.check_answer)
        self.button.grid(row=2, column=0, columnspan=2)

        # bind enter/return key to button
        def cmd(event):
            self.check_answer()
        self.answer_entry.bind("<Return>", cmd)

    def check_answer(self):
        """ Checks to see if answer is correct; if so, generate a new problem
        """

        # evaluate string problem
        solution = eval(self.problem)

        # once the answer is correct
        if eval(self.answer_entry.get()) == solution:

            # show pop-window
            showinfo(message='You got it!')

            # add solved problem to list of old problems
            self.problem_list.append(self.problem)

            # only keep 10 most recent problems
            if len(self.problem_list) > 10:
                self.problem_list.pop(0)

            # create a new problem that isn't in old problem list
            self.generate_new_problem()
            while self.problem in self.problem_list:
                self.generate_new_problem()

            # remove old problem and add new one to problem entry widget
            self.problem_entry.delete(0, END)
            self.problem_entry.insert(END, self.problem)

    def generate_new_problem(self):
        """ generates new problem; makes sure solution is always positive number
        """

        # randomly select numbers (1-9) and operand (addition or subtraction)
        self.a = randrange(0, 10)
        self.b = randrange(0, 10)
        self.op = choice(['+', '-'])

        # combine variables into problem
        self.problem = '{} {} {}'.format(self.a, self.op, self.b)

        # make sure solutions are always positive
        if self.a < self.b and self.op == '-':
            self.problem = '{} {} {}'.format(self.b, self.op, self.a)

# root = Tk()
# teach = Ed(root)
# root.mainloop()

############
### 9.32 ###
############
print('\nPP 9.32')

from calendar import monthrange


class Calendar(Frame):
    """ Basic Calendar app
    """

    def __init__(self, master=None, year=2000, month=1):
        """
        """

        Frame.__init__(self, master)
        self.pack()

        days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                  'August', 'September', 'October', 'November', 'December']
        self.notes = []

        # get weekday at which month starts and number of days in month
        self.weekday, self.numdays = monthrange(year, month)
        self.month = months[month - 1]
        self.year = year

        # create month and year label
        self.month_label_text = '{} {}'.format(self.month, year)
        month_label = Label(self, text=self.month_label_text)
        month_label.grid(row=0, columnspan=7)

        # create and place weekday labels
        for i in range(7):
            days_label = Label(self, text=days[i])
            days_label.grid(row=1, column=i)

        # create a calendar starting with week (row) 1 and day (column) 1
        week = 2

        for i in range(1, self.numdays + 1):
            # shift week to start at sunday instead of monday (sunday-saturday calendar)
            shift_weekday = self.weekday

            if self.weekday == 6:
                shift_weekday = 0
                week += 1
            else:
                shift_weekday += 1

            # create button i and place it in row: week, and column: day
            button = Button(self, text=str(i), width=2)
            button.grid(row=week, column=shift_weekday)

            # update weekday (column), and week(row)
            self.weekday += 1
            if self.weekday > 6:
                # week += 1                                     # use with monday-sunday calendar
                self.weekday = 0

    # def previous(self):
    #
    # def next(self):

root = Tk()
calen = Calendar(root, 2015, 2)
root.mainloop()