# Dictionary
## Dictionaries are used to store data values in key:value pairs.
## A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
`As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.`
## Dictionaries are written with curly {} brackets, and have keys and values

# Dictionary Items
## Dictionary items are ordered, changeable, and do not allow duplicates.
## Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

# Changeable
## Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

# Duplicates Not Allowed
## Dictionaries cannot have two items with the same key
## Duplicate values will overwrite existing values

# Dictionary Length
## By using `len()` method

# Dictionary Items - Data Types
## The values in dictionary items can be of any data type

# type() => <class 'dict'>

# The `dict()` Constructor 

--------------------- Access
# Accessing Items
## You can access the items of a dictionary by referring to its key name, inside square brackets
## There is also a method called get() that will give you the same result:

# Get Keys
## The `keys()` method will return a list of all the keys in the dictionary.
## The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.

# Get Values
## The `values()` method will return a list of all the values in the dictionary.

# Get Items
## The items() method will return each item in a dictionary, as tuples in a list.

# Check if Key Exists
## To determine if a specified key is present in a dictionary use the in keyword

--------------------- Change dictionary items
# Change Values
## You can change the value of a specific item by referring to its key name
# Update Dictionary
## The `update()` method will update the dictionary with the items from the given argument.
## The argument must be a dictionary, or an iterable object with key:value pairs.
## If the item does not exist, the item will be added.

--------------------- Removing items
# The `pop()` method removes the item with the specified key name
# The `popitem()` method removes the last inserted item (in versions before 3.7, a random item is removed instead)
# The `del` keyword removes the item with the specified key name
# The `clear()` method empties the dictionary

-------------------- Loop Through a Dictionary
# You can loop through a dictionary by using a `for` loop
## When looping through a dictionary, the return value are the `keys` of the dictionary, but there are methods to return the `values` as well.

## Using the `keys()` to return the keys of a dictionary
## Using the `values()` method to return values of a dictionary
## Loop through both keys and values, by using the `items()` method

------------------- Copy a Dictionary
# Using `copy()` method
# Make a copy of a dictionary with the `dict()` function

------------------- Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.

# Access Items in Nested Dictionaries
## 1. To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:
## `(myfamily["child2"]["name"])`

# Loop Through Nested Dictionaries
## You can loop through a dictionary by using the `items()` method 

----------------- Method
# `formkeys()` 
## The `fromkeys()` method returns a dictionary with the specified keys and the specified value.

# `setdefault(keyname, value)`
## keyname	- Required. The keyname of the item you want to return the value from.
## value	- Optional. If the key exist, this parameter has no effect. If the key does not exist, this value becomes the key's value, Default value None











