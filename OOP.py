# Blueprint for car

class Car:
    # constructor
    def __init__(self):
        self.carName="Audi"
        self.noOfWheels=4
    
    # Method
    def startCar(self):
        print("Car is starting!")
    def stopCar(self,name):
        print("Car is stopped by",name)
    
    
# Car --> 2 attr --> 2 method

# Blueprint of Cat 
class Cat(Car):
    # constructor
    def __init__(self):
        self.catName="tom"
        self.favFood="milk"
        self.friend="jerry"
    # Methods
    def sayHello(self):
        print("Meow...!")
    
# Car class --> 3 attr --> 1 method

# Objects

# car1=Car()
# car2=Car()
# car3=Car()
# car4=Car()
# car5=Car()

# print(car1.carName)
# print(car1.noOfWheels)

# car1.startCar()
# car1.stopCar("Leo")

# cat1=Cat()
# cat2=Cat()
# cat3=Cat()
# cat4=Cat()

# cat3.sayHello()


a="23" # class str
b=Cat() #Object

# print(type(b)) 

a=[1,2,3,4,5]

b.startCar()

str