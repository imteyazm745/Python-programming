#Python Program to print all numbers in a Range Divisible by a Given Number
lower=int(input("Enter lower range limit : "))
upper=int(input("Enter upper range limit : "))
n=int(input("Enter a number to be divided by : "))
for i in range(lower,upper+1):
    if(i%n==0):
         print(i)
"""
Output:-
Enter lower range limit : 1
Enter upper range limit : 50
Enter a number to be divided by : 5
5
10
15
20
25
30
35
40
45
50
"""
