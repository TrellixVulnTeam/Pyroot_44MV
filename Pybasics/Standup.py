j = 0


def standup(day):
    global j
    # j = 0
    sbo3_list = ['Florian', 'Georg', 'Simon', 'Manuel', 'Ion', 'Raul', 'Flaviu', 'Vig']
    if not((day.startswith('Sa') or day.startswith('Su')) or j == 8):
        # if j < 8:
        print('Todays standup presenter:' + day + " " + sbo3_list[j])
        j += 1
    elif j == 8:
        j = j-8
    print('Current j local value:', j)


days_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday','Monday', 'Tuesday',
             'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
for i in range(len(days_list)):
    standup(days_list[i])


# print('Global j value:', j)
