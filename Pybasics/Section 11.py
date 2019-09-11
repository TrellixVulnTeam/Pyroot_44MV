# S11 - Building a simple calculator application using Tkinter
# use lambdas for command on click
# parser - get the full string - express, compile - evaluate it

# permutation logic to be done

from tkinter import *   # importing tkinter module
import parser           # to perform mathematical operations
import tkinter.messagebox     # Message box


root = Tk()             # initializing the tkinter
root.title('Calculator')

# Functions on click of buttons

i = 0


def numberclick(num):
    global i
    displaybox.insert(i, num)
    i += 1


def allclear():
    displaybox.delete(0, END)


def backspace():
    entireinput = displaybox.get()
    if len(entireinput):
        newinput = entireinput[:-1]
        allclear()
        displaybox.insert(0, newinput)


def insert_operation(operators):
    global i
    length = len(operators)
    displaybox.insert(i, operators)
    i += length


def calculate():
    stringinput = displaybox.get()
    if '!' in stringinput:
        fact = 1
        newperm = stringinput[:-1]
        newerperm = int(newperm)
        for j in range(1, newerperm+1):
            fact = fact * j
        allclear()
        displaybox.insert(0, fact)
    else:
        expression = displaybox.get()
        par = parser.expr(expression).compile()   # expression, compile it
        result = eval(par)  # evaluates the parsed expression
        allclear()
        displaybox.insert(0, result)



# Display box


displaybox = Entry(root)
displaybox.grid(row=0, columnspan=6)

# Add number buttons

button1 = Button(root, text='1', command=lambda: numberclick(1)).grid(row=1, column=0)
button2 = Button(root, text='2', command=lambda: numberclick(2)).grid(row=1, column=1)
button3 = Button(root, text='3', command=lambda: numberclick(3)).grid(row=1, column=2)

button4 = Button(root, text='4', command=lambda: numberclick(4)).grid(row=2, column=0)
button5 = Button(root, text='5', command=lambda: numberclick(5)).grid(row=2, column=1)
button6 = Button(root, text='6', command=lambda: numberclick(6)).grid(row=2, column=2)

button7 = Button(root, text='7', command=lambda: numberclick(7)).grid(row=3, column=0)
button8 = Button(root, text='8', command=lambda: numberclick(8)).grid(row=3, column=1)
button9 = Button(root, text='9', command=lambda: numberclick(9)).grid(row=3, column=2)

button0 = Button(root, text='0', command=lambda: numberclick(0)).grid(row=4, column=1)

# Add functionality buttons
buttonac = Button(root, text='Ac', command=lambda: allclear()).grid(row=4, column=0)
buttonequals = Button(root, text='=', command=lambda: calculate()).grid(row=4, column=2)

buttonplus = Button(root, text='+', command=lambda: insert_operation('+')).grid(row=1, column=3)
buttonminus = Button(root, text='-', command=lambda: insert_operation('-')).grid(row=2, column=3)
buttonstar = Button(root, text='', command=lambda: insert_operation('')).grid(row=3, column=3)
buttondiv = Button(root, text='/', command=lambda: insert_operation('/')).grid(row=4, column=3)

buttonpi = Button(root, text='pi', command=lambda: insert_operation('3.14')).grid(row=1, column=4)
buttonpercent = Button(root, text='%', command=lambda: insert_operation('%')).grid(row=2, column=4)
buttonlbrac = Button(root, text='(', command=lambda: insert_operation('(')).grid(row=3, column=4)
buttonexp = Button(root, text='exp', command=lambda: insert_operation('exp')).grid(row=4, column=4)

buttonbspace = Button(root, text='<-', command=lambda: backspace()).grid(row=1, column=5)
buttonperm = Button(root, text='x!', command=lambda: insert_operation('!')).grid(row=2, column=5)
buttonrbrac = Button(root, text=')', command=lambda: insert_operation(')')).grid(row=3, column=5)
buttonsquare = Button(root, text='2', command=lambda: insert_operation('*2')).grid(row=4, column=5)


root.mainloop()
