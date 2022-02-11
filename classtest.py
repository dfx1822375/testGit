class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(self.name,self.age)
class Student(Person):
    def __init__(self,name,age,number):
        super().__init__(name,age)
        self.number = number
    def show(self):
        super(Student, self).show()
        print(self.number)
a = Student('xiang',20,123456)
a.show()