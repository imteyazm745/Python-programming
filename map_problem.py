# Practice with map
# Fill out the rest of the map functions.
# You can define additional functions if you need to.
# (a) ["apple", "orange", "pear"] => (5, 6, 4)  (length)
# (b) ["apple", "orange", "pear"] => ("APPLE", "ORANGE", "PEAR")  (uppercase)
# (c) ["apple", "orange", "pear"] => ("elppa", "egnaro", "raep")  (reversed)
# (d) ["apple", "orange", "pear"] => ("ap", "or", "pe")  (first two letters)
 
def reverse(s):
    return s[::-1]
 
def two_alpha(s):
    return s[:2]
 
a = map(len, ["apple", "orange", "pear"])
b = map(str.upper, ["apple", "orange", "pear"])
c = map(reverse, ["apple", "orange", "pear"])
d = map(two_alpha, ["apple", "orange", "pear"])
 
