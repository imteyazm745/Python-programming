 #Write a program in Python to check if a number is prime.
  
a=int(input("enter number"))
if a=1:
   for x in range(2,a):
         if(a%x)==0:
          print("not prime")
   break
   else:
      print("Prime")
else:
   print("not prime")
    
"""Output:
enter number 3
Prime
"""
