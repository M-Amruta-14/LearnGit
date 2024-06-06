# a collection which is ordered and changeable. Allows duplicate members.

List = ["Apple", "Mango", "Banana"]
print(List)

# to determinr how many items in List.
print(len(List))

List1 = [1, 2, 3, 4]
print(List1)

# list can contain diff data types also
List2 = ["My", 23, 9.08]
print(List2)

#From Python's perspective, lists are defined as objects
# with the data type 'list':
print(type(List2))

# list() constructor
Const = list(("A", 3, "D"))
print(Const)

# Access Items
print(List[1])

#Negative indexing means start from the end
print(List[-1])

#When specifying a range, the return value will be a new list with the specified items.
print(List[1:3])

#By leaving out the start value, the range will start at the first item:
print(List[:2])

#By leaving out the end value, the range will go on to the end of the list:
print(List[2:])