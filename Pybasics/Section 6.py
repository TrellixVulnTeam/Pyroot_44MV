# l47 > Data structures - Dicitionaries (Word - meaning |||r Key - value in python)

# peopleage = {'Vig': 29, 'Tha': 27, 'Ara': 26}
# print(peopleage['Vig'])

# *********

# l48 > Dictionary function , get keyword

# friendslist = {1: 'Vi', 2: 'Th', 3:'Ar'}
# print(friendslist)
# print(friendslist[1])
#
# print(peopleage['Vig'], friendslist[1])
# print(1 in friendslist)  # checks for the key value not the pair
# print(friendslist.get(2)) # gets the pair value in the dictionary
#
# print(peopleage.get('Sud','Not in the friends list ')) # custom output statement from the dictionary

# *********

# l49 > Tuples - are immutable >can't be modified !!!

# List [] , Dictionary {} , Tuples ()
# Friendlist = ['Vig', 'Ara', 'Tha']
# Friendtuple = ('Vig', 'Ara', 'Tha')
# Friendsdict = {'Vig', 'Ara', 'Tha'}
# print('Tuples', Friendtuple)
# Friendlist[1] = 'Ani'
# Friendlist.insert(3,'Sud')
# print('Friendlist after insert', Friendlist)
# Friendlist.append('Ank')
# print('Friendslist after append ', Friendlist)
# print('Ank stands at ', Friendlist.index('Ank'))
# print('Length of the Friendlist ', len(Friendlist))

# ************

# l50 > List,Dictionary,Tuple slicing

# Friendlist = ['Vig', 'Ara', 'Tha', 'Ani', 'Ank','Sud']
# Friendtuple = ('Vig', 'Ara', 'Tha', 'Ani', 'Ank','Sud')
# Frienddict = {'Vig': 1, 'Ara': 2, 'Tha': 3, 'Ani': 4, 'Ank': 5,'Sud': 6}
#
# print('Slicing in list ', Friendlist[0:5])  # n-1
# print('Slicing in list jump ', Friendlist[1:5:2])  # jump
# print('Slicing in list end', Friendlist[2:])  # 2nd pos to end
# print('Slicing in list start', Friendlist[0:]) #1st pos to end
#
# print('Slicing in tuple ', Friendtuple[1:5+1])
# print('Slicing in tuple jump ', Friendtuple[1:6:2])
# print('Slicing in tuple end', Friendtuple[:4])
#
#
# print('Vis' in Frienddict)  # prints true or false
# print(Frienddict.get('Vis', 'NA in Friendsdict'))  # prints the cons statement when false

# *************

# l51 > ListComprehension  > fills the list with certain logic/rules

# Listcompre = [x**2 for x in range(0,6) if x % 2 == 0]
# print(Listcompre)

# Data structures recap - Dictionary, Tuples, List, List compre, Slicing

# Dictionary - key pair - Slicing not possible in dicitonary - get keyword
# friendsdict = {1: 'Vig', 2: 'Tha', 3: 'Ara', 4: 'Sud'}
# print(friendsdict[3]) # prints the pair value
# print(friendsdict.get(1)) # gets the pair value
# print(friendsdict.get('Vig','Can\'t be found'))

# Tuples - Immutable data structures

# Friendstuple = ('Vig', 'Tha', 'Ara', 'Sud')
# print(Friendstuple)

# Slicing tuples

# print(Friendstuple[1:])  # count starts from zero prints to the end
# print(Friendstuple[:3])  # prints from the start to end-1
# print(Friendstuple[1::2])  # jumps

# List - Mutable data structures

# Friendslist = ['Vig', 'Tha', 'Ara', 'Sud']
# print(Friendslist)
# Friendslist.insert(3, 'Ani')
# print('After insert ', Friendslist)
# Friendslist.append('Ank')
# print('After append', Friendslist)
# print(len(Friendslist))
# print(Friendslist.index('Ank'))

# List comprehension

# Comprelist = ['Messi','Ronaldo','Modric','Neymar']
# Listcompre1 = [x for x in Comprelist]
# print(Listcompre1)
#
# Listcompre2 = [x**2 for x in range(1, 5)]
# print(Listcompre2)

# Listcompre3 = [x**3 for x in range(1,5)]
# print(Listcompre3)


# ************

# l52> String formatting > .format keyword

# datelist = [30, 1, 2019]
# print(datelist)
# datestring = '{0}/{1}/{2}'.format(datelist[0], datelist[1], datelist[2])
# print(datestring)

# idlist = [194767, 'Sys Engineer', 'Infy', 'Mysore', 206, '19-09-11']
# print(idlist[0])
# idstringformat = \
# 'Infy tag:{0}-{1}-{2},Location-{3},Room-{4},Doj-{5}'.format(idlist[1],idlist[0],idlist[2],idlist[3],idlist[4],idlist[5])
# print(idstringformat)

# dojformat = 'DOJ={d}/0{m}/{y}'.format(d=19, m=9, y=2011)
# print(dojformat)

#
# stringformat = 'Division:{a}/{b}'.format(a=10, b=5)
# print(stringformat)

# ************

# l53> String functions - .format, Join , Replace, startswith, endswith, upper, lower

# format
# Stringformat = 'Date:{d}/0{m}/{y}'.format(d=30, m=1, y=2019)
# print(Stringformat)
#
# Listformat = [30, 1, 2019]
# Stringformat = 'Date:{0}/0{1}/{2}'.format(Listformat[0],Listformat[1],Listformat[2])
# print(Stringformat)

# join

# Numlist = ['H', 'E', 'L', 'L', 'O']
# Stringjoin = '?'.join(Numlist)
# print(Stringjoin)

# replace

# Stringreplace = Stringjoin.replace('?', '!')
# print(Stringreplace)
#
# Stringreplace2 = 'Hello'.replace('e', 'a')
# print(Stringreplace2)

# startswith endswith
# Stringstart = 'Fuck you!!!'
# print(Stringstart.startswith('Fuck'))
# print(Stringstart.endswith('.'))

# Upper # lower

# Stringupperlower = 'Fuck you'
# print(Stringupperlower.upper())
# print(Stringupperlower.lower())


# String ops - format,join,replace,startswith,endswith,upper,lower

# format

# skillsetlist = ['ML','AI','Datasets','DL','Neuralnets']
# skillstring= \
#     'Myskills:Exp{0}-Beginner{1},Basic{2},Exp{3},Exp{4}'.format(skillsetlist[0],skillsetlist[1],skillsetlist[2], skillsetlist[3],skillsetlist[4])
# print(skillstring)
# killstring = 'Myskills:Exp {M}-Beginner {A},Basic {D},Exp {Da},Exp {N}'.format(M='ML',A='AI',D='DL',Da='Data',N='Neural')
# print(killstring)

#join strings

# stringgreet = 'Hello'
# stringnew = stringgreet + '!'
# print(stringnew)

#join string to list

# stringlist = ['H','E','L','L','O']
# stringlist.append('!')
# print(stringlist)
# newstring = '?'.join(stringlist)
# print(newstring)


# replace

# replacestring = newstring.replace('?','!')
# print(replacestring)

# startswith, endswith , upper, lower

# stringcheck = 'Fuckyou'
# print(stringcheck.startswith('F'))
# print(stringcheck.endswith('u'))
# upperstring = stringcheck.upper()
# lowerstring = stringcheck.lower()
# print(upperstring)
# print(lowerstring)

# ************

# l54> Numeric functions> min,max,abs

# numlist = [1, 2, 3, 4, 5]
# print('min of the list', min(numlist))
# print('Max of the list', max(numlist))

# absnum = -100
# print(abs(absnum))

# ************

# l55 > Coding challenge 7 > Dictionary

# Write Python code which accepts name of a product and in turn returns their respective prices.

# productprice_dictionary = {'Dairymilk': 50, 'Lindt': 40, 'Tob': 30, 'Rittersport': 20, '5star': 10}
#
# print('Userinput productname')
# productname = input()
#
# if(productname in productprice_dictionary):
#     print('Price of the product: ', productname,':',productprice_dictionary[productname])
# else:
#     print('product not available in the dicitonary')

# print('List of product and price :',productprice_dictionary)
# print('Price of Lindt: ', productprice_dictionary['Lindt'])
# print('Check if prod exists: ', productprice_dictionary.get('Truffle','Doesnt exist'))
# print('Chek if prod exists:', 'Kitkat' in productprice_dictionary)

# Coding challenge - Dictionary

# Dictprodlist = {'Milk': 10, 'Bread': 5, 'Butter': 2, 'Chocolates': 1, 'Meat': 3}
# prodname = input()
# if prodname in Dictprodlist:
#     print(prodname, 'Price', Dictprodlist[prodname], 'Exists in the store')
# else:
#     print(prodname, 'Doesn\'t Exists in the store')

# inserting into Dict

# Dictprodlist['Bun'] = 4
# print(Dictprodlist)
# print('Length of the Proddict list', len(Dictprodlist))

# *****

# l57 > coding challenge 8 > List

# List out  all the odd numbers from 1 to 100 using lists in Python.

# Numlist = list(range(1, 100, 1))
# print(Numlist)
# print(1 in Numlist)

# for counter in range(0,99):
#     if Numlist[counter] % 2 != 0:
#         print('Odd: ', Numlist[counter])
#         counter += 1
#     else:
#         print('')

# ************