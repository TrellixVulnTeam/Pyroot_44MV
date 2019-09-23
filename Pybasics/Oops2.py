# Functional vs Object oriented programming

# Functional programming

def funprog():
    studname = input('Enter name')
    studage = input('Enter age')
    return studname, studage


print(funprog())


# Object oriented programming

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def user_put_data(self):
    #     self.name = input('Enter name')
    #     self.age = input('Enter age')

    def get_user_data(self):
        print(self.name + ',' + self.age)

    def para_put_data(self, name, age):
        self.name = name
        self.age = age

    def get_para_data(self):
        print(self.name + ',' + self.age)


Vig = Student("", "")
# Vig.user_put_data()
Vig.para_put_data('Vik', '30')
Vig.get_user_data()

