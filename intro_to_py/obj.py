class Doggo:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name =  name
        self.age = age
        
    # instance method
    def description(self):
        return f"{self.name} is {self.age} years old."

    # another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}!"
    #
    def __str__(self):
        return f"\n{self.name} is {self.age} years old and is a good dog! Yes he is!"

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y
    
    def __str__(self):
        return f"Point at x: {self.x}, y: {self.y}"    


Rex = Doggo("Rex", 7)

print(Rex)    

first_coords = Point(1,2)

second_coords = Point(3,-2)

print(f"First coordinates: {first_coords}.")
print(f"Second coordinates: {second_coords}.")

first_coords + second_coords

print(f"Result of addition: {first_coords}.")
