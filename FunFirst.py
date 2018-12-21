# keyword def is start of the function header
# to execute function, write function name and pass real user input as argument
def greets(name):
     """Function calling"""

     print("Hello" + name + ", Good Morning!")

greets('smita')


def hello_func(greetings, name):
    print(greetings + ", " + name)

hello_func("Good Morning", "Smita")

def hello_func(greetings):
    return '{}function'.format(greetings)
print(hello_func('hi'))

def hello_func(greetings, name = 'You'):
    return '{}, {}'.format(greetings, name)
print (hello_func("Hi", name = "Smita"))

def student(*args, **kwargs):
    # *args = prints Math, Art as tuple
    print(args)

    # **kwargs = print name and age as dictionary
    print(kwargs)
student('Math', 'Art', name = 'Smita', Age = 30)

def student(*args, **kwargs):
    course = ['Math', 'Art']
    info = {'Name':'Smita', 'Age' : 30}
    print(args)
    print(kwargs)
#student(course, info)

def work ():
    print("smita")
work()

def addition(a, b):
    sum = a + b
    print(sum)

    multiply = a * b
    print(multiply)
addition(10, 20)





