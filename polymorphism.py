#Polymorphism: Greek word that means to have many forms or faces;
#              poly=many  morphe=forms
#             Two ways to achieve polymorphism in python:
#             1.Inheritance: An object could be treated of the same tpe as a parent class
#             2. Duck Typing: object must have necessary attributes/methods


from abc import ABC,abstractmethod

class shape:
    @abstractmethod
    def area(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius**2
class square(shape):
    def __init__(self,side):
        self.side = side

    def area(self):
        return self.side**2
class Triangle(shape):
    def __init__(self,base,height):
        self.base = base
        self.height=height

    def area(self):
        return self.base*self.height/2
shapes=[circle(5),square(4),Triangle(3,4)]
for shape in shapes:

   print(shape.area())
