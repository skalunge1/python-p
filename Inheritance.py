# Parent class or base class
# child class derives properties from base class
# class child(parent):

class Inheritance:
    count = 100
    def __init__(self):
        print("calling Parent constructor ")

    def parentMethod(self):
        print("calling parent method")

    def __setattr__(self, attr):
        Inheritance.count = attr

    def __getattr__(self):
        print(Inheritance.count)

class child(Inheritance):
    def __init__(self):
        print("calling child class constructor")

    def childMethod(self):
        print("calling child method")

# create child class object
c = child()
c.childMethod()
c.parentMethod()
c.__setattr__(1000)
c.__getattr__()


#In a similar way, you can drive a class from multiple parent classes as follows
#class A:        # define your class A
#.....

#class B:         # define your calss B
#.....

#class C(A, B):   # subclass of A and B
# .....