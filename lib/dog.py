#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed
        print(f"{self.name} is born!")
    
    def bark(self):
        print("Woof!")

    def showing_self(self):
        return self

fido = Dog("Fido")
fido.bark()
fido.showing_self()

snoopy = Dog("Snoopy","Beagle")
