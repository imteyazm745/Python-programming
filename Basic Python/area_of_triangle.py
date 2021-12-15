a = float(input("Enter firste side of triangle : "))
b = float(input("Enter second side of traingle : "))
c = float(input("Enter third side of triangle : "))
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("area of traingle is %0.3f"%area)

"""
Enter firste side of triangle : 4
Enter second side of traingle : 5
Enter third side of triangle : 3
area of traingle is 6.000
"""
