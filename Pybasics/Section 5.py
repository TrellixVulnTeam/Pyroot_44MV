# l35 > Errors & Exceptions

# Syntax error , logical error
# Exception - terminates the program > Divide by zero

# l36 > Exception
# try  except

# try:
#     a = 10
#     b = 0
#     c = a/b
#     print(c)
#
# except ZeroDivisionError:
#     print('Divide by zero error ')

# ************

# l37 > Try except finally

# try:
#     a = 10
#     b = 10
#     print(a/b)
#
# except ZeroDivisionError:
#     print('Divide by zero error')
#
# finally:
#     print('I\'l be executed no matter what')

# *************

# l38 l39 l40 > file handling, file read, file write
# read content

# filehandle = open("demo.txt", 'r')
# filecontent = filehandle.read()
# filecontentline = filehandle.readline()
# print(filecontent)
# print(filecontentline)
# filehandle.close()

# write content

# filehandle = open("demo.txt",'w')
# filehandle.write('This is line3')
# filehandle.close()
#
# # append content
# filehandle = open("demo.txt",'a')
# filehandle.write('\nThis is line4')
# filehandle.close()

# ***********

# file handling recap

# filereader = open('demo.txt','r')
# print(filereader.read())
# # print(filehandler.readline())
# filereader.close()
#
# filewriter = open('demo.txt','w')
# filewriter.write('I\'m writing in my file')
# filewriter.close()
#
# fileappender = open('demo.txt','a')
# fileappender.write('\nI\'m writing line2 my file')
# fileappender.close()

# **************

# try except finally block

# try:
#     a = 10
#     b = 0
#     c = a/b
#
# except ZeroDivisionError:
#     print('Tried to divide by zero')
#
# finally:
#     print('I print finally')

# ***************

# l43 > Coding challenge > try except finally block

# Write a function which would divide two numbers, design the function in a manner that it handles the divide
# by zero exception.

# try:
#     print('User input a ')
#     a = int(input())
#     print('User input b')
#     b = int(input())  # input accepts as string and needs to be converted to int
#     print('Division value: ', a//b)
# except ZeroDivisionError:
#     print('b can\'t be zero')
# finally:
#     print('User entered values are: ', a, b)

# **************

# l44> coding challenge > file handling
# 1. Write Python code to open a file named demo.txt and write some random data into it.
filehandler = open('demo1.txt', 'r')
print(filehandler.read())
filehandler.close()

# 2. Write python code to add additional text to the existing file on a new line without deleting the previous contents.
filehandler = open('demo1.txt', 'a')
filehandler.write('I will write without deleting the contents\n')
filehandler.close()