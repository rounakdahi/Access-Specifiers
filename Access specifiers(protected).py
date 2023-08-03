class Student:
    def __init__(self):
        self._name = "Ram"
    def _funName(self):       #protected method

        return"He is a Student"


class Subject(Student):
    pass
obj = Student()
obj = Subject()

print(obj._name)
print(obj._funName())
