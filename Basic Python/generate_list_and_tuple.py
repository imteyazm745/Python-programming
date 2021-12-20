#write a python program which accepts a sequence of comma-seperated numbers from user and generate a list and a tuple with those numbers.
values = input("Input some seperated numbers : ")
list = values.split(",")
tuple = tuple(list)
print("list :" , list)
print('Tuple : ', tuple)
"""
Input some seperated numbers : 3,5,7,32
list : ['3', '5', '7', '32']
Tuple :  ('3', '5', '7', '32')
"""
