# Sort List Alphanumerically
# List objects have a sort() method 
# that will sort the list alphanumerically, ascending, by default:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Sort the list numerically
thisnumlist = [100, 50, 65, 82, 23]
thisnumlist.sort()
print(thisnumlist)

# Sort Descending 
thislist.sort(reverse = True)
print(thislist)

# Customize sort func 
# by using the keyword argument key = function.
# Tính khoảng cách tuyệt đối giữa n và 50.
# Giá trị càng nhỏ → phần tử càng gần 50 hơn → được xếp trước.
def myFunc(n):
    return abs(n - 50)
thisnumlist.sort(key = myFunc)
print(thisnumlist)

# Case insensitive sort - phan biet hoa thuong
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# Reverse order 
thisnumlist.reverse()
print(thisnumlist)
