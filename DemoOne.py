#take two numbers from user and add them, also display the result.
a = input("Enter two numbers :")
b = input("Enter two numbers :")
try:
    result =int(a) +  int(b)
except Exception as amit:
    print("Error is: {}".format(amit))

#print("Final result is : " + str(result))

#print("Final result is : {}".format(result))

# # is used for comment purpose
# input is a system defined function, which accepts user input in any format from third interface. ex) Keybord input
# By default Python accepts input in String and we need to convert it to specific format
# For smooth execution flow  and exception handling,  try: .... except Exception as e format
# print (" {}".format()) --> is method.By prviding {} braces in it, and using .format() it can convert in any format.
# for type conversion we have to use specifiers explicitely. ex. str(result)