#1. Left Triangle Star Pattern In Python

# Solution 1 : using while loop
i =1
while i<=5:
    print(i*'*')
    i = i +1

# Solution 2 : using for loop
n = 5
for i in range(1, n+1):
    print("*" * i)  
    
"""
Output 
*
**
***
****
*****
"""

# 2. Left triangle star pattern
size = 5
for i in range(1, size+1):
    print(" " * (size - i) + "*" * i)

"""
    *
   **
  ***
 ****
*****
"""
