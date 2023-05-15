

class Machinery:
    def __init__(self, machine_type, manufacturer, model, storage_size, location):
        self.machine_type = machine_type 
        self.manufacturer = manufacturer
        self.model = model
        self.storage_size  = storage_size
        self.location = location
class Tractor(Machinery):
    def __init__(self, manufacturer, model, storage_size, 
                 location, registration, reg_year, colour, initial_milage):
        machine_type = "Tractor" 
        super().__init__(machine_type, manufacturer, model, storage_size, location)
        self.registration = registration
        self.reg_year = reg_year
        self.colour = colour
        self.initial_milage = initial_milage
        self.milage = initial_milage
    def __str__(self):
        return (
            f"\nMachine details: {self.colour.capitalize()}, {self.manufacturer}, {self.model}, {self.machine_type}"
            f"\nRegistration number: {self.registration}, Registration year: {self.reg_year}. "
            f"\nIt has done {self.initial_milage:,} miles and is currently stored in the {self.location}. " 
        )
    def drive(self, miles):
        self.milage = self.milage + miles 
    
class CombineHarvester(Machinery):
    def __init__(self, manufacturer, model, storage_size,
                 location, registration, reg_year, colour, initial_milage):
        machine_type = "Combine Harvester"
        super().__init__(machine_type, manufacturer, model, storage_size, location)
        self.registration = registration
        self.reg_year = reg_year
        self.colour = colour
        self.initial_milage = initial_milage
        self.milage = initial_milage
    def __str__(self):
        return (
            f"\nMachine details: {self.colour.capitalize()}, {self.manufacturer}, {self.model}, {self.machine_type}"
            f"\nRegistration number: {self.registration}, Registration year: {self.reg_year}. "
            f"\nIt has done {self.initial_milage:,} miles and is currently stored in the {self.location}. " 
        )
    def drive(self, miles):
        self.milage = self.milage + miles 
class Bailer(Machinery):
    def __init__(self, manufacturer, model, storage_size,
                 location, manufact_year, colour):
        machine_type = "Bailer"
        super().__init__(machine_type, manufacturer, model, storage_size, location)
        self.manufacturer = manufacturer
        self.manufact_year = manufact_year
        self.colour = colour
    def __str__(self):
        return (
            f"\nMachine details: {self.colour.capitalize()}, {self.manufacturer}, {self.model}, {self.machine_type} "
            f"\nCurrently stored in the {self.location}. "
            f"\nYear of manufacture: {self.manufact_year}. "
        )


class Places:
    def __init__(self, building_type, name, size, contents):
        self.building_type = building_type
        self.name = name 
        self.size = size
        self.contents = contents
class Barn(Places):
    building_type = "barn"
    def __init__(self, name, size, contents):
        self.name = name
        self.size = size 
        self.contents = contents
        # storage_capacity about 60
        contents = []
    def __str__(self):
        return (
            f"\nBuilding details: {self.name} "
            f"\n{self.colour.capitalize()} {self.manufacturer} {self.model}. "
            f"\Currently stored in the {self.location}. "
            f"\nYear of manufacture: {self.manufact_year}. "
        )    
class Field(Places):
    building_type = "field"
    def __init__(self, name, size, contents):
        self.name = name
        self.size = size
        self.contents = contents
        # field_size about 60_000
        contents = []


class Animal():
    def __init__(self, breed, barn_space_requirement, grazing_space_requirement, location):
        self.breed = breed
        self.barn_space_requirement = barn_space_requirement
        self.grazing_space_requirement = grazing_space_requirement
        self.location = location
    def animal_speak(self, name, sound):
        return f"A {name} goes '{sound}'. "
class Chicken(Animal):
    sound = "cluck-cluck"
    animal_type = "chicken"
    def __init__(self, breed, location):
        self.breed = breed
        # self.barn_space_requirement = barn_space_requirement
        # self.grazing_space_requirement = grazing_space_requirement
        self.location = location
        barn_space_requirement = 0.5
        grazing_space_requirement = 2.5
    def speak(self):
        print(super().animal_speak(self.animal_type, self.sound))
    def move(self, move_to):
        location = move_to
        return location 
        
class Cow(Animal):
    sound = "shazooooo"
    animal_type= "cow"
    def __init__(self, breed, location):
        self.breed = breed
        # self.barn_space_requirement = barn_space_requirement
        # self.grazing_space_requirement = grazing_space_requirement
        self.location = location
        barn_space_requirement = 4.5
        grazing_space_requirement = 1200 
    def speak(self):
        print(super().animal_speak(self.animal_type, self.sound))
class Sheep(Animal):
    sound = "baaaaaa"
    animal_type = "sheep"
    def __init__(self, breed, location):
        self.breed = breed
        # self.barn_space_requirement = barn_space_requirement
        # self.grazing_space_requirement = grazing_space_requirement
        self.location = location
        barn_space_requirement = 2.5
        grazing_space_requirement = 400
    def speak(self):
        print(super().animal_speak(self.animal_type, self.sound))

# Buildings declarations

big_barn = Barn("Big Barn", 80, 0)
old_barn = Barn("Old Barn", 60, 0)
lower_field = Field("Lower Field", 40_000, 0)
upper_field = Field("Upper Field", 80_000, 0)
far_field = Field("Far Field", 20_000, 0)

# Animal input and output
chicken_001 = Chicken("Burford Brown", big_barn)
chicken_001.speak()
print(f"The breed of chicken 001 is: {chicken_001.breed}. ")
cow_001 = Cow("Jersey", old_barn)
cow_001.speak()
print(f"The breed of cow 001 is: {cow_001.breed}. ")
sheep_001 = Sheep("Hampshire Blue Face", upper_field)
sheep_001.speak()
print(f"The breed of sheep 001 is: {sheep_001.breed}. ")

# Machinery input and output
red_tractor = Tractor(
"Massey Ferguson",
"MF 4700 M",
9,
"Old Barn",
"PR5 6HY",
2014,
"red",
9_398
)
print(red_tractor)

blue_combine = CombineHarvester(
"John Deere", 
"T670", 
20,
"Old Barn",
"NX07 HMD", 
2021, 
"blue", 
978
)
print(blue_combine)

yellow_bailer = Bailer(
"Massey Ferguson", 
"MF 1842S",
10,
"Old Barn", 
1999, 
"yellow"
)
print(yellow_bailer)

blue_tractor = Tractor(
"New Holland",
"T7.230",
10,
"Old Barn",
"AS3 9HU",
2020,
"blue",
1_398
)
print(blue_tractor)

miles_to_drive = 42
print(f"\nWe're going to drive the {blue_tractor.colour} {blue_tractor.machine_type} for {miles_to_drive} miles.")
blue_tractor.drive(miles_to_drive)
print(f"\nThe {blue_tractor.colour.lower()} {blue_tractor.manufacturer} {blue_tractor.model} {blue_tractor.machine_type.lower()} has now driven {blue_tractor.milage} miles. ")

print(Places.instances)