# Join list
# Using + operator
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# By appending all the items from list2 to list1, one by one
for x in list2:
    list1.append(x)
print(list1)

# Using extend() method
list1.extend(list2)
print(list1)