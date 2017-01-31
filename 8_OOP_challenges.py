# This code tests the Animal, Tiger, Bear, Unicorn, Giraffe and Bee classes
# and then tests the Zookeeper class and its feedAnimals method
def test():
    def getline():
        # Read a line from standard input and strip surrounding whitespace
        return sys.stdin.readline().strip()
    # Get the number of animals
    animalCount = int(getline())
    animals = []
    # Iterate through the input for each animal
    for count in range(animalCount):
        # Get the animal's species and name
        species = getline()
        name = getline()
        animal = None
        # Check what species the animal is
        if species == "tiger":
            # Create a Tiger object
            animal = Tiger(name)
        elif species == "bear":
            # Create a Bear object
            animal = Bear(name)
        elif species == "unicorn":
            # Create a Unicorn object
            animal = Unicorn(name)
        elif species == "giraffe":
            # Create a Giraffe object
            animal = Giraffe(name)
        elif species == "bee":
            # Create a Bee object
            animal = Bee(name)
        else:
            # Create an Animal object
            animal = Animal(name, "kibble")
        # Add the animal to the list of animals
        animals.append(animal)
    # Get the zookeeper's name and food to feed the animals
    name = getline()
    food = getline()
    # Create a Zookeeper object and test its feedAnimals method
    zookeeper = Zookeeper(name)
    zookeeper.feedAnimals(animals, food)


if __name__ == "__main__":
    test()
