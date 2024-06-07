"""
#Global Variable

x = "WOW"

def myFunc():
    x = "O3"
    print("Skin Product name is " + x)

myFunc()

print("Skin Product name is " + x)
"""

#Global Keyword
#x="O3" will not affect the value of X, as global X decalred in function
x = "O3"
def myFunc():
    global x
    x = "WOW"

myFunc()
print("Skin Product name is " + x)
