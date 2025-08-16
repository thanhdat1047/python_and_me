thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple2 = ("apple",)  # tuple
print(type(thistuple2))
thisnottuple = ("apple") # str
print(type(thisnottuple)) 

thistuple3 = tuple(("apple",))
print(thistuple3)
print(type(thistuple3))

print(thistuple[1])

# Range of index
print(f"range {thistuple[1:2]}")

# How to change item of tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "banana2"
x = tuple(y)
print(x)

# Add item to tuple
# No1: covert to list
z = list(x)
z.append("cherry2")
x = tuple(z)
print(x)
# No2: Add tuple to a tuple
z2 = tuple(("cherry3",))
x += z2
print(x)

# remove 
z3 = list(x)
z3 = [item for item in z3 if item not in ["cherry2", "cherry3"]]
x = tuple(z3)
print(x)

# clear 
del x