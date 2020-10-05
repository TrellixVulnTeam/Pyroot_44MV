# l72 > Object oriented programming
# Functions in func programming, methods in OOP
# attributes are variables(key parameters) of the class
# class > attributes(use dunders) > methods


class Students:
    # attribute initializer using dunders
    def _init_(self, name, contact):
        self.name = name
        self.contact = contact

    def setdata(self):
        print('Setting data')
        self.name = input('Enter student name: ')  # setting using user input here
        self.contact = input('Enter student contact: ')

    def setdata1(self, name, contact):
        print('Setting data1')
        self.name = name
        self.contact = contact

    def getdata(self):
        print('Getting data')
        print('Student name: '+self.name)
        print('Contact: ', self.contact)

# Object creation


# Vig = Students('Vig', 0) # intializes attributes with these initial values
# Vig.getdata()  # prints the default values passed above
# Vig.setdata()  # sets the user input values
# Vig.getdata()  # gets the user input values

# Teacher class
# class Teacher:
#     def _init_(self, tname, tcontact):
#         self.tname = tname
#         self.tcontact = tcontact
#
#     def setter(self):
#         print('Setting up teachers details')
#         self.tname = input('Enter teachers name:')
#         self.tcontact = input('Enter teachers contact:')
#
#     def getter(self):
#         print('Teacher name:'+self.tname)
#         print('Teacher contact: ', self.tcontact)
#
# David = Teacher('Blank', 0)
# David.setter()
# David.getter()

# l73 > inheritance


class Sciencestudent(Students):  # inherits from Students
    def _init_(self,regno):    # attribute initializing
        self.regno = regno

    def getterscience(self):
        print('Registration no of scistudent: ', self.regno)


# Bruce = Sciencestudent(2060)
# Bruce.getdata()  # wont work as there's nothing to get - Vig object has the data Bruce obj doesnt have any for now
# Bruce.setdata1('Bruce', '9444')  # setting it with parameters upfront, setting with Bruce obj data
# Bruce.getdata()  # works fine now as there is some data set
# Bruce.getterscience()


# l74 > recursion - function factorial calling itself - function call in the function definition

# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         # print('Debug', factorial(x))
#         return x * (factorial(x-1))
#
# print(factorial(4))


# l75 > Sets > collections |||r to list > elements are unique in Sets
# > add, remove keywords > union(|), intersect(&), diff(-)

# dupnumbset = {1, 2, 3, 5, 5, 6, 7, 8, 9, 10}   # doesnt consider the duplicate 5
# print(dupnumbset)
#
#
# numbset1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# numbset1.add(11)
# print('After adding an element ', numbset1)
# numbset1.remove(11)
# print('After removing an element', numbset1)

# numbset2 = {7, 8, 9, 10, 11, 12, 13, 14, 15, 16}
# print('After union ', numbset1 | numbset2) # duplicate elements are removed automatically
# print('Intersect', numbset1 & numbset2)  # prints common elements in the set
# print('Difference', numbset1 - numbset2) # prints difference of the sets

# l76 > itertools > module in python > count, accumulate, takewhile

from itertools import count, accumulate, takewhile

# keeps counting upto infinity

# for i in count(5):
#     print(i)
#
#     if i >= 20:
#         break


# accumulates the values of the list to previous accumulated element values and creates a list

numlist = list(range(1,6,1))
print(numlist)

accumulatedlist = list(accumulate(numlist))
print('Accumulating the values in list')
print(accumulatedlist)

# takewhile similar to filter

# print('Takewhile list', list(takewhile((lambda x: x < 10), accumulatedlist)))
# print('Filtered list', list(filter((lambda x: x >= 10), accumulatedlist)))


# l77 > Operator overloading - add, sub > use of inbuilt str function

class Coordinates:
    def _init_(self, x, y):
        self.x = x
        self.y = y

    def setcoordinates(self, x, y):
        self.x = x
        self.y = y

    def getcoordinates(self):
        print('x coordinate', self.x)
        print('y coordinate', self.y)

    # predefined function for operator overloading
    def _add_(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Coordinates(x, y)

    # predefined str function
    def _str_(self):
        return "({0},{1})".format(self.x, self.y)


# coordinate0 = Coordinates(0, 0)

# print('I\'m the default cooridnate ', coordinate0.getcoordinates()) -

# coordinate1 = Coordinates(2, 4)

# print('I\'m the 1st cooridnate ', coordinate1.getcoordinates()) -

# coordinate2 = Coordinates(3, 5)

# print('I\'m the 2nd cooridnate ', coordinate2.getcoordinates()) -

# print(coordinate1 + coordinate2)


# operator overloading - Sub
class Point:

     def _init_(self, x, y ):
         self.x = x
         self.y = y

     def setpoints(self, x, y):
         self.x = x
         self.y = y


     def getpoints(self):
         return self.x, self.y

     def _sub_(self, other):
         x = self.x - other.x
         y = self.y - other.y
         return Point(x, y)

     def _str_(self):
         return "({0},{1})".format(self.x, self.y)

# position1 = Point(7,9)
# print('Position1 points: ', position1.getpoints())
# position2 = Point(5,3)
# print('Position2 points:', position2.getpoints())
# print('Position3 points - overloaded: ', position1 - position2)
# print(position1 - position2)


# string format template

# print('Date format: {d}/{m}/{y} '.format(d=30, m=3, y=2018))

# l78 - Encapsulation - Data hiding - OOPS facilitates - prefix with __

class Myclass:

    def _init_(self):
        self.__privattribute = 0
        self.publicattribute = 0

    def modify(self, inc):
        self.__privattribute += inc
        self.publicattribute += inc
        # print(self.__privattribute, self.publicattribute)


# objectclas = Myclass()
# objectclas.modify(5)
# print('Trying to access public attribute:', objectclas.publicattribute)
# print('Trying to access private attribute:', objectclas.__privatattribute) # fires a private attribute error

# l79 > Coding challenge > parent class cant access child class methods > initializer are very important and compulsory
# Using the concept of object oriented programming and inheritance,
# create a super class named Computer, which has two sub classes named Desktop and Laptop.

class Computer:
    def _init_(self,ram, hd, graphic):
        self.ram = ram
        self.hd = hd
        self.graphic = graphic

    def getspecs(self, ram, hd, graphic):
        print('Getting the specs from Computer object')
        self.ram = ram
        self.hd = hd
        self.graphic = graphic

    def displayspecs(self):
        print('Displaying the computer specs below: ')
        return self.ram, self.hd, self.graphic

class Desktop(Computer):

    def _init_(self, processor):
        self.processor = processor

    def getprocessor(self, processor):
        print('Getting the processor from Desktop object')
        self.processor = processor

    def displayprocessor(self):
        print('Displaying processor from Desktop below: ')
        return self.processor


class Laptop(Computer):

    def _init_(self, weight):
        self.weight = weight

    def getweight(self, weight):
        print('Getting the weight from Laptop object')
        self.weight = weight

    def displayweight(self):
        print('Displaying weight for laptop below: ')
        return self.weight


# Compobj = Computer('4gb', '1TB', 'AMD')

# Deskobjectproc = Desktop('Quadcore')
# Deskobjectproc.getspecs('4gb', '1TB', 'AMD')  # for the Computer class- child class accessing parent class methods
# print(Deskobjectproc.displayspecs())
# print(Deskobjectproc.displayprocessor())
#
# Laptopobject = Laptop(3)
# Laptopobject.getspecs('8gb', '2TB', 'AMDrad') # for the Computer class- child class accessing parent class methods
# print(Laptopobject.displayspecs())
# print(Laptopobject.displayweight())
#
# Compobj = Computer('blank', 'empty', 'null')
# Compobj.getspecs('16gb', '4TB', 'nvidia')
# print(Compobj.displayspecs())

# l81 > Coding challenge > Operator overloading
# > class > initializer > getter setter > inbuilt operator func > inbuilt str function

class Mult:

    def _init_(self, x, y):
        self.x = x
        self.y = y

    def setter(self, x, y):
        print('Setting values: ')
        self.x = x
        self.y = y

    def getter(self):
        return self.x, self.y

    def _mul_(self, other):
        x = self.x + other.x
        y = self.y + other.y

        # x = self.x * other.x
        # y = self.y * other.y

        # return Mult(x, y) ---

        return x, y
        # return self.x+other.x, self.y+other.y

    # def _str_(self): ---
    #     return "Mult: {0}, {1}".format(self.x, self.y)


prod1 = Mult(2, 2)
prod2 = Mult(3, 3)
prod3 = (prod1 * prod2)  # calling mult operator but it does add inside
print(prod3)
