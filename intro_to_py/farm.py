

class Machinery:
    def __init__(self, machine_type, manufacturer, model):
        self.machine_type = machine_type 
        self.make = manufacturer
        self.model = model
# Machinery could be combines, tractors, ploughs, etc
class Tractor(Machinery):
    def __init__(self, manufacturer, model, registration, reg_year, colour, mileage):
        self.manufacturer = manufacturer
        self.model = model
        self.registration = registration
        self.reg_year = reg_year
        self.colour = colour
        self.mileage = mileage
    def __str__(self):
        return (
            f"\nMachine details: "
            f"\n{self.colour} {self.manufacturer} {self.model}. "
            f"\nRegistration number: {self.registration}, Registration year : {self.reg_year}. "
            f"It has done {self.mileage} miles. " 
        )
    def drive(self, miles):
        self.mileage = self.mileage + miles 
    
class CombineHarvester(Machinery):
    def __init__(self, manufacturer, model, registration, reg_year, colour, mileage):
        self.manufacturer = manufacturer
        self.model = model
        self.registration = registration
        self.reg_year = reg_year
        self.colour = colour
        self.mileage = mileage
    def drive(self, miles):
        self.mileage = self.mileage + miles 
class Bailer(Machinery):
    def __init__(self, manufacturer, model, manufact_year, colour):
        self.manufacturer = manufacturer
        self.model = model
        self.manufact_year = manufact_year
        self.colour = colour


class Places:
    def __init__(self, building_type):
        self.building_type = building_type
class Barn(Places):
    def __init__(self, barn_contents):
        self.barn_contents = barn_contents
class Field(Places):
    def __init__(self, field_type):
        self.field_type = field_type

class Animal():
    def __init__(self, breed):
        self.breed = breed
    def animal_speak(self, name, sound):
        return f"A {name} goes '{sound}'. "
class Chicken(Animal):
    sound = "cluck-cluck"
    animal_type = "chicken"
    def __init__(self, breed):
        self.breed = breed
    def speak(self):
        print(super().animal_speak(self.animal_type, self.sound))
class Cow(Animal):
    sound = "shazooooo"
    animal_type= "cow"
    def __init__(self, breed):
        self.breed = breed
    def speak(self):
        print(super().animal_speak(self.animal_type, self.sound))
class Sheep(Animal):
    sound = "baaaaaa"
    animal_type = "sheep"
    def __init__(self, breed):
        self.breed = breed
    def speak(self):
        print(super().animal_speak(self.animal_type, self.sound))


chicken_001 = Chicken("Burford Brown")

chicken_001.speak()

print(f"The breed of chicken 001 is: {chicken_001.breed}. ")

my_red_tractor = (
"Massey Ferguson",
"MF 4700 M",
"PR5 6HY",
2009,
"red",
"4_398"
)

print(my_red_tractor)

