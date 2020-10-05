# j = 0


# def standup(day):
#     global j
#     sbo3_list = ['Florian', 'Georg', 'Simon', 'Manuel', 'Ion', 'Raul', 'Flaviu', 'Vig']
#     if not ((day.startswith('Sa')) or (day.startswith("Su")) & j == 8):
#         # if j < 8:
#         print('Todays standup presenter:' + day + sbo3_list[j])
#         j += 1
#     elif j == 8:
#         j = 0
#
#     print('Current j local value:', j)
#
#
# days_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# for i in range(len(days_list)):
#     standup(days_list[i])
#
#
# print('Global j value:', j)

def count_bits(n):
    r = []
    q = n//2           # 2
    remainder = n % 2  # 0
    r.append(remainder)
    count = 0
    while q != 0:
        remainder = q % 2  # 0
        r.append(remainder)
        q = q//2  # 1
    print(r)
    for x in r:
        if x == 1:
            count += 1
    return count


# binary_count = count_bits(0)
# print(binary_count)

def square_digits(num):

    digit_list = [int(x) for x in str(num)]
    squared_list = list(map((lambda sq: sq**2), digit_list))
    clubbed_list = ''.join([str(x) for x in squared_list])
    return int(clubbed_list)

# print(square_digits(45678))


def get_sum(a, b):
    total = 0
    result = 0
    if not(a == b):
        for x in range(a, b):
            print(x)
            total += x
        result = total + b
    elif a == b:
        result = a

    return result


# print(get_sum(-5, 5))

def find_short(s):
    split_list = s.split()
    len_list = []
    print(split_list)
    for i in range(len(split_list)):
        len_list.append(len(split_list[i]))
    print(len_list)
    len_list.sort()
    return len_list[0]


# print(find_short("bitcoin take over the world"))

def to_camel_case(text):
    split_list = text.split("_")
    for i in range(len(split_list)):
        while not(split_list[0]):
            print(split_list[i].capitalize())
    return split_list





print(to_camel_case("the_stealth_warrior"))
 # to_camel_case("the-stealth-warrior")











