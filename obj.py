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

# """ Two Names, One Shirt """
#
# class shirt:
#
#     def __init__(self):
#         self.clean = True
#
#     def make_dirty(self):
#         self.clean = False
#
#     def make_clean(self):
#         self.clean = True

""" You Can Change an Outfit, But You Can't Change Your Words """

# create a closet full of clothes
closet = ['shirt','hat','pants','jacket','socks']
print(closet)
print(id(closet))

# remove a hat

closet.remove('hat')
print(closet)
print(id(closet))

# create a poor choice of words
words = "You're wearing that"
print(words)
print(id(words))

# add more to the phrase
words = words + ' because you look great!'
print(words)
print(id(words))
