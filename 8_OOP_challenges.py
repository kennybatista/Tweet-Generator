class Tiger(object):
    def __init__(self, name):
        self.name = name

    def sleep(self):
        print(self.name + " sleeps 8 hours")

    def eat(self, food):
        print(self.name + " eats " + food)
        favoriteFood = "meat"
        if favoriteFood == food:
            print("YUM!" + self.name + " wants more " + food)


tiger = Tiger("Tiger")
tiger.eat("meat")
tiger.sleep()




class Bear(object):
    def __init__(self, name):
        self.name = name
        self.favoriteFood = "fish"

    def sleep(self):
        print(self.name + " hibernates for 4 months")

    def eat(self, food):
        print(self.name + " eats " + food)
        if food == self.favoriteFood:
             print("YUM! " + self.name + " wants more " + self.favoriteFood)


bear = Bear("Smokey")
bear.eat("fish")
bear.sleep()
