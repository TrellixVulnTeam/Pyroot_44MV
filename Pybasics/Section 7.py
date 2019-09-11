# l60 > Functional programming > Implementation of functions in hierarchial manner

# Define everything as functions and pass functions as parameters
# Passing function as parameter to another parameter

# Simple function definition

# def add_10(x):
#     return x+10

# Using function as parameter for function

# def twice_function(func,arg):
#     return func(func(arg))
#
# print(twice_function(add_10,10))

# Function recap

# Simple function

# def add(x,y):
#     return x+y
#
# print(add(2,2))

# Function calling function

# def add(x,y):
#     return x+y
#
# def square(x):
#     return x**2
#
# print(square(add(2,2)))

# Complex function using function as parameter arguements
# this function accepts another function as parameter

# def add_ten(x):
#     return x+10
#
# def twice_add_ten(funcpara,arg):
#     return funcpara(funcpara(arg))
#
#
# print(twice_add_ten(add_ten,10))

# Program flow => funcpara = add_10 , 10 is the thing to be added twice => Simple

# ***********



# l61 > Lambdas |||lr to function but doesn't have a name / anonymous function > no return statement
# Functions can have return statement , lambda need not !!!


# result = (lambda x: x**2)(2)
# print(result)

#1

# print((lambda cube: cube**3)(int(input())))

#2

# user_input = int(input())
# print((lambda addx: addx+2)(user_input))

#3

# print((lambda y: y-5)(10))

# **********

# l62 > Map > allows to perform operations using functions/lambdas on iterables (list)

# numlist = [10, 20, 30, 40, 50]

# Map using func and list
# def add2(x):
#     return x+2
#
# numlistv1 = list(map(add2,numlist))
# print(numlistv1)

# Map using lambdas and list

# numlistv2 = list(map((lambda x: x*5), numlist))
# print(numlistv2)

# operate on iterables without using map

# def mfunction():
#     i = 0
#     for x in numlist:
#         numlist[i] = (x*2)
#         print(numlist[i])
#         i += 1
#     return 0
#
# checkm = mfunction()
# print(numlist)


# l63 > Filters are > Functions used with lambdas FiLters > filtering based on criteria from iterables

# numlist = [1, 3, 5, 7, 9, 11, 13, 15, 2, 4, 6, 8, 10, 12, 14]

# lets filter this list as odd and even no > filter(function, iterable)

# evenlist = list(filter(lambda x: x%2 == 0, numlist))
# oddlist = list(filter(lambda y: y%2 != 0, numlist))
#
# print('Evenlist', evenlist)
# print('Oddlist', oddlist)

# l64 > Generators |||r to list , tuples > uses a function and yield keyword generates the number with while, for loop

# Generate list of numbers upto 100 using while loop

# def num_100():
#     counter = 0
#     while counter <= 100:
#         yield counter
#         counter += 1
#
# list100 = list(num_100())
# print(list100)

# Generate list of even numbers upto 100
#
# def evennum(i):
#
#     for x in range(i):
#         if x % 2 == 0:
#             yield x
#
#
# print(list(evennum(100)))

# Recap Lambda, Maps, Filter, Generators

# Lambda > anonymous function

# lambda v1.0
# print((lambda x: x**2)(2))

# lambda v1.1
# print('Enter user input for lambda')
# print((lambda y: y+2)(int(input())))

# Maps > maps operations on iterables
# Maps using func

# maplist = list(range(10, 100, 10))
# print(maplist)
#
# def multx2(x):
#     return x*2
#
# print(list(map(multx2,maplist)))

# Maps using lambdas
# print(list(map((lambda x: x+2), maplist)))

# FiLters - Functions / lambdas used with iterables to filter values

# numlist = list(range(1, 10, 1))
# print(numlist)
#
# def funfilter(x):
#     if x % 2 == 0 :
#         print('Even', x)
#     else:
#         print('Odd', x)
#         return x
#
# print(list(filter(funfilter, numlist)))

# Filters using lambdas

# print(list(filter((lambda xeven: xeven % 2 == 0), numlist)))
# print(list(filter((lambda xodd: xodd % 2 != 0), numlist)))

# Generators > generates list using function , yield keyword

# def evennos(x):
#     for x in range(x):
#         if x % 2 == 0:
#             yield x
#
# print('List of even nos', list(evennos(100)))

# l65> Coding challenge
# Assume you want to build two functions for discounting products on a website.
# Function number 1 is for student discount which discounts the current price to 10%.
# Function number 2 is for additional discount for regular buyers which discounts an
# additional 5% on the current student discounted price.

# def stud_discount(cp):
#     dis = cp * 0.10
#     studprice = cp - dis
#     return studprice
#
# def regularcust_discount(studfunc, cp):
#     discountprice1 = studfunc(cp)
#     regcustprice = discountprice1 - (discountprice1*0.05)
#     return regcustprice
#
# print('Enter the price of the prod:')
# currentprice = float(input())
# print('Enter type of customer:')
# customer = input()
# if customer == 'student':
#    studprice_discounted = stud_discount(currentprice)
#    print('Price after stud discount', studprice_discounted)
# elif customer == 'regular':
#     regcusprice_discounted = regularcust_discount(stud_discount, currentprice)
#     print('Price after stud discount', regcusprice_discounted)

# l67 > lambda
# Calculate the value of mathematical expression x*(x+5)^2 where x= 5 using lambda expression.

# print((lambda x: x*(x+5) ^ 2)(5))

# l69 > Map
# Consider a list in Python which includes prices of all the items in a store.
# Build a function to discount the price of all the products by 10%.
# Use map to apply the function to all the elements of the list so that all the product prices are discounted.

# prodprices_list = list(range(100, 1100, 100))
# newprodprice_list = list(map((lambda x: x - (x*0.1)), prodprices_list))
# print(newprodprice_list)
