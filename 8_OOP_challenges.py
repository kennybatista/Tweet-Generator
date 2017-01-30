def sleep(name):
    print(name + " sleeps for 8 hours")


# Implement the eat function here
def eat(name, food):
    print(name + " eats " + food)
    favoriteFood = "meat"
    if food == favoriteFood:
        print("YUM! " + name + " wants more " + food)

eat("Leo", "lemons")
sleep("Leo")
eat("Tiger", "meat")
sleep("Tiger")
