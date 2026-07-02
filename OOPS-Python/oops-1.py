#initiating a class
class employee:
    #dunder method -> to define data/attribute that is constructor
    def __init__(self):
        self.id = 123
        self.salary = 12000
        self.desgination = "Soft. Engineer" 
    # class ke andar ek function is technically a method

    def travel(self, destination):
        print(f"Employee is travelling to {destination}")
#creating an object/instance of the class
sam = employee()

print(sam.desgination)

sam.travel("Kerala")