# define class, Human
class Human:

    # class attritubes
    species = "Homo sapiens"

    # initialise method, with name as arg, save it as an attritube of self
    def __init__(self, name):

        # instance attritubes
        self.name = name


guido = Human("Guido")
guido.species       #Homo sapiens
guido.name          # Guido

# change species and name using dot notation
guido.species = "Python programmer"
guido.name = "Guido van Rossum"
print(guido.species)        # Python programmer
print(guido.name)           # Guido van Rossum


# Getting - retrive
print("getattr(): ", getattr(guido, "name"))   # getattr():  Guido van Rossum


#  Creating new attritubes
# add new attritubes using dot notation
guido.nationality = "Dutch"


# Setting - update attritube
print(guido.nationality)    # Dutch
setattr(guido, "nationality", "AAA")
print(guido.nationality)    # AAA


# Checking 
print(hasattr(guido, "name"))       # True
print(hasattr(guido, "language"))   # False

# Deleting - delattr()


# ===============================================================================
Human.species   # Homo sapiens
# Human.name      # AttributeError: type object 'Human' has no attribute 'name