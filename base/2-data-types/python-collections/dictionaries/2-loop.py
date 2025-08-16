thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year"  : 2002,
    "year"  : 2008
}
for x in thisdict: 
    print(x)
    
for x in thisdict: 
    print(thisdict[x])
    
for x in thisdict.keys():
    print(x)

for x in thisdict.values():
    print(x)

for (k,v) in thisdict.items():
    print(f"{k} - {v}")
    

y = thisdict.copy()
print(y)
print(type(y))

y2 = dict(thisdict)
print(y2)
print(type(y2))