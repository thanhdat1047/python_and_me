## countinuing
thislist = ["apple", "banana", "banana", "banana", "cherry"]

## Remove specified item
# If there are more than one item with the specified value,
# the remove() method removes the first occurrence:
thislist.remove("banana")
print(thislist)

# Remove specified index
# using pop() method
thislist.pop(2)
print(thislist)

# the del() also removes the specified index
del thislist[2]
print(thislist)

# Clear the list using clear()
thislist.clear()
print(thislist)

## Loop throught a list
thislist = ["apple", "banana", "banana", "banana", "cherry"]
# using for
for x in thislist:
  print(x)

# Loop through the index numbers
# using the range and len funcs to create a suitable iterable
for i in range(len(thislist)): 
  print(thislist[i])
  
# Using a while loop
i = 0
while i < len(thislist):
  print(thislist[i])
  i += 1
  
# Looping Using List Comprehension
# this is the shortest syntax for looping through lists
[print(x) for x in thislist]