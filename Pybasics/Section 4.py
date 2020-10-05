# l28 > Functions
# Pass by ref - depends on the data type which can be mutable(list) and immutable(string)
# Mutable list


def list2(list1):
    print('got',list1)
    list1.append('5')
    print('mutated to ', list1)

list1 = ['1', '2', '3', '4']

print('before mutation', list1)
list2(list1)
print('after mutation', list1)

# immutable string


def immu2_string(immu1_string):
    print('got', immu1_string)
    immu1_string = 'Hello'
    print('tried to mutate ', immu1_string)


immu1_string = 'Hi'
print('before trying to mutate ', immu1_string)
immu2_string(immu1_string)
print('after tried to mutate', immu1_string)

# *******

# l29 > Functions return


# def add(a,b,c,d):
#     sum = a + b
#     concat = c + d
#     return sum , concat
#
#
# result = add(100, 200, 'Vig', 'Rav')
# print(result)

# ******

# l30 > Passing function as arguement to another function
#
# def add(a,b):
#     return a+b
#
#
# def square(c):
#     return c*c
#
# power = square(add(2,2))
# print(power)

# *******

# l31 > Module - piece of code written by others(libraries) / inbuilt modules as well
# random module

# import random
#
# for x in range(5):
#     print(random.randint(1,6))

# *********

# l32 > Coding challenge > Functions
# BMI calculator  BMI = (weight in Kg)/(Height in Meters)^2.
# Write python code which can accept the weight and height of a person and calculate his BMI.

# Function definition

# def BMI(w, h):
#     bmi = w/h**2
#     return bmi

# arguements

# print('Enter user weight')
# weight = float(input())
# print('Enter user height')
# height = float(input())

# Function call

# Bodymassindex = BMI(weight, height)
# print('BMI of the user: ', Bodymassindex)