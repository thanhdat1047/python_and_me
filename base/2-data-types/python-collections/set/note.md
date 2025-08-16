### Set
## Sets are used to store multiple items in a single variable.

## A set is a collection which is unordered, unchangeable*, and unindexed.
* `Note: Set items are unchangeable, but you can remove items and add new items.`

# Sets are written with curly '{' brackets.
`Note: Sets are unordered, so you cannot be sure in which order the items will appear.`

# Set Items
## Set items are unordered, unchangeable, and do not allow duplicate values.

# Unordered
## Unordered means that the items in a set do not have a defined order.
## Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

## Unchangeable
# Set items are unchangeable, meaning that we cannot change the items after the set has been created.
`Once a set is created, you cannot change its items, but you can remove items and add new items.`

## Duplicates Not Allowed
# Sets cannot have two items with the same value.
# Duplicate values will be ignored
`Note: The values True and 1 are considered the same value in sets, and are treated as duplicates`
`Note: The values False and 0 are considered the same value in sets, and are treated as duplicates`

## Using len method

# Set Items - Data Types
## Set items can be of any data type
## A set can contain different data types:

# type() <class 'set'>

# The `set()` Constructor

-------------- Access items
# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

-------------- Add
# Once a set is created, you cannot change its items, but you can add new items.

## To add one item to set use `add()` method
## Add items from another set into the current set, use the `update()` method

# Add Any Iterable
# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

------------- Remove 
## To remove an item in a set, use the `remove()`, or the `discard()` method.
## Remove by using the `pop()` method
## The `clear()` method empties the set
# The `del()` keyword will delete the set completely

------------- Loop
# You can loop through the set items by using a for loop

------------- Join
# There are several ways to join two or more sets in Python.
# The `union()` and `update()` methods joins all items from both sets.
# The `intersection()` method keeps ONLY the duplicates.
# The `difference()` method keeps the items from the first set that are not in the other set(s).
# The `symmetric_difference()` method keeps all items EXCEPT the duplicates.

## Union
## The `union()` method returns a new set with all items from both sets.
## You can use the | operator instead of the `union()` method, and you will get the same result.

-------------- Join Multiple Sets
# All the joining methods and operators can be used to join multiple sets.
# When using a method, just add more sets in the parentheses, separated by commas:
# The `union()` method allows you to join a set with other data types, like lists or tuples.

-------------- Join a Set and a Tuple
# The `union()` method allows you to join a set with other data types, like lists or tuples.
# The result will be a set.
`Note: The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method`

------------- Update
# The `update()` method inserts all items from one set into another.
# The `update()` changes the original set, and does not return a new set.

------------- Intersection
# Keep ONLY the duplicates
# The intersection() method will return a new set, that only contains the items that are present in both sets.
# You can use the & operator instead of the intersection() method, and you will get the same result.
`Note: The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.`
# The `intersection_update()` method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.

------------ Difference 
# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
# You can use the - operator instead of the difference() method, and you will get the same result.
# The `difference_update()` method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.

------------ Symmetric Differences'
# The `symmetric_difference()` method will keep only the elements that are `NOT` present in `both` sets.
# You can use the ^ operator instead of the `symmetric_difference()` method, and you will get the same result.
# The `symmetric_difference_update()` method will also keep all but the duplicates, but it will change the original set instead of returning a new set.

----------- Method
# Method	            Shortcut	Description
# add()	 	                        Adds an element to the set
# clear()	 	                    Removes all the elements from the set
# copy()	 	                    Returns a copy of the set
# difference()	        -	        Returns a set containing the difference between two or more sets
# difference_update()	-=	        Removes the items in this set that are also included in another, specified set
# discard()	 	                    Remove the specified item
# intersection()	    &	        Returns a set, that is the intersection of two other sets
# intersection_update()	&=	        Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	 	                Returns whether two sets have a intersection or not
# issubset()	        <=	        Returns True if all items of this set is present in another set
# 	                    <	        Returns True if all items of this set is present in another, larger set
# issuperset()	        >=	        Returns True if all items of another set is present in this set
# 	                    >	        Returns True if all items of another, smaller set is present in this set
# pop()	 	                        Removes an element from the set
# remove()	 	                    Removes the specified element
# symmetric_difference()	^	    Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
# union()	            |	        Return a set containing the union of sets
# update()	            |=	        Update the set with the union of this set and others














