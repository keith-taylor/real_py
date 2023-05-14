

class Machinery:
    def __init__(self, machine_type, manufacturer, model):
        self.machine_type = machine_type 
        self.make = manufacturer
        self.model = model
# Machinery could be combines, tractors, ploughs, etc
class Tractor(Machinery):
    machine_type = "Tractor" 
    def __init__(self, manufacturer, model, registration, reg_year, colour, initial_milage):
        self.manufacturer = manufacturer
        self.model = model
        self.registration = registration
        self.reg_year = reg_year
        self.colour = colour
        self.initial_milage = initial_milage
        self.milage = initial_milage
    def __str__(self):
        return (
            f"\nMachine details: {self.machine_type}"
            f"\n{self.colour.capitalize()} {self.manufacturer} {self.model}. "
            f"\nRegistration number: {self.registration}, Registration year: {self.reg_year}. "
            f"\nIt has done {self.initial_milage:,} miles. " 
        )
    def drive(self, miles):
        self.milage = self.milage + miles 
    
class CombineHarvester(Machinery):
    machine_type = "Combine Harvester"
    def __init__(self, manufacturer, model, registration, reg_year, colour, initial_milage):
        self.manufacturer = manufacturer
        self.model = model
        self.registration = registration
        self.reg_year = reg_year
        self.colour = colour
        self.initial_milage = initial_milage
        self.milage = initial_milage
    def __str__(self):
        return (
            f"\nMachine details: {self.machine_type}"
            f"\n{self.colour.capitalize()} {self.manufacturer} {self.model}. "
            f"\nRegistration number: {self.registration}, Registration year : {self.reg_year}. "
            f"\nIt has done {self.initial_milage:,} miles. " 
        )
    def drive(self, miles):
        self.milage = self.milage + miles 
class Bailer(Machinery):
    machine_type = "Bailer"
    def __init__(self, manufacturer, model, manufact_year, colour):
        self.manufacturer = manufacturer
        self.model = model
        self.manufact_year = manufact_year
        self.colour = colour
    def __str__(self):
        return (
            f"\nMachine details: {self.machine_type} "
            f"\n{self.colour.capitalize()} {self.manufacturer} {self.model}. "
            f"\nYear of manufacture: {self.manufact_year}. "
        )


class Places:
    def __init__(self, building_type, storage):
        self.building_type = building_type
        self.storage = storage
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
cow_001 = Cow("Jersey")
cow_001.speak()
print(f"The breed of cow 001 is: {cow_001.breed}. ")
sheep_001 = Sheep("Blue Faced Jones")
sheep_001.speak()
print(f"The breed of sheep 001 is: {sheep_001.breed}. ")


my_red_tractor = Tractor(
"Massey Ferguson",
"MF 4700 M",
"PR5 6HY",
2009,
"red",
4_398
)

print(my_red_tractor)

my_bailer = Bailer(
   "Massey Ferguson", 
   "MF 1842S",
   1999, 
   "yellow" 
)

print(my_bailer)

my_blue_tractor = Tractor(
"New Holland",
"T7.230",
"AS3 9HU",
2020,
"blue",
1_398
)

print(my_blue_tractor)

miles_to_drive = 42
print(f"\nWe're going to drive the {my_blue_tractor.colour} {my_blue_tractor.machine_type} for {miles_to_drive} miles.")
my_blue_tractor.drive(miles_to_drive)
print(f"\nThe {my_blue_tractor.colour.lower()} {my_blue_tractor.manufacturer} {my_blue_tractor.model} {my_blue_tractor.machine_type.lower()} has now driven {my_blue_tractor.milage} miles. ")

