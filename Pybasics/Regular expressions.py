# This section will handle the deep dive into the regular expression module
# pattern and the raw string
# match method, search method - in re module
# match method - checks from the beginning of the raw string

import re

# match method

match_string = 'abc'
match_pattern = 'a'

if re.match(match_pattern, match_string):
    print('match pattern found in the string')
else:
    print('match pattern not found in the string ')

# search method

search_string = 'baba'
search_pattern = 'a'

if re.search(search_pattern, search_string):
    print('search pattern found in the string')
else:
    print('search pattern not found in the string')


# metacharacters - * , +, {}, . , ? , ^

# * - character preceding * needs to be present 0 or more times

star_string = 'abbc'
star_pattern = 'ab*c'

if re.match(star_pattern, star_string):
    print('star pattern matches with star string')
else:
    print('star pattern doesnt matches with star string')


# + - character preceding + needs to be present atleast once in the raw string
plus_string = 'acbccc'
plus_pattern = 'ab+c'

if re.match(plus_pattern, plus_string):
    print('plus pattern matches with plus string')
else:
    print('plus pattern doesnt matches with plus string')

# {} - specifies the exact number of repeatation , has to be the same number or more but not less

braces_string = 'abbbb'
braces_pattern = r'ab{3}'   # r represents the raw string

if re.match(braces_pattern, braces_string):
    print('braces pattern matches with braces string')
else:
    print('braces pattern doesnt match with the braces string')

# . - wildcard character - . can take place any symbol

wild_string = 'a!?b'
wild_pattern = r'a..b'

if re.match(wild_pattern, wild_string):
    print('wild pattern matches with the wild string')
else:
    print('wild pattern doesnt match with the wild string')

# ? optional meta character ? - character preceding ? is optional - doesnt matter if it exists or not

optional_string = 'vig123'
optional_pattern = r'vig_?123'

if re.match(optional_pattern, optional_string):
    print('optional pattern matches with the optional string')
else:
    print('optional pattern doesnt match with the optional string')

# ^ caret meta character - represents the string should start with the string if ^ precedes

caret_string = "9444235163"
caret_pattern = r'^9'

if re.match(caret_pattern, caret_string):
    print('caret pattern matches with the caret string')
else:
    print('caret pattern doesnt match with the caret string')

# character class -1
# \d - represents digits,  \D- non digit character,  \w- alphanumeric

digit_string = '1234'
alpha_string = 'abcd'
alphanum_string = 'vig89'

d_character_pattern = r'\d'
a_character_pattern = r'\D{5}'
an_character_pattern = r'\w'

if re.match(d_character_pattern, digit_string):
    print('digit string matches the digit pattern')

if re.match(a_character_pattern, alpha_string):
    print('alpha string matches the non digit pattern ')

if re.match(an_character_pattern, alphanum_string):
    print('alphanum string matches alphanum pattern')


# character class -2
# []
# python Python
character_string = 'Aython'
character_pattern = r'^[a-zA-Z]ython'

if re.match(character_pattern, character_string):
    print('character string matched with pattern')
else:
    print('No match found with pattern')
