n=int(input("Enter a number : "))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("Reverse of the number is : ", rev)

#output-
#Enter a number : 687
#Reverse of the number is :  786