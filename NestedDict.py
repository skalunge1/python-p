# Nested dictionary
# dictionary within dict.
# Collection of dictionaries in single dictionary.

nested_dict = { 'dictA': {'key_1': 'value_1'},
                'dictB': {'key_2': 'value_2'}}

print(nested_dict)

# 1 and 2 is nested dictionary
# Name, Age, Sex is key assigned to it.
People_NestedDict = {1:{'Name':'Smita','age' : 30, 'Sex': 'Female'}, 2:{'Name' :'Kalunge', 'Age': 30, 'Sex' : 'Female'}}
print(People_NestedDict)

# Access elements of a Nested Dictionary
# To access element of a nested dictionary, we use indexing [] syntax in Python.
People_NestedDict = {1:{'Name':'Smita','age' : 30, 'Sex': 'Female'}, 2:{'Name' :'Kalunge', 'Age': 30, 'Sex' : 'Female'}}

print(People_NestedDict[1]['Name'])
print(People_NestedDict[2]['Age'])
# How to retrive data using get() method in nested dictionary
print(People_NestedDict.get('Name'))
