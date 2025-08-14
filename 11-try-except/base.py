x = 2
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except: 
    print("Something else went wrong")
else: 
    if not type(x) is str:
        raise TypeError("Only str are allowed")
    print("Nothing went wrong")
finally:
  print("The 'try except' is finished")