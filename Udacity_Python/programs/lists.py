>>> empty=[]
>>> empty
[]
>>> letters=['a','b','c','d']
>>> numbers=[1,2,3]
>>> both=['a', 1, 'b', 2, 'c', 3]
>>> nested=[letters, numbers]
>>> nested
[['a', 'b', 'c', 'd'], [1, 2, 3]]
>>> numbers
[1, 2, 3]
>>> numbers.append(4)
>>> numbers.append(5)
>>> numbers
[1, 2, 3, 4, 5]
>>> numbers[2]
3
>>> numbers[-2]
4
>>> letters[2]
'c'
>>> numbers[::-1]
[5, 4, 3, 2, 1]
>>> numbers
[1, 2, 3, 4, 5]
>>> letters[::-1]
['d', 'c', 'b', 'a']
>>> numbers
[1, 2, 3, 4, 5]
>>> numbers[1]=100
>>> numbers
[1, 100, 3, 4, 5]
