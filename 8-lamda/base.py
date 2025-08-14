lfunc = lambda x : x * 2
print(lfunc(2))

def muiltupleFunc(x, y):
    return lambda n: [ x * n, y * n]

myFunc = muiltupleFunc(4, 2)

value = myFunc(2)
print(value)