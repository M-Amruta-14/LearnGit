'''
String is an Array, Python has no char data type,
so even a single character is treated as a string
'''

a = "Hi, Amruta"
print(a[4])
print("\n")

'''
Looping through a string
'''

for s in "Apple":
    print(s)
print("\n")

#to Get length of a string

a = "Amruta"
print(len(a))
print("\n")

# to check certain Phrase or character is in string
txt = "I am learning Python"
print("Python1" in txt)
print("Python" in txt)

# to check certain Phrase or character is not in string
txt = "I am learning Python"
print("Python1" not in txt)
print("Python" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

print("\n")

# Slice of the string
b = "Hello, Amruta"
print(b[2:8])

# slice from start
print(b[:6])

# slice to the end of string
print(b[1:])

# -ve indexes to start the slice from end of the string
# but this is not working as expected
print(b[-2: 6])