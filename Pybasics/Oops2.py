# Functional vs Object oriented programming

# Functional programming


def funprog():
    studname = input('Enter name')
    studage = input('Enter age')
    return studname, studage


# print(funprog())


# Object oriented programming

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def user_put_data(self):  # sets the data
        self.name = input('Enter name')
        self.age = input('Enter age')

    def para_put_data(self, name, age):  # sets the data from the args passed
        self.name = name
        self.age = age

    def get_user_data(self):   # gets the data set
        print(self.name + ',' + self.age)


Vig = Student("", "")
Vig.user_put_data()
print('User date from user')
Vig.get_user_data()
Vig.para_put_data('Vik', '30')
print('User data from args')
Vig.get_user_data()


