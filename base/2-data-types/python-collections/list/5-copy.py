# copy method
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()  # không tạo ra tham chieu
print(mylist) 

# Another way is to used list()
mylist2 = list(thislist)
print(mylist2)

# use the slice Operator
mylist3 = thislist[:]
thislist.append('pepsi')
print(mylist3)