class Car :
    name = "Tesla"
    def __init__(self):
        print ("Car Class Initiated");
        self.name = "Batmobile"

    def getCarname(self):
        print ("Car name");
        print (self.name);

    def acclerate(self):
        print ("Acclerated");

#Creating Instance of class.
mycar = Car();
Car.speed = 95;

print (Car.speed);

#Inheritance.
class Autonomous_Car(Car):

    def __init__(self):
        super().__init__();        #Parent class constructor can be called first, like i want to get and initialize properties of parent class
        print ("Autnomous Car Class");
        super().getCarname();       #Calling parent class method.

#Child class Instance.
aut_car = Autonomous_Car();

