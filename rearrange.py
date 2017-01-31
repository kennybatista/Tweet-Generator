import sys
from random import randrange

#script name
scriptname = sys.argv[0]
print(scriptname)

# script holds a list of all args
argList = sys.argv
# we take off the first item, which is the script name
argList.pop(0)
print("This is our argument list " + str(argList))

rearrangedList = []
for i in argList:
    # randomInt = random.randint(1, len(argList))
    rearrangedList.insert(randrange(len(argList)),i)

print("This is our rearranged list " + str(rearrangedList))
