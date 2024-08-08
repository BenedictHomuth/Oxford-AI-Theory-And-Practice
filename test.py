class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dog(Animal): 
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
        return

    def printBreed(self):
        print(self.breed)

d = Dog("Sparky", 7, "Terrier")

print(d.name)