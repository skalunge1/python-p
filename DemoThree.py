mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)

for i in range(len(mylist)):
    print(i)

print("my list..")
for i in mylist:
    print(i)


# append list to insert value
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = names[1]
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings = "Hello"+" "+ "world"

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)