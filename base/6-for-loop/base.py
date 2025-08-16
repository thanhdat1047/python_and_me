for x in "banana":
  print(x)
  
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
# apple banana

for x in fruits:
  if x == "banana":
    break
  print(x)
# apple

for x in fruits:
  if x == "banana":
    continue
  print(x)

# Range
  
for x in range(6):
  print(x)
  
for x in range(2, 6):
  print(x)
  
for x in range(2, 30, 3):
  print(x)

# Else in For Loop
for x in range(6):
    print(x)
else: 
    print("Finally finished")

