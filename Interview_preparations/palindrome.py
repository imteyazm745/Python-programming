#Write a program in Python to check if a sequence is a Palindrome.

a=input("enter sequence")
b=a[::-1]
if a==b:
  print("palindrome")
else:
  print("Not a Palindrome")

#Output: enter sequence 323 palindrome

