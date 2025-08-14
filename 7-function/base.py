def my_func(*kids):
    print("The yougest: " + kids[2])

my_func("Emil", "Tobi", "Fana")


def my_func2(**kid):
    print("last name is: " + kid["lname"])
    
my_func2(fname = "Emil", lname = "Tobi")

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)