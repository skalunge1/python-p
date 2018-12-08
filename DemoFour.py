# empty list
my_list = []
print(my_list)

# list of integers
my_list = [1, 2, 3]
print(my_list)

# list with mixed datatypes
my_list = [1, "Hello", 3.4]
print(my_list)

# Print 'e' & '3.4
print(my_list[1][1])

#print("Print 3.4 = {}").format(my_list[2][0])
#print("Print 3.4 value : {}").format(my_list[2])

# Negative indexing
# Python allows negative indexing for its sequences. The index of -1 refers to the last item, -2 to the second last item and so on.
my_list = ['p','r','o','b','e']
print(my_list   )
for i in range(len(my_list)):
    print ("Values in lists are : {}".format(my_list[i]))

for a in ['p','r','o','b','e']:
     print(a)

print("***************")
# Output: e
print(my_list[-1])

# Output: p
print(my_list[-5])