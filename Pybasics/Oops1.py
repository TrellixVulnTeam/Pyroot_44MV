# choc teddy bear mould - class
# choco teddy bears created - objects
# attributes - properties of the objects -weight,color, taste of the content poured in the teddy mould
# method - belongs to a particular class only


class Teddy:
    quantity = 200   # attribute

    def __init__(self, name, color):       # self is reference to that particular object itself- current instance teddy1
        self.name = name                   # teddy1.name = darkchoc , teddy2.name= vanilla
        self.color = color                 # teddy1.color= brown , teddy2.color = white
        # color is an attribute

    # implementing methods in class
    def change_name_color(self):
        print('changing the attributes of the objects')
        self.name = 'Ted'
        self.color = 'Pink'

    def change_name_color_para(self, nam, col):
        self.name = nam
        self.color = col


teddy1 = Teddy("darkchoc", "brown")     # object1
print(teddy1.name, teddy1.quantity, teddy1.color)
teddy1.change_name_color()
print('After changing attribute through method:' + teddy1.name, teddy1.color)

teddy2 = Teddy("vanilla", 'white')      # object2
print(teddy2.name, teddy2.quantity, teddy2.color)
teddy2.change_name_color_para('Ted1', 'yellow')
print('After changing attribute through method:' + teddy2.name, teddy2.color)


