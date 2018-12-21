# Display employess name, salary and count
class Employee:
    # define all function
    employeeCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employeeCount = 1 + Employee.employeeCount

    def display_EmployeeCount(self):
         print("Employee count is %d: " % Employee.employeeCount)


    def display_EmployeeInfo(self):
        print("Name :",self.name, "and Salary is : ",self.salary)


# create class object
emp1 = Employee("Smita", 20000)
emp2 = Employee("Neha", 30000)

# call class methods
emp1.display_EmployeeInfo()
emp2.display_EmployeeInfo()

# print total employee count
print("Total Employee count is : %d" %Employee.employeeCount)

# verify if attribute presents, if yes returns 'TRUE'
print(hasattr(emp1, 'salary'))
print(hasattr(emp1, 'salar'))

# to return/get attribute value
print(getattr(emp2, 'salary'))

# to set new attribute value to emp 1 salary and name
print(setattr(emp1, 'salary', 70000))
setattr(emp1, 'name', 'nia')
emp1.display_EmployeeInfo()

# delete an attribute
delattr(emp1, 'salary')
emp1.display_EmployeeInfo()


