# will contain the recollection of all the concepts
# brush up topics

# - basics -

# string_input = input()
# int_input = int(input())
# print(string_input*2)   # string * int works fine
# print(int_input*2)      # int * int works fine
# escape sequence \


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


# - List , List operations -

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


astring = 'alpha'
print('Before mutation', astring)
immutstr(astring)
print('After mutation', astring)

print('Before mutation try ', numlist)
mutlis(numlist)
print('After mutation try', numlist)











