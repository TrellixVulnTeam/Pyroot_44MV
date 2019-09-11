# l92 > TKINTER application > create application with GUI > Tkinter

from tkinter import *  # * imports all features



# l92, l93 > Frames , Buttons

# root = Tk()  # creates the window

# Labels

# label1 = Label(root, text='Fuckyou')   # puts the label in the window with the label text
# label1.pack()  # packs to the window

# Frames
# frame1 = Frame(root)
# frame1.pack(side=TOP)

# frame2 = Frame(root)
# frame2.pack(side=BOTTOM)

# Buttons
# button1 = Button(frame1, text='Clickme', fg='Red')
# button2 = Button(frame2, text='Clickhere', fg='Blue')
#
# button1.pack()
# button2.pack()

# l94 > Grids(need not pack) > Textfields - entry

# create firstname , lastname label

# labelfn = Label(root, text='Firstname')
# labelln = Label(root, text='Lastname')

# labelfn.pack()
# labelln.pack()


# Text fields entries

# entryfn = Entry(root)
# entryln = Entry(root)

# entryfn.pack()
# entryln.pack()

# Align these labels and text fields in grids

# labelfn.grid(row=0, column=0)
# labelln.grid(row=1, column=0)
#
# entryfn.grid(row=0, column=1)
# entryln.grid(row=1, column=1)
#
# button1 = Button(root, text='Ok', fg='Red')
# button1.grid(row=4, column=1)





# l95 > Self adjusting widgets - "Fill" keyword

# labelfn = Label(root, text='Firstname', bg='Red')
# labelln = Label(root, text='Lastname', bg='Yellow')
#
# labelfn.grid(row=0, column=0)
# labelln.grid(row=1, column=0)

# Autoadjusting widgets

# labelfn.pack(fill=X)
# labelln.pack(side=LEFT, fill=Y)

# entryfn = Entry(root)
# entryln = Entry(root)
#
# entryfn.grid(row=0, column=1)
# entryln.grid(row=1, column=1)



# l96 > button click event - Command keyword

# def buttonclick():
#     print('Firstname and lastname: ')
#
#
# buttonsubmit = Button(root, text='Submit', bg='Green', command=buttonclick())
# buttonsubmit.grid(row=2, column=1)


# l97 > Tkinter using classes

# class Myform:
#
#     def _init_(self, rootone):
#         frame1 = Frame(rootone)
#         frame1.pack()
#
#         labelfn = Label(frame1, text='Firstname', fg='Black')
#         labelln = Label(frame1, text='Lastname', fg='Blue')
#
#         labelfn.pack()
#         labelln.pack()
#
#         buttonsubmit = Button(frame1, text='Submit', bg='Green', command=self.buttonclick())
#         buttonsubmit.pack()
#         buttoncancel = Button(frame1, text='Cancel', bg='Red', command=frame1.quit)
#         buttoncancel.pack()
#
#     def buttonclick(self):
#         print('I\'m clicked ')
#
#
# form = Myform(root)


# l98 > Dropdown lists > menu > submenu > add_cascade(Menu) > add_Command

# class Mymenu:
#
#     def funcclick(self):
#         print('I\'m Clicked')
#
#     def _init_(self, rootone):
#         self.rootone = rootone
#
#     def menucreation(self):

        # creating Mainmenu

        # mainmenu = Menu(self.rootone)
        # self.rootone.config(menu=mainmenu)  # configured main menu to root

        # creating submenu

        # submenu1 = Menu(mainmenu)

        # adding File on main menu slab but over the submenu

        # mainmenu.add_cascade(label='File', menu=submenu1)

        # adding items to submenu1 now

        # submenu1.add_command(label='Project', command=self.funcclick())
        # submenu1.add_command(label='Save', command=self.funcclick())
        #
        # submenu1.add_separator()  # adds a grey line in menu
        #
        # submenu1.add_command(label='Exit', command=self.funcclick())

        # creating another submenu2

#         submenu2 = Menu(mainmenu)
#
#         mainmenu.add_cascade(label='Edit', menu=submenu2)  # adding Edit on main menu slab but over the submenu
#         submenu2.add_command(label='Undo', command=self.funcclick())
#         submenu2.add_command(label='Cut', command=self.funcclick())
#
#         submenu2.add_separator()
#         submenu2.add_cascade(label='Copy')
#
#
#
#
# manu = Mymenu(root)
# manu.menucreation()
#
# root.mainloop()   # holds the window
#

# Recap of Tkinter, Label, Text field, Frames, Grids, Buttons

# from tkinter import *

# root = Tk()

# Label root

# label1 = Label(root, text='Hello', bg='red')
# label2 = Label(root, text='Tkinter', bg='green')


# Fill keyword

# label1.pack(fill=X)
# label2.pack(side=LEFT, fill=Y)




# Text field root

# entry1 = Entry(root)
# entry2 = Entry(root)
#
# entry1.pack()
# entry2.pack()


# Frames

# frame1 = Frame(root)
# frame2 = Frame(root)
#
# frame1.pack(side='top')
# frame2.pack(side='bottom')

# Label frame

# label1 = Label(frame1, text='Hello')
# label2 = Label(frame2, text='Tkinter')
# label1.pack()
# label2.pack()

# Text field frame  - Entry

# entry1 = Entry(frame1)
# entry2 = Entry(frame2)
# entry1.pack()
# entry2.pack()

# Buttons frame

# button1 = Button(frame1, text='Stop', bg='red')
# button2 = Button(frame2, text='Ready', bg='Yellow')
#
# button1.pack()
# button2.pack()

# Button root

# button1 = Button(root, text='Stop', bg='red')
# button2 = Button(root, text='Ready', bg='Yellow')
#
# button1.pack()
# button2.pack()

# Grids - doesnt need packing

# On click command


# def submit():
#
#     print('Details are submitted')
#
#
# def cancel():
#
#     print('Cancelled')
#
# label1 = Label(root, text='Fname', bg='Blue')
# label2 = Label(root, text='Lname', bg='Green')
#
#
# label1.grid(row=0, column=0)
# label2.grid(row=1, column=0)
#
#
# entry1 = Entry(root)
# entry2 = Entry(root)
#
# entry1.grid(row=0, column=1)
# entry2.grid(row=1, column=1)
#
# button1 = Button(root, text='Submit', bg='grey', command=submit())
# button2 = Button(root, text='Cancel', bg='pink', command=cancel())
#
# button1.grid(row=3, column=0)
# button2.grid(row=3, column=1)


# classes using Tkinter
def submitok():
    print('I clicked a button')

def submitcancel():
    print('I/ve cancelled')

def submitprint():
    print('I/m printed')

def submitinsert():
    print('I/m inserted')

class applicationForm:

    def _init_(self, rootone):
        self.rootone = rootone

    def roottemplate(self):
        label1 = Label(self.rootone, text='Firstname', bg='Blue')
        label2 = Label(self.rootone, text='Lastname', bg='yellow')

        entry1 = Entry(self.rootone)
        entry2 = Entry(self.rootone)

        button1 = Button(self.rootone, text='Ok', bg='green')
        button2 = Button(self.rootone, text='Cancel', bg='red')

        label1.pack()
        label2.pack()
        entry1.pack()
        entry2.pack()
        button1.pack()
        button2.pack()


    def gridtemplate(self):
        label1 = Label(self.rootone, text='Firstname', fg='Black')
        label2 = Label(self.rootone, text='Lastname', fg='Black')

        entry1 = Entry(self.rootone)
        entry2 = Entry(self.rootone)

        button1 = Button(self.rootone, text='OK', bg='green', command=submitok())
        button2 = Button(self.rootone, text='Cancel', bg='red', command=submitcancel())

        label1.grid(row=0, column=0)
        label2.grid(row=1, column=0)

        entry1.grid(row=0, column=1)
        entry2.grid(row=1, column=1)

        button1.grid(row=2, column=1)
        button2.grid(row=2, column=2)

    def toolbar(self):
        # is a frame basically
        toolbar1 = Frame(self.rootone, bg='pink')
        printbutton = Button(toolbar1, text='Print', command=submitprint())
        insertbutton = Button(toolbar1, text='Insert', command=submitinsert())

        toolbar1.pack(side=TOP, fill=X)
        printbutton.pack(side=LEFT, padx=2, pady=3)
        insertbutton.pack(side=LEFT, padx=2, pady=3)

    def statusbar(self):  # is just a label - relief, bd, anchor
        statusbar1 = Label(self.rootone, text='statusbar', bd=1, relief=SUNKEN, anchor=W)
        statusbar1.pack(side=BOTTOM, fill=X)

    def messagebox(self):
        # showinfo, askquestion
        import tkinter.messagebox
        tkinter.messagebox.showinfo('Warning', 'This is a warning')

        orderresponse= tkinter.messagebox.askquestion('Your order', 'Would you like to have coffee?')
        if orderresponse == 'yes':
            print('A cup of cafe')
        else:
            print('No thanks!!!')

    def canvas(self):
        # for drawing purposes in tkinter
        canvas1 = Canvas(self.rootone, width=200, height=100)
        redline = canvas1.create_line(0, 0, 100, 100, fill='red')
        greenline = canvas1.create_line(10, 0, 0, 100, fill='green')
        blueline = canvas1.create_line(0, 100, 100, 100, fill='blue')
        canvas1.pack()


root = Tk()
appform = applicationForm(root)
# appform.roottemplate()
# appform.gridtemplate()
# appform.toolbar()
# appform.statusbar()
# appform.messagebox()
# appform.canvas()


root.mainloop()