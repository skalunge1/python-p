# How to access elements from a dictionary?
# 1. with the help of key :
# 2. using get() method : If the key has not found, instead of returning 'KeyError', it returns 'NONE'
my_dict = {'name':'Jack', 'age': 26}

# Output: Jack
print(my_dict['name'])
print(my_dict.get('name'))

# Output: 26
print(my_dict.get('age'))
print(my_dict['age'])

# get() : If the key has not found, instead of returning 'KeyError', it returns 'NONE'
print(my_dict.get('adress'))

# with the help of key only : If the key has not found, returning 'KeyError'.
#print(my_dict['adress'])

# How to change or add elements in a dictionary?
# dictionary is mutable.We can add or edit existing values using assignment operator
# if key is already present, value gets updated else new key:value pair get added

my_dict = {'Name' : 'Smita', 'Adress' : 'Pune', 'Age': 29}
my_dict['Name'] = 'Deepika'
print("Name value after change :{}".format(my_dict['Name']))

my_dict['Age'] = 30
print("Age after change : {}".format(my_dict['Age']))

