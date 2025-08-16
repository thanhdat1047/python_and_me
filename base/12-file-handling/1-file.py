f = open("demonfile.txt")
print(f.read())

with open("demonfile.txt") as f:
    print(f.readline())
    
with open("demonfile.txt") as f:
    for x in f:
        print(x)
        
# Append content
with open("demonfile.txt", "a") as f:
    f.write("\nNow the file has more content")

with open("demonfile.txt") as f:
    print(f.read())
    
# Overwrite Existing Content
with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")
with open("demofile.txt") as f:
  print(f.read())
  
  
f = open("myfile.txt", "x")
    
    