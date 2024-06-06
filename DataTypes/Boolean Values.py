b =  10
d = 9

if b > d :
    print("b is greater")
else :
    print("d is greater")

'''
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.
'''
print(bool("Hello"))
print(bool(1))

# print yes if function returns tru
def myFunc():
    return True

if myFunc():
    print("Yes !")
else:
    print("No !")

# Python also has many built-in functions that return a boolean value,
# like the isinstance() function, which can be used to determine if an object is of a certain data type:
# Check if an object is an integer or not:
x = 200
print(isinstance(x, int))