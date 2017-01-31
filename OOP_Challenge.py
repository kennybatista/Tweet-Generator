# Copy your Animal class here
class Animal(object):
    def __init__(self, name):
        self.name = name

    def sleep(self):
        print(self.name + " sleeps for 8 hours")

    def eat(self, food):
        print(self.name + " eats " + food)
        if food == self.favoriteFood:
             print("YUM! " + self.name + " wants more " + self.favoriteFood)


# Copy your Tiger class here
class Tiger(Animal):
    def __init__(self, name):
        self.favoriteFood = "meat"
        self.name = name


# Copy your Bear class here
class Bear(Animal):
    def __init__(self, name):
        self.name = name
        self.favoriteFood = "fish"

    def sleep(self):
        print(self.name + " hibernates for 4 months")


# Implement the Unicorn class here as a subclass of Animal
# Hint: Implement the initializer method and override the sleep method
class Unicorn(Animal):
    def __init__(self, name):
        self.name = name
        self.favoriteFood = "marshmallows"

    def sleep(self):
        print(self.name + " sleeps in a cloud")


# Implement the Giraffe class here as a subclass of Animal
# Hint: Implement the initializer method and override the eat method
class Giraffe(Animal):
    def __init__(self, name):
        self.name = name
        self.favoriteFood = "leaves"

    def eat(self, food):
        print(self.name + " eats " + food)
        if food == self.favoriteFood:
            print("YUM! " + self.name + " wants more " + self.favoriteFood)
        else:
            print("YUCK! " + self.name + " spits out " + food)


# Implement the Bee class here as a subclass of Animal
# Hint: Implement the initializer method and override the sleep and eat methods
class Bee(Animal):
    def __init__(self, name):
        self.name = name
        self.favoriteFood = "pollen"

    def eat(self, food):
        print(self.name + " eats " + food)
        if self.favoriteFood == food:
            print("YUM! " + self.name + " wants more " + self.favoriteFood)
        else:
            print("YUCK! " + self.name + " spits out " + food)

    def sleep(self):
        print(self.name + " never sleeps")


# Implement the Zookeeper class here
class Zookeeper(object):
    # Implement the initializer method here
    def __init__(self, name):
        self.name = name

    # Implement the feedAnimals method here
    def feedAnimals(self, animals, food):
        number = len(animals)
        print(self.name + " is feeding " + food + " to " + str(number) + " animals")
        for currentAnimal in animals:
            currentAnimal.eat(food)
            currentAnimal.sleep()
