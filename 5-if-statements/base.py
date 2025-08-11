# Short Hand If ... Else
a = 2
b = 300
print("A") if a > b else print("B")

# One line if else statement, with 3 conditions:
print("A") if a >b else print("=") if a == b else print('B')

# The `and` keyword is a logical operator, 
# and is used to combine conditional statements
c = 500
if a < b and c > b:
    print("True")

# The `or` keyword is a logical operator, 
# and is used to combine conditional statements:
if a > b or c > b:
    print(True)

# The `not` keyword is a logical operator, 
# and is used to reverse the result of the conditional statement:
if not a > b: 
    print("True")

# Nested if 
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
    
# The pass Statement
# if statements cannot be empty, but if you for some reason have an 
# if statement with no content, put in the pass statement to avoid 
# getting an error.

if a > b:
    pass