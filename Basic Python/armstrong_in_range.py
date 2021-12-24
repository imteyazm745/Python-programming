for i in range(100):
    num =i
    result =0
    n=len(str(i))
    while(i!=0):
        digit = i%10
        result = result + digit**n
        i=i//10
    if num==result:
        print(num)
        """
output-
0
1
2
3
4
5
6
7
8
9
"""
