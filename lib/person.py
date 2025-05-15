#!/usr/bin/env python3

class Person:
    def __init__(self,name,):
        self.name = name
        print(f"{self.name} has been created.")
man = Person("Ken")
print(man.name)
        
