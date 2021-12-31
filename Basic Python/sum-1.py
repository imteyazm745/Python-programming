#write a python program to calculate the sum of three given numbers, if the values are given then return thrice of their sum.
def sum_thrice(x,y,z):
    sum = x + y + z

    if x==y==z:
        sum = sum *3    
    return sum
print(sum_thrice(1,2,3))
print(sum_thrice(3,3,3))

"""
Output:- 
6
27
"""
