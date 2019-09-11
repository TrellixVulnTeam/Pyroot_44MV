# l84 > Regular expressions > manipulate strings > Django will need this
# re module > match > search & find all
# > To verify email address patter etc

import re  # reg exp module

# pattern = r'Vig'
#
# if re.match(pattern, 'Ravindran Vigneshwaran'):  # for match string and pattern start should be alike
#     print('Match found')
# else:
#     print('Match not found')  # string start should have the same as in the pattern


# l85 > search and find all

patternsearch = r'friends'  # case sensitive

# if re.search(patternsearch, 'EnemyfriendsEnemyfriendsEnemyfriends'):
#     print('Match found')
# else:
#     print('Match not found')
#
#
# print('search all string', re.findall(patternsearch, 'EnemyFriendsEnemyfriendsEnemyfriends'))

# >l86 Find and replace

# string replace keyword recap

# name = 'Vig'
# newname = name.replace('Vig', 'Vik')  # strings are immutable ?

# or

# print(name.replace('Vig', 'Vigi'))
# print('Name string after replace', newname)

# Find and replace => re module > sub function

# mystring = 'Hi I\'m Vig, My name is Vig'
# pattern = r'Vig'
# newstring = re.sub(pattern, 'Vigi', mystring)
# print(newstring)

# l87 > metacharacter > dot ., $(end), caret ^(start), star


# pattern = r"^gr.y$"
#
# print('Enter user string: ')
#
# if re.match(pattern, input()):
#     print('User string start with gr and end with y')
# else:
#     print('User string doesnt start with gr and end with y')

# l88 > character class [] - character class

# emailpattern = r"[A-Z][0-9]@[A-Z]*.com$"
#
# useremail = input()
# # if re.search(emailpattern, useremail):
# if re.match(emailpattern, useremail):
#     print(useremail)
# else:
#     print('Match not found')

# l89 > * star metacharacter - doesnt consider the repeatation of characters of before it

# l90 > Groups ()

# breakfastpattern = r'breads(eggs)*bacon'  # if * doesnt exist bf1 and bf2 wont match
# bf = ['breadsbacon', 'breadseggseggsbacon', 'breadseggsbacon'  ]
# # print(bf[0])
# # print(len(bf))
#
# for i in bf:
#     if re.match (breakfastpattern, i):
#         print('Match found, bf pattern: ', i)
#     else:
#         print('Match not found, bf pattern: ', i)