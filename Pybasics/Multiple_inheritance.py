# Understanding multiple inheritance


class A:
    def a_method(self):
        print('Method from class A')


class B:
    def b_method(self):
        print('Method from class B')


class C(A, B):                      # inherits from both A & B
    def c_method(self):
        print('Method from class C')


c_object = C()
c_object.a_method()     # accessing method from A class
c_object.b_method()     # accessing method from B class
c_object.c_method()     # accessing method from C class


# multilevel inheritance
# class B(A):
# class C(B):
# object creation and method access will hold the same as above with multiple inheritance

