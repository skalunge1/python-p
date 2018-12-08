# Declare first list with 5 numbers
# Declare second list with 10 numbers
# compare common numbers and create a new list
# create a new list with numbers which are not common.

a = [1,2,3,4,5]
b = [3,1,2,6,7,8,9,0,11,12]
c = []
d = []

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            c.append(a[i])

print("Common value: {}".format(c))

for i in a:
    if i in c:
        pass
    else:
        d.append(i)
for i in b:
    if i in c:
        pass
    else:
        d.append(i)

print("UnCommon value: {}".format(d))

print("xyz")
print("m bhi edit karunga")

# list declaration a = [] - empty list declarations
# list declaration b = [1, 2, 3]
# for loop declarations = for i in a:   --> it counts values from a list
# for loop declarations different way using length of a list = for i in range(len(a)):   --> it counts length of a list
# append() : method used to insert element in list



