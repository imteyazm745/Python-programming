lower=int(input("Enter the lower limit for the range : "))
Upper=int(input("Enter the upper limit for the range : "))
for i in range(lower,Upper+1):
    if(i%2!=0):
        print(i)
"""
output 
Enter the lower limit for the range : 1
Enter the upper limit for the range : 15
1
3
5
7
9
11
13
15

"""
