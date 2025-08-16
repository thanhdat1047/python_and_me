# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

## Tuple Items
## Tuple items are ordered, unchangeable, and allow duplicate values.
## Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

# Ordered
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

# Unchangeable
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

# Allow Duplicates
# Since tuples are indexed, they can have items with the same value

# Tuple Length
# To determine how many items a tuple has, use the len() function

# Create Tuple With One Item
# To create a tuple with only one item, you have to add a comma (,)after the item, otherwise Python will not recognize it as a tuple.

# Tuple items can be of any data type

# type() <class 'tuple'>

# The tuple() Constructor

-------------- Access item
# You can access tuple items by referring to the index number, inside square brackets:

# Negative indexing
# Negative indexing means start from the end.
# -1 refers to the last item, -2 refers to the second last item etc.

# Range of indexes
# When specifying a range, the return value will be a new tuple with the specified items.
# The first item has index 0.

# Use ` in ` to check if item exists

------------- Update tuples
## Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

## But there is a workaround. You can `convert the tuple into a list, change the list, and convert the list back into a tuple.`

------------- Add items
# Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.

# 1. `Convert into a list`: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.
# 2. `Add tuple to a tuple`: You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:

------------- Remove
# Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:
# 1. `Convert into a list`:
# 2. Use `del`, but it will delete the tuple completely

------------- Unpack Tuple
# Unpacking a Tuple
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple
# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking"

# Using Asterisk*
# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list

------------- Loop 
# Loop Through a Tuple
# You can loop through the tuple items by using a `for` loop.
# `range and len`
# `while`

------------ Join
# Join Two Tuples
## Use `+` operator

# Multiply Tuples
## If you want to multiply the content of a tuple a given number of times, you can use the `*` operator:

------------ Method
# Tuple Methods
# Python has two built-in methods that you can use on tuples.

# Method	Description
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found




