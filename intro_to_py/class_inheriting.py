class Dog:
    species = "Canis familiaris"
    
    def __init__(self, name, age, sex):
        self.name =  name
        self.age = age
        self.sex  = sex
        
    # instance method
    def description(self):
        return f"{self.name} is {self.age} years old."

    # another instance method
    def speak(self, sound):
        return f"\n{self.name} says {sound}!"
    #
    def __str__(self):
        if self.sex == "boy":
            pronoun = "he"
        else:
            pronoun = "she"
        return f"\n{self.name} is {self.age} years old and {pronoun} is a good {self.sex}! Yes {pronoun} is!"

#miles = Dog("Miles", 4, "boy")
#buddy = Dog("Buddy", 9, "boy")
#jacky = Dog("Jacky", 3, "girl")
#snowy = Dog("Snowy", 5, "girl")

#print(buddy.speak("woof-woof") )

class JackRussell(Dog):
    pass
class Bulldog(Dog):
    pass

myles = JackRussell("Myles", 4, "boy")
jacky = Bulldog("Jacky", 3, "girl")

class Labrador(Dog):
    pass

ghandi = Labrador("Ghandi", 3, "boy")

print(f"{ghandi.name} is a {ghandi.species}.")
print(ghandi)
print(ghandi.speak("rrruff"))
