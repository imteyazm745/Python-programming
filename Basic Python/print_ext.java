#write a python program to accept a filename from the user and print the extension of that
filename = input("Input the filename : ")
f_ext = filename.split(".")
print("The extension of the file is : "+repr(f_ext[-1]))
"""
Input the filename : aba.java
The extension of the file is : 'java'
"""
