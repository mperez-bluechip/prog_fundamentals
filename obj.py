""" The Blueprints for Jeans """

# class jeans:
#
#     def __init__(self, waist, length, color):
#         self.waist = waist
#         self.length = length
#         self.color = color
#         self.wearing = False
#
#     def put_on(self):
#         print('Putting on {}x{} {} jeans'.format(self.waist, self.length, self.color))
#         self.wearing = True
#
#
#     def take_off(self):
#         print('Taking off {}x{} {} jeans'.format(self.waist, self.length, self.color))
#         self.wearing = False

""" Two Names, One Shirt """

class shirt:

    def __init__(self):
        self.clean = True

    def make_dirty(self):
        self.clean = False

    def make_clean(self):
        self.clean = True
