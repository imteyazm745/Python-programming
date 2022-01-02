class Room:
    def __init__(self, fname, lname, age):
        self.fname=fname
        self.lname=lname
        self.age=age



hamza = Room('Hamza' ,'alam', 22)
sarfaraz = Room('Mohammad' ,'sarfaraz' , 24)
print(hamza.fname, sarfaraz.fname)
print(hamza.lname, sarfaraz.lname)
print(hamza.age, sarfaraz.age)
print(sarfaraz.fname, sarfaraz.lname, sarfaraz.age)
print(hamza.fname, hamza.lname, hamza.age)
"""
Hamza Mohammad
alam sarfaraz
22 24
Mohammad sarfaraz 24
Hamza alam 22
"""
