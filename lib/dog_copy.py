class Dog:
    
    
    # def __init__(self, name=""):
    #     self._name = name

    # dog = Dog(120)  # name: 120
    # print(dog.name) # set-name: 120
    # dog.name = 120  # Name must be string between 1 and 25 characters.
    # print(pdogerson.name)   # name: 120


     def __init__(self, name=""):
        self.name = name
    # dog = Dog(90)     # set-name: 90
    # print(dog.name)   # Name must be string between 1 and 25 characters.
                        # Traceback (most recent call last):  print(dog.name)
                        # File...in get_name...return f'name: {self._name}'
                        # AttributeError: 'Dog' object has no attribute '_name'
    # dog.name = "120"  
    # print(dog.name)
    

    def get_name(self):
        return f'name: {self._name}'
    

    def set_name(self, nameVal):
        print(f'set-name: {nameVal}')
        if type(nameVal) == str and 1 <= len(nameVal) <= 25:
            self._name = nameVal
        else:
            print("Name must be string between 1 and 25 characters.")



    name = property(get_name, set_name)








