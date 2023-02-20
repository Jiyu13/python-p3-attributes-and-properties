# define class, Human
class Human:

    # class attritubes
    species = "Homo sapiens"

    # initialise method, with name as arg, save it as an attritube of self
    def __init__(self, name):

        # instance attritubes
        self.name = name

    
    # 
    def get_age(self):
        print("Retriving age. ")
        return self._age

    
    def set_age(self, age):
        # method 1:
        # print(f"Setting age to { age }")
        # self._age = age

        # method 2:
        if type(age) in (int, float) and (0 <= age <= 120):
            print(f"Setting age to { age }.")
            self._age = age
        else:
            print("Age must be a number between 0 and 120.")

    # create property age of class Human
    age = property(get_age, set_age)


# =============================================================================
guido = Human("Guido")
guido.species       #Homo sapiens
guido.name          # Guido


# guido.age = 9       # Setting age to 9
# print(guido.age)    # Retriving age. 9
                      # 9
# print(guido._age)   # 9

# ========== method 2: ===========================
guido.age = 0       # Setting age to 0.
guido.age = False   # Age must be a number between 0 and 120.
guido.age = 66      # Setting age to 66.
guido.age           # Retriving age. 
# ==============================================


# change species and name using dot notation
# guido.species = "Python programmer"
# guido.name = "Guido van Rossum"
# print(guido.species)        # Python programmer
# print(guido.name)           # Guido van Rossum


# Getting - retrive - getattr()
# print("getattr(): ", getattr(guido, "name"))   # getattr():  Guido van Rossum


#  Creating new attritubes
# add new attritubes using dot notation
guido.nationality = "Dutch"


# Setting - update attritube - setattr()
# print(guido.nationality)    # Dutch
setattr(guido, "nationality", "AAA")
# print(guido.nationality)    # AAA


# Checking - hasattr()
# print(hasattr(guido, "name"))       # True
# print(hasattr(guido, "language"))   # False

# Deleting - delattr()


# ===============================================================================
Human.species   # Homo sapiens
# Human.name      # AttributeError: type object 'Human' has no attribute 'name

# ===============================================================================
