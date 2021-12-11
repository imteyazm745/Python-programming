#python progrm to check the string is palindrome or not
string = input(("Enter a string : "))
if(string==string[::-1]):
    print("The string is a palindrome")
else:
    print("The string is not palindrome")

"""
Enter a string : stats
The string is a palindrome

Enter a string : madam
The string is a palindrome

Enter a string : Imteyaz
The string is not palindrome
"""
