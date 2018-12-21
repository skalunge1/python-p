# Dictionary declaration
# Python dictionary is an unordered collection of items. While other compound data types have only value as an element,
# a dictionary has a key: value pair.
# Dictionaries are optimized to retrieve values when the key is known.
# ... Note – Keys in a dictionary doesn't allows Polymorphism.
# values can be unordered, unsorted, collectipn of mixed datatypes
# key muct be immutable types such as 'string, tuple, number and key must be unique

# empty dictionary
my_dict = {}
print(my_dict)

# My dictionary with integers
my_dict = {1 : "smita", 2: "pina", 3 : "Deepika"}
print(my_dict)

my_dict = {1 : 'smita', 2: 'pina', 3 : 'Deepika'}
print(my_dict)

# dictionary with mixed datatypes values
my_dict = {1: 'smita', 2: 10.5, 3: 10}
print(my_dict)

my_dict = {1: 'smita', 2:[10,20,30], 3:['a', 'b', 'c']}
print(my_dict)

# dictionary with mixed keys
my_dict = {'name' : 'smita', 2 : 'sirname', 3:[1,2,3] }
print(my_dict)

# using dict() function
my_dict = dict({1 : 'smita', 2: [10, 20,30]})
print(my_dict)

# from sequence having each item as a pair
my_dict = dict({(1,'smita'), (2, 1020), ('Adress', 'pune'), ('Amba', 'Devi'), ('number', 966627043)})
print(my_dict)