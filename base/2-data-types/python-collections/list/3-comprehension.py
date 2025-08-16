fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

# with for
# for x in fruits:
#     if 'a' in x:
#         newlist.append(x)

# with comprehension 
newlist = [x for x in fruits if 'a' in x]
print(newlist)

# Iterable
newlist = [x + 1  for x in range(10) if x % 5 == 0]

# Expression
newlist = [x.upper() for x in fruits]
print(newlist)
