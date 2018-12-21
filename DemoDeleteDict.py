# How to delete or remove elements from a dictionary?
# 1. pop() : Remove particular item from list
#       : It removes particular item after providing key and returns removed value

squares = {1:1, 2:4, 3:9, 4:16, 5:25}
print(squares.pop(4))
print(squares.pop(2))
print(squares)
print(squares.popitem())
print(squares)
print("*********")

# popitem() : used to remove and return an arbitrary item (key, value) form the dictionary.
# 2. removes 5:25 , 4:16, 3:9, 2:4, and last removes 1:1
squares = {1:1, 2:4, 3:9, 4:16, 5:25}
print(squares.popitem())
print(squares.popitem())
print(squares.popitem())
print(squares.popitem())
print(squares.popitem())

# after removing all items, it displays empty list
print(squares)
print("*********")

# 3. clear() : All the items can be removed at once using the clear() method.
# It returns None
squares = {1:1, 2:4, 3:9, 4:16, 5:25}
print(squares.clear())
print("After deletion of all the itmes :{}".format(squares))
print("*********")
# 4. 'del' keyword: We can also use the del keyword to remove individual items
# or remove the entire dictionary itself.
squares = {1:1, 2:4, 3:9, 4:16, 5:25}
del squares[4]
del squares[5]
del squares
# print squares after deletion of entire dictionary, throws error
#print(squares)

