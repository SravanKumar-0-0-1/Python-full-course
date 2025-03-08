#@Static method: A method that belong to a class rather than any object from that class (instance)
#               Usually used for general utility functions.

#               Instance method: Best for operations on instances of the class(objects)
#               static method : Best for utility functions that do not need access to class data.

class Employee:
    def __init__(self,name,position):
        self.name=name
        self.position=position
    
    def get(self):
        return f"{self.name} ={self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions=["Manager","Assistant","Accountant"]
        return position in valid_positions
    
employee1=Employee("John","Manager")
employee2=Employee("Alice","Assistant")
print(Employee.is_valid_position("Manager"))
print(employee1.get())