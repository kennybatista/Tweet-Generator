def sleep(name):
    print(name + " sleeps for 8 hours")

sleep("Rabbit")



def eat(name, food):
    print(name + " eats " + food)
    favoriteFood = "meat"
    if food == favoriteFood:
        print("YUM! " + name + " wants more " + food)


eat("Tiger", "meat")
