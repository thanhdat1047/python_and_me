## Map with List, Tuple, Set, Dict
from functools import reduce

lst = [1,2,3,4,5,6]
l1 = map(lambda x: x*2, lst) # <class 'map'>
l1 = list(l1)
print(l1)
print(type(l1))

tpl = (1, 2, 3, 4, 5, 6)
t1 = tuple(map(lambda x: x*2, tpl))
print(t1)
print(type(t1))


st = {1, 2, 3, 4, 5, 6}
st1 = set(map(lambda x: x*2, st))
print(st1)
print(type(st1))

dct = {'a': 1, 'b': 2, 'c': 3}
dct1 = list(map(lambda k: k.upper(), dct))
dct1_1 = list(map(lambda v: v * 2 , dct.values()))
dct1_2 = list(map(lambda kv: (kv[0], kv[1]*2) , dct.items()))
print(dct1)
print(dct1_1)
print(dct1_2)


## filter 
print(list(filter(lambda x: x % 2 == 0, lst)))
print(tuple(filter(lambda x: x % 2 == 0, tpl)))
print(set(filter(lambda x: x % 2 == 0, st)))
print(dict(filter(lambda x: x[1] % 2 == 0, dct.items())))

# reduce
print(reduce(lambda x, y: x + y, lst))
print(reduce(lambda x, y: x + y, tpl))
print(reduce(lambda x, y: x + y, st))
print(reduce(lambda x, y: x + y, dct.values()))
print(reduce(lambda x, y: x + y, dct.keys()))
