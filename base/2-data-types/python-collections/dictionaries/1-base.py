# Duplicates not allowed

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year"  : 2002,
    "year"  : 2008
}

print(thisdict)
print(thisdict["year"])
print(thisdict.get("year"))

## is a view of the dictionary
x = thisdict.keys()
print(x)
thisdict["color"] = "gg"
print(x)

y = thisdict.values()
print(y)
thisdict["brand"] = "gen"
print(y)

x = thisdict.items()
print(x)
thisdict["year"] = 2010
print(x)

# Check if key exists

if "model2" in thisdict: 
    print("Yes")
else : print("No")

thisdict.update({"year2": 2020})
print(x)

# remove 
# thisdict.pop("year")
# thisdict.popitem()
# thisdict.clear()
# del thisdict["year"]
# del thisdict
print(x)


# formkeys
x = ('key1', 'key2', 'key3')
y = 0 

thisdict = dict.fromkeys(x,y)
print(thisdict)
# {'key1': 0, 'key2': 0, 'key3': 0}

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault('brand', 'Bronce')
print(x) # Ford

x = car.setdefault("color", "white")
print(x) # white