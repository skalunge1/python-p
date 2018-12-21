# 1. fromkeys() : returns new dictionary
# only single value present in fromkeys after array and comma
# 2. keys()	: Return a new view of the dictionary's keys.

# 1. fromkeys
marks = {}.fromkeys(['English', 'Hindi'], 0)
print(marks)

# if given two valuse after comma in fromkeys, it assigns both value to first and second key from dictionary
marks = {}.fromkeys(['English', 'Hindi'], [10, 20])
print(marks)
print("*****")

# fromkeys
marks = {}.fromkeys(['Marathi', 'English'], 10)
print(marks)
print("*****below for loop execution")
# loop runs for two times because array contains two keys
for item in marks.items():
  print(marks)
print("***** below timepass ")
for marks in marks:
    print(marks)

# 2. keys() : Return a new view of the dictionary's keys.
print("**** keys ****")
list(sorted(marks.keys()))
print(marks)



