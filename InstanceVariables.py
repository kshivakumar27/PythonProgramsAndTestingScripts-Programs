class Animal():
    animallegs = 4

    # instance method
    def setAnimalLegs(self):  
        animallegs = 10  # instance varibale
        print("Animal legs are ", animallegs)

    @classmethod
    def changeLegs(cls):
        cls.animallegs = 5
        print("in class method legs are ", cls.animallegs)

    @staticmethod
    def myMethodlegs():
        print("static method")

animal = Animal()

Animal.myMethodlegs()



# print(f"animal legs are {animal.animallegs}")
#
# Animal.changeLegs()
#
# print(f"animal legs are {Animal.animallegs}")



# print(f"animal legs are {animal.animallegs}")
#
# animal.setAnimalLegs()
#
# print(f"animal legs are {animal.animallegs}")