# List operations
# Lists are mutable, and hence, they can be altered even after their creation.
# 1. return largest & smallest item in the list

mylist = [1,23,56,700,23,100,700]
a = max(mylist)
b = min(mylist)
print ("Largest item in the list IS : {}".format(a))
print ("Smallest item in the list IS : {}".format(b))

# Return the new sorted list
c = sorted(mylist)
print ("Sorted item in the list IS : {}".format(c))

d = sum(mylist)
print ("Addition of item in the list IS : {}".format(d))

# test if an item exists in a list or not, using the keyword in : returns TRUE or FALSE
my_list = ['p','r','o','b','l','e','m']
if 'p' in my_list:
    print(my_list)

print('r' in my_list)
print('k' in my_list)

print("index(), count(), reverse() clear()outputs")
# index(), count(), reverse()
my_list = [3, 8, 1, 6, 0, 8, 4]

print(my_list.index(8))

print(my_list.count(8))

my_list.sort()

print(my_list)

my_list.reverse()

print(my_list)

my_list.clear()
print(my_list)

# We can use remove() method to remove the given item
# pop() method to remove an item at the given index
my_list = ['p','r','o','b','l','e','m']
my_list.remove('p')

# Output: ['r', 'o', 'b', 'l', 'e', 'm']
print(my_list)

# It will remove 'o'
my_list.pop(1)

# Output: ['r', 'b', 'l', 'e', 'm']
print(my_list)

# We can add one item to a list using append() method or
# add several items using extend() method.

odd = [1, 3, 5]
odd.append(7)
print(odd)

odd.extend([9, 11, 13])

# Output: [1, 3, 5, 7, 9, 11, 13]
print(odd)

print(odd + [9,11,13])