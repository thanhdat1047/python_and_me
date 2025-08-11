fruits = ("apple", "banana", "cherry")

# Unparking tuple
(a, b, c) = fruits
print(a,b,c)
# Note: The number of variables must match the number of values in
# the tuple, if not, you must use an asterisk to collect the 
# remaining values as a list.

# Using Asterisk *
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red) # ['cherry', 'strawberry', 'raspberry']

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)