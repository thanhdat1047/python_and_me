age = 36
# txt = "My name is John, I am" 
# print(txt + age) # Error

# Using fstring
txt = f"My name is John, I am {age}" 
print(txt)

# Placeholders and Modifiers
price = 56.567890
txt = f"I have {price:.2f}"

print(txt.center)