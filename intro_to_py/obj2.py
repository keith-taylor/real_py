class Doggo:
    species = "Canis familiaris"
    def __init__(self, name, age, coat_colour, sex):
        self.name =  name
        self.age = age
        self.coat_colour = coat_colour
        self.sex  = sex
        
    # instance method
    def description(self):
        return f"{self.name} is {self.age} years old."

    # another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}!"
    #
    def __str__(self):
        if self.sex == "boy":
            pronoun = "he"
        else:
            pronoun = "she"
        return f"\n{self.name} is {self.age} years old and {pronoun} is a good {self.sex}! Yes {pronoun} is!"

rex = Doggo("Rex", 4, "red", "boy")

snowy = Doggo("Snowy", 8, "white", "girl")

print(rex)

print(snowy)

class Car:
    def __init__(self, make, model, registration, reg_year, colour, mileage):
        self.make = make
        self.model = model 
        self.registration = registration
        self.reg_year =  reg_year
        self.colour = colour
        self.mileage = mileage
    
    def drive(self, miles):
        self.mileage = self.mileage + miles 
    
    def __str__(self):
        return f"\nCar details: {self.reg_year} {self.colour} {self.make} {self.model} with {self.mileage} miles on the clock. \nThe car's registration is: {self.registration}." 

amanda_car = Car("Porsche", "Carerra", "FK18 7CAR", 2001, "Racing Green", 12_345)

print(amanda_car)

miles  = 4

print(f"Driving for {miles} miles.")

amanda_car.drive(miles)

print(amanda_car)
