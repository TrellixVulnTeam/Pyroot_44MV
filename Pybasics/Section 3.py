# Section 3 Statements


# l13> if else statement
# ***

# Adult determination based on age

# Age = int(input('Enter the age\n'))
#
# if Age >= 18:
#     print('Adult Age')
# else:
#     print('Kids age')

# *****

# l14> elif statement
# ****

# Simple Grading System

# Marks = int(input('Enter the score \n'))
# if Marks >= 90:
#     print('Grade A+')
# elif Marks >= 80:
#     print('Grade A')
# elif Marks >= 70:
#     print('Grade B')
# elif Marks >= 60:
#     print('Grade C')
# elif Marks >= 50:
#     print('Grade D')
# else:
#     print('Grade Failed')

# *****

# l15>List,l16-List operations > Lists (Similar to arrays- collection of similar data types)
# *****

# List
# numbers = [1, 2, 3, 4, 5]
# names = ['Vig', 'Ara', 'Tha', 'Sud']
# print(numbers)
# print(names)

# Accessing data in List
# print(names[3])

# Modifying data in the list
# names[3] = 'Ani'
# print(names)

# *******

# List operations
# namenos = names + numbers
# print(namenos)
# namemult = names * 2
# print(namemult)

# ****

# Using in keyword in list
# Armusic = ['24', 'ATM', 'VTV', 'AYM']
# print('24' in Armusic)
# Fruits = ['Apple', 'Orange', 'Banana', 'Watermelon']
# print('Fruits in ')
# print('Apple' in Fruits)

# ********

# statements recap
# Homenumber = int(input('Enter my home number \n'))
# if Homenumber == 14:
#     print('My Homenumber matches')
# elif Homenumber == 16:
#     print('My new Homenumber matches')
# else:
#     print('Homenumber doesn\'t match')

# ********

# l17>List functions > append, len, index, insert
# Friends = ['Vig', 'Tha', 'Ara', 'Sud']
# print(Friends)

# Appending a value to the list
# Friends.append('Ank')
# print(Friends)

# Finding length of the list - length counts from 1 while list from 0
# strlen = len(Friends)
# print(strlen)

# Inserting a value in the list
# Friends.insert(4,'T')
# print(Friends)

# Index of a value in the list - starts with 0
# print(Friends.index('T'))

# List recap

# numberseven = [0, 2, 4, 6, 8, 10]
# numbersodd  = [1, 3, 5, 7, 9, 11]
#
# print(2 in numberseven)
# print(9 in numberseven)
#
# print(numberseven*2)
# numbers = numberseven+numbersodd
# print(numbers)

# *****

# l18 > Range functions > basically a child of list

# numberrange = list(range(0,101,5))
# print(numberrange)
#
# numberevenrange = list(range(0,11,2))
# print(numberevenrange)
#
# numberoddrange = list(range(10,30,3))
# print(numberoddrange)

# l19 > codereuse and functions > functions are placeholders for chunks of code

# def profile(): # function definition
#     print('Vignesh \nMasters \n29 \nDatascientist')
#
# print('Given below are the profile details')
# profile() # function call
# lr = list(range(1,11))
# print(lr)

# *****

# l20 > For loop > use of for loop with list, range etc

# fruits = ['apple', 'mango', 'kiwi', 'Grapes', 'orange']
# for x in fruits:
#     print(x)

# for x in range(1,6):
#     x += 1
#     print(x)

# for x in range(0,21):
#     if x % 2 == 0:
#         print(x)
#     else:
#         print('Not an even number')
#         print(x)

# ******

# function and for loop recap
# def creds():
#     print('Solid mechanics')
#     print('Informatik')
#     print('Math module')
#
#
# print('Student needs 20 cred\'s in module\'s below for Masters')
# creds()
#
# numlist = list(range(1,5))
# for x in numlist:
#     print(x)
#     if (x%2 == 0):
#         print('Even module')
#     else:
#         print('odd module')

# **********

# l21 > Boolean logic > and, or
# print('Enter the username \n')
# Username = input()
#
# print('Enter the password \n')
# Password = input()
#
# if Username == 'Vig' and Password == 'Infy':
#     print('Login success for ', Username)
# else:
#     print('Invalid creds')
#
# if Username == 'Vig' or Username == 'vig' and Password == 'Infy':
#     print('Login success for ', Username)
# else:
#     print('Invalid creds')


# *********

# l22 > While loop

# counter = 0
# while counter <= 10:
#
#     print(counter)
#     counter += 1

# ********