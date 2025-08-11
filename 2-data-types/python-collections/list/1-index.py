# The list() constructor
# Using the list() constructor to make a List:

thislist = list(("a", "b", "c", "d", "e", "i"))
print(type(thislist))
print(len(thislist))

## Access item
print(thislist[1])

## Negative indexing - start from the end
### -1 refers to the last items
print(thislist[-1])

## Range of index 
print(thislist[-1:]) # lasted item

# Change Item Value
thislist[1] = "a"
# Change a range of item values
thislist[0:2] = ["z", "z"]

# Insert more items than u replace
# the new items will be inserted where you specified
# and the remaining items will move accordingly:
thislist[1:2] = ["y", "n"]

# If you insert less items than you replace
# the new items will be inserted where you specified
# and the remaining items will move accordingly:
thislist[1:3] = ["1"]

# Insert items
thislist.insert(2, "C")

# Append items
thislist.append("lastest")
thatlist = list((1, 2, 3))

thislist.extend(thatlist)
# any iterable
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
















print(thislist)