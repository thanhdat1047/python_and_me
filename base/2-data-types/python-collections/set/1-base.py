thisset = {"apple", "banana", "cherry"}
print(thisset)

for x in thisset: 
    print(x)

print('apple' in thisset) # True
print('apple' not in thisset) # False

thisset.add('apple2')
print(thisset)

tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

thistuple = tuple(("banana2",))
thisset.update(thistuple)
print(thisset)

thisset.remove("banana2")
print(thisset)

thisset.discard("apple")
print(thisset)

thisset.clear()
print(thisset)

del thisset

