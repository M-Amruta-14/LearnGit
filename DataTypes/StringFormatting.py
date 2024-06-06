#To specify a string as an f-string, simply put an f in front of the string literal, like this:
# {}, a placeholder can contain variables, operations, functions, and modifiers to format the value.

age = 26
str = f"My age is {age}"
print(str)

# modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
# formatting can be done with or without a variable
str = f"Length is {34:.2f}"
print(str)

# Operations in F-String
# Math Operation
txt = f"The value is {2+5}"
print(txt)

# Math operation on variable
a = 4
b = 6
txt =  f"Percentage = {(a + b)/100}"
print(txt)

# if..else inside F_String
price = 49
txt = f"It is very {'Expensive' if price>40 else 'Chea0'}"
print(txt)

# Execute functions in F-String
name = "amruta"
txt = f"My name is {name.upper()}"
print(txt)

# String format()
ln = 5
wd = 2
rect = "Reactangle's length = {:.2f} width = {}"
print(rect.format(ln, wd))

rect = "Reactangle's length = {0} {1} width = {0}"
print(rect.format(ln , wd))

# named indexex
txt = "I am {name}"
print(txt.format(name  = "Amruta"))