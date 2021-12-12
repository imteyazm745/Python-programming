# Python program to read a number n and Print the series "1+2t....tn="
n = int(input("Enter a number : "))
a = []
for i in range(1,n+1):
        print(i,sep=" ",end=" ")
        if(i<n):
            print("+",sep=" ",end=" ")
        a.append(i)
print("=",sum(a))
print()

"""
Enter a number : 4
1 + 2 + 3 + 4 = 10

Enter a number : 6
1 + 2 + 3 + 4 + 5 + 6 = 21
"""
