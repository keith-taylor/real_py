class Doggo:
     species = "Canis familiaris"
     def __init__(self, name, age):
             self.name =  name
             self.age = age
             
     # instance method
     def description(self):
             return f"{self.name} is {self.age} years old."
     
     # another sinatnce method
     def speak(self, sound):
             return f"{self.name} says {sound}!"

    