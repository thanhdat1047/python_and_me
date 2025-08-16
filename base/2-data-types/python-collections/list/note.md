# list are used to store multiple items in a single variable
# list are one of 4 built-in data types in  Python used to store collections of data, the orther are Tuple, Set, Dictionary all with defferent qualities and usage. 

# List are created using square brackets:


## List items 
### List items are ordered, changeable and allow duplicate values.
### List items are indexed, the first item has index [0]

### Ordered
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list.
# `Note` : There are some list methods that willl change the order, but in general the order of the items will not change


### Changeable
# The list is changeable, meaning that we can change, add, remove items in a list after it has been created

### Allow Duplicates
# Since list are indexed, lists can have items with the same value

### List length
# To determine how many items a list has, use the len() function:

### List items - Data types
# List items can be of any data type
# A list can contain different data type

### type()
` <class 'list'> `

------------------- Access list items
## Negative indexing - start from the end
### -1 refers to the last items

## Range of indexes
### U vcan specify a range of indexes by specifying where to start and where to end the range
### When specifying a range, the return value will be a new list with the specified items
### The started index will include and the ended index will not include

------------------- Change
# Insert more items than u replace
# the new items will be inserted where you specified and the remaining items will move accordingly:

------------------- Add
# Use `append` to add an item to the end of the list
# Use `insert` to insert a list item at a specified index
# Use `extend()` method to append elements from another list to the current list

## Add any iterable
### The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

------------------- Remove
# Remove specified item
# If there are more than one item with the specified value,
# the remove() method removes the first occurrence:

# Remove specified index using pop() method

# the del() also removes the specified index

# Clear the list using clear()

------------------ Loop
# Using for, range and len, while, comprehension

------------------ Comprehension
# Syntax
## newlist = [expression for item in iterable if condition == True]
## The return value is a new list, leaving the old list unchanged. 
## The condition is optional and can be omitted

# Iterable - Doi tuong lap
## The iterable can be any iterable object, like a list, tuple, set ...

# Expression - Bieu thuc
# The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:


----------------- Sort 
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

# To sort descending, use the keyword argument reverse = True:

# You can also customize your own function by using the keyword argument key = function.

# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

# The reverse() method reverses the current sorting order of the elements.

------------------ Copy 
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

# Use the copy() method
# Use the list() method
# Use the : slice operator 

---------------- Join 
# Using + operator
# By appending all the items from list2 to list1, one by one
# Using extend() method

---------------- Method
# Method	    Description
# append()	Adds an element at the end of the list
# clear()	    Removes all the elements from the list
# copy()	    Returns a copy of the list
# count()	    Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the    end of the current list
# index()	    Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	    Sorts the list



