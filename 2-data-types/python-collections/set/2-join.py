# Union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
myset2 = set1 | set2 | set3 | set4
print(myset2)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

set3 = set1.intersection(set2)
print(f'set3: {set3}')


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
set4 = set1 - set2

print(set4)

set1.difference_update(set2)
print(f'set1: {set1}')
print(f'set2: {set2}')

set5 = set1.symmetric_difference(set2)
print(set5)

set1.symmetric_difference_update(set2)
print(f'set1: {set1}')
