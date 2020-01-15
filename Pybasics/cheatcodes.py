# will contain the recollection of all the concepts
# brush up topics

# Topics checklist
# loops - if else , while, for x in range
# List [] , append, len(), insert, index , list compre
# File handling - filehandler = open(read/write/append mode) , filehandler.read, filehandler.write
# try , except, finally
# Dictionary {} - word meaning pair - give the word get meaning - in , get keyword
# Tuples () - tuple slicing
# string ops - .format , upper, lower, startswith , endswith , join , replace
# lambdas template - (lambda x: x**2)(2)
# MFG - Map(func/lambda, iterable)
#       Filter(func/lambda, iterable)
#       Generator - yield keyword
# Count - Accumulate - Takewhile(lambda, iterable)
# re - ^, $, *,{}, ?- optional, . -wild , + - atleast once

# - basics -

# string_input = input()
# int_input = int(input())
# print(string_input*2)   # string * int works fine
# print(int_input*2)      # int * int works fine
# escape sequence \

# ----------------------------------------------------------------------------

# - loops -
# if elif else statement

# vacation = input()
# if vacation == 'italy':
#     print('Destination Italy')
# elif vacation == 'uk':
#     print('Destination United kingdom')
# elif vacation == 'spain':
#     print('Destination spain')
# else:
#     print('Destination India')

# for loop

# for x in range(0, 10):
#     print(x)

# while loop

# count = 1
# while count <= 10:
#     print(count)
#     count += 1
#
# print(count)

# - Boolean logic --
# and or

# user_id = input()
# location = input()
#
# if user_id == 'vig' or location == 'de':
#     print('user_id matched')
# elif user_id == 'Vig' and location == 'DE':
#     print('user_profile matched')

# -------------------------------------------------------------------

# - List , List operations - List compre

evennum_squarelist = [x**2 for x in range(0, 10) if x % 2 == 0]
# print(evennum_squarelist)

import re

ballondor_list = ['Messi', 'Ronaldo', 'Messi10', 'Messiy', 'CR7']
messipattern = 'Messi?'    # wildchar metacharacter

messicompre_list = [x for x in ballondor_list if re.match(messipattern, x)]
# print(messicompre_list)

# List [ bracket - List index starts with 0
# List operations - len() - .insert - .index - .append
# in keyword
# List operations numlist * 2, numlist + numlist
# string immutable , List mutable

numlist = [1, 2, 3, 4, 5]
alphalist = ['a', 'b', 'c', 'd', 'e']




# string immutable list mutable

def immutstr(astring):
    astring = 'newalpha'
    print('Tried to mutate to', astring)
    return astring


def mutlis(nlist):
    print('Received numlist', nlist)
    nlist.append(6)
    print('Mutated to ', nlist)
    return nlist


# astring = 'alpha'
# print('Before mutation', astring)
# immutstr(astring)
# print('After mutation', astring)

# print('Before mutation try ', numlist)
# mutlis(numlist)
# print('After mutation try', numlist)

# -------------------------------------------------------


# passing one function to another

def add(a, b):
    return a+b


def square(c):
    return c**2


# power = square(add(2, 2))
# print(power)

# ------------------------------------------------

# try , except , finally
# try something - except something - finally

# try:
#     a = 10
#     b = 0
#     c = a/b
#     print(c)
# except ZeroDivisionError:
#     print('Looks like a Zerodivision Error')
# finally:
#     print('Denominator is zero')

# --------------------------------------------------

# file handling - read , write , append mode

# read
# file_handler = open('demo.txt', 'r')
# file_content = file_handler.read()
# print(file_content)
# file_handler.close()
# file_handler = open('demo.txt', 'r')
# file_contentline = file_handler.readline()
# print(file_contentline)
# file_handler.close()

# write - removes the existing content

# file_handler = open('demo.txt', 'w')
# file_write = file_handler.write('Hi this is line 4 write')
# file_handler.close()

# append mode

# file_handler = open('demo.txt', 'a')
# file_append = file_handler.write('\nHi this is line 5 append')
# file_handler.close()

# -------------------------------------------------------------

# Data structures - List(alii), Dictionary(ig) , Tuples
# List -[] , Dictionary - {}, Tuples - ()
# List operations - .append, len(), .insert , index - "in" keyword

# Dictionary - word-meaning concept , key-value concept
# Dictionary - "get" keyword , "in" keyword
# key is the priority - the one that comes before : is the key and the other is the pair

friendsage_dict = {'Vig': 30, 'Tha': 27, 'Ara': 26, 'Sud': 30}
friends_list = ['Vig', 'Tha', 'Ara', 'Sud']
friends_tuples = ('Vig', 'Tha', 'Ara', 'Sud')

# Dictionary concepts

# print('Age of Sudharshan', friendsage_dict['Sud'])
# print('Age of Thanu', friendsage_dict.get('Tha'))
# print('Check if Aravind age is in the dict?', 'Ara' in friendsage_dict)
# friendsage_dict['Ani'] = 27
# print('Inserting a new key value pair', friendsage_dict)

# List slicing - count starts from 0 ends to n+1

# print(friends_list[0:4])  # prints 0 to n-1
# print(friends_list[1:])   # Tha to Sud
# print(friends_list[:2])   # Vig to Tha -, n-1
# print(friends_list[0:4:2])  # jump - Vig to Ara - skips Tha


# Tuple slicing  - count starts from 0 and ends with n+1

# print('Tuples', friends_tuples[0:4])
# print(friends_tuples[0:])   # prints Vig - Sud
# print(friends_tuples[:3])   # prints Vig - Ara
# print(friends_tuples[0:4:2])  # jumps Tha Vig-Ara

# -----------------------------------------------------------------------------------


# string operations - .format, .join , .replace, .endswith .startswith, upper , lower

# .format

# doj = '{y}/{m}/{d}'.format(d=4, y=2019, m=11)
# print(doj)

# .format from a list

# idmelist = ['194767', 'Vignesh', 'Sys Engineer', 'Mysore', 'Infosys']
# idmestring = 'Emp id# {} - Name {} - Designation {} - Location {} - Company {}'.format(idmelist[0], idmelist[1],
#                                                                                        idmelist[2], idmelist[4],
#                                                                                        idmelist[3])
# print(idmestring)
#
# datelist = [4, 11, 2019]
# datestring = '0{}/{}/{}'.format(datelist[0], datelist[1], datelist[2])
# print(datestring)


# join - joins after each literal / letter of the string / list

literal_1 = ['J', 'o', 'i', 'n']
string1 = 'Join'

string2 = 'e'.join(literal_1)
string3 = 'e'.join(string1)
# print(string2)                 # Jeoeien
# print(string3)                 # Jeoeien

# replace

# literal_2 = 'Join'
# string4 = literal_2.replace('J', 'C')
# print(string4)                  # Coin
# string5 = 'Hello'.replace('H', 'E')
# print(string5)                  # Eello

# starts with , ends with - case sensitive

# sw_string = 'check mate'
# ew_string = 'check_mate'
# print(sw_string.startswith('check'))  # true
# print(ew_string.endswith('Mate'))     # false


# upper, lower

# caps_string = 'CheckmatE'
# print(caps_string.upper())         # CHECKMATE
# print(caps_string.lower())         # checkmate


# min , max, abs

numlist = [100, 200, 300, 400, 500]
negativeval = -100

# print(min(numlist))  # 100
# print(max(numlist))  # 500
# print(abs(negativeval))  # 100

# ----------------------------------------------------------------------------------------


# Functional programming - passing functions to functions, lambdas

# passing one function to another function
# adding 10 twice to the input parameter


def add_ten(x):
    return x+10


def add_twice_ten(functionarg, parameterarg):
    return functionarg(functionarg(parameterarg))

# need to 5 twice to 10 => 25


# print('Added 10 twice to 5:', add_twice_ten(add_ten, 5))


# lambdas - anonymous functions - use the keyword lambda

# power2 = (lambda x: x**2)(2)
# print(power2)

# print((lambda cube: cube**3)(int(input())))   #27

# --------------------------------------------------------

# operations using func/lambdas on iterables - Map makes the work easy rather than conventional func manipulation

# function
def add_two(x):
    return x+2


list1 = [1, 2, 3, 4, 5]

list1_1 = list(map(add_two, list1))
# print('Mapped new list with func', list1_1)

list1_2 = list(map((lambda x: x+2), list1))
# print('Mapped new list with lambda', list1_2)

list1_3 = []


def mfunction(listn):
    print(len(listn))
    for x in range(0, len(listn)):
        list1_3.append(int(listn[x]) + 2)
    return list1_3


# print(mfunction(list1))

# ---------------------------------------------------------------

# FiLters - Func / Lambdas used on iterables to filter values

eveodd_list = list(range(1, 11))

# Lets filter the above iterable list using filter

# with function


evenlist = list(filter((lambda eve: eve % 2 == 0), eveodd_list))
oddlist = list(filter((lambda odd: odd % 2 != 0), eveodd_list))
# print('Entire list elements', eveodd_list)
# print('Filtered even list elements', evenlist)
# print('Filtered odd list elements', oddlist)

# ----------------------------------------------------------------------

# Generators - generates iterables with yield keyword and a function


def oddgenerator(i):
    for x in range(i):
        if x % 2 != 0:
            yield x


oddlist = list(oddgenerator(20))
# print(oddlist)

# -------------------------------------------------------------------------

# Sets - unique collections - add, union | , intersect & , diff -
set1 = {1, 2, 3, 4, 5, 5}
set2 = {6, 6, 7, 8, 9, 10}
# print(set1)      # {1, 2, 3, 4, 5} - removes duplicate

set1.add(6)
# print(set1)      # {1, 2, 3, 4, 5, 6}

set3 = set1.union(set2)
# print(set3)   # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

set4 = set1.intersection(set2)
# print(set4)          # 6

set5 = set1.difference(set2)
# print(set5)        # {1, 2, 3, 4, 5}

# ---------------------------------------------------------------

# iterables keywords - Count, Accumulate, TakeWhile - CAT


from itertools import count, accumulate, takewhile

# count
# for i in count(10):
#     print(i)             # [10-21]
#     if i > 20:
#         break

# Accumulated list - makes the accumulation to previous elements

a_list = list(range(0, 11, 1))
# print(a_list)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

acc_list = list(accumulate(a_list))
# print(acc_list)        # [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55]

# takewhile
# print('Takewhile', list(takewhile((lambda x: x < 10), acc_list)))     # [0, 1, 3, 6]




# ------------------------------------------------------------------


# Regular expression

import re

# match , search , sub , findall , characterclass, metacharacters - *, ?, ^, $, {}, .

# match - checks the raw string for match at start
match_string = 'abc'
match_pattern = 'c'

# if re.match(match_pattern, match_string):
#     print('matched')     # a
# else:
#     print('not matched')  # b , c


# search
search_string = 'babab'
search_pattern = 'b'

# if re.search(search_pattern, search_string):
#     print('search clicked')    # ab , b
# else:
#     print('search unclicked')  # c

# findall
fa_string = "EnemyFriendsEnemyfriendsFriendsEnemy"
fa_pattern = r"Friends"

# print(re.findall(fa_pattern, fa_string))       # Friends, Friends - case sensitive
# if re.search(fa_pattern, fa_string):
#     print('searched true')                        # true
# else:
#     print('searched false')

# string replace - re module sub function
string1 = "vig"
string2 = string1.replace("vig", "vigi")
# print(string2)     # vigi

string3 = 'Hi I\'m Vig'
sub_pattern = r"Vig"
string4 = re.sub(sub_pattern,"Vigi", string3)
# print(string4)        # Hi I'm Vigi

# Characterclass - [a-zA-z] , /d - digits numeric , /D - alpa, /w - alphanumeric

digit_string = '1234'
alpha_string = 'abcd'
alphnum_string = 'a12b'

digit_pattern = r'\d'
alpha_pattern = r'\D{5}'
alphanum_pattern = r'\w'

# if re.match(digit_pattern, digit_string):
#     print('digit string')
# if re.match(alpha_pattern, alpha_string):
#     print('alpha string')
# if re.match(alphanum_pattern, alpha_string):
#     print('alpha num')

# metacharacters

# ^ starting  , $ ending, * repeat, {} exact no of repetition  , ? optional char, . wild char, + - atleast once

# ^ - starts with
caret_string = '9444235163'
caret_pattern = r'^9'

# if re.match(caret_pattern, caret_string):
#     print('string begins with 9')   # ^9
# else:
#     print('string doesnt begin with 9')  # ^8

# $ ends with - NOT SURE HOW IT WORKS
dollar_string = 'ch!'
dollar_pattern = r"^[a-z][A-Z]!$"

# if re.match(dollar_pattern, dollar_string):
#     print('Ends with !')
# else:
#     print('Doesnt End with !')

# * - repeat one or more times
star_string = "eggseggsbreadeggs"
star_pattern = 'eggs*'

# if re.match(star_pattern, star_string):
#     print('Eggs repeat')
# else:
#     print('Eggs doesnt repeat')

# {} - exact no of times
braces_string = "suckfucksuckfuckfuck"
braces_pattern = r"suckfuck{2}"

# if re.search(braces_pattern, braces_string):
#     print('repeats one time')   # {1}
# else:
#     print('didnt seem to repeat')  # {2}

# ? - optional character
quest_string = "Hihello"
quest_pattern = r"^Hi!?[a-z][A-Z]*"

# if re.match(quest_pattern, quest_string):
#     print('pattern matched')
# else:
#     print('pattern didnt match')

# . - wild char
dot_string = "Hey?you"
dot_pattern = "^[A-Z][a-z]*.you$"

# if re.match(dot_pattern, dot_string):
#     print('wild char matched')              # matched
# else:
#     print('wild char didnt match')

# + - atleast once
plus_string = 'abbccdd'
plus_pattern = '^[a-z]*b+'

# if re.match(plus_pattern, plus_string):
#     print('plus pattern matched')
# else:
#     print('plus pattern didnt match')


# ---------------------------------------------------

# object oriented programming

class Student:

    def __init__(self, name, age):   # default initializer
        self.name = name
        self.age = age

    def set_user_input(self):
        self.name = input()
        self.age = input()

    def set_para_studinput(self, name, age):
        self.name = name
        self.age = age

    def getter_student(self):
        print('Studentname - age', self.name + '-' + self.age)


class StudentStream(Student):    # child class inheriting from parent class

    def __init__(self, stream):  # default child class initializer
        self.stream = stream

    def set_para_strinput(self, stream):
        self.stream = stream

    def getter_stream(self):
        print('Student stream', self.stream)

# Lets initialize and create objects


# Vig = StudentStream('Mech')     # child class object - can access parent class mathods
# Vig.set_para_studinput('Vignesh', '29')
# Vig.getter_student()
# Vig.getter_stream()


Tha = Student('Thanu', '27')    # parent class object initialization - cant access child class methods
Tha.getter_student()

# --------------------------------------

# Data analysis - Jupyter notebooks

# from pandas import *
# import numpy as np
# Series - Dataframes
# series_num = Series([1,2,3,4,5], index=[1,2,3,4,5])# data_set = {'Name':['Vi', 'Th','Ar'],
# data_set = {'Name':['Vi', 'Th','Ar'], 'Age':[29,27,26], 'Uni':['FAU','FAU','FAU']}
# dataframe_set = DataFrame(data_set, index=[1,2,3,4])

# ------------------

# keywords #

# reindex - reshuffle the index of the elements, rows
# .T - transpose of the dataframe
# drop - .drop(3) - .drop('column name', 1)
# operations - series1 + series2 # needs to have the same index
# dataframe1 - dataframe2
# sort - sort_index, sort_index(ascending=False) , sort_values('Age', ascending = False)
# unique - is_unique (for elements), index.is_unique(for index)
# sum - sum(Series) , dataframe.sum()
# idxmax, idxmin
# np.array([]) - .reshape(x,y)
# arange, zeros
# linspace, logspace
# indexing after reshaping - []array []row []column

















