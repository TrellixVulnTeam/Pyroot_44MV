# child class inheriting properties and methods of the parent class


class Student:      # base class
    def __init__(self, name, age):  # default initializer
        self.name = name
        self.age = age

    # setter
    def setstuddata(self, name, age):
        self.name = name
        self.age = age

    # getter
    def getstuddata(self):
        print('Student name & age:', self.name + ',' + self.age)


class Science(Student):  # derived class
    def __init__(self, enrolled):
        self.enrolled = enrolled

    def setenrolldata(self, enrolled):
        self.enrolled = enrolled

    def getenrolldata(self):
        self.getstuddata()          # accessing base class methods in derived class
        if self.enrolled == 'yes':
            print('Student enrolled in Science')
        elif self.enrolled == 'maybe':
            print('Student might enroll')
        else:
            print('Student not enrolled')


sci = Science('')
sci.setstuddata('Vig', '29')
sci.setenrolldata('yes')
sci.getenrolldata()
