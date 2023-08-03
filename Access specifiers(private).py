class Employee:
    def __init__(self):
        self.__name = "Rahul"
        self.__age = 18

a = Employee()
print(a._Employee__name)  # can be accessed indirectly
print(a._Employee__age)

