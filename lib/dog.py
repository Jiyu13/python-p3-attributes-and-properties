#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    
    def __init__(self, name='Fido', breed='Mastiff'):
        self.name = name
        self.breed = breed


    def get_name(self):
        return self._name
    

    def set_name(self, nameVal):
        if type(nameVal) == str and 1 <= len(nameVal) <= 25:
            self._name = nameVal
        else:
            print("Name must be string between 1 and 25 characters.")
    

    def get_breed(self):
        return self._breed
    

    def set_breed(self, breedVal):
        if breedVal in APPROVED_BREEDS:
            self._breed = breedVal
        else:
            print("Breed must be in list of approved breeds.")
    

    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)




