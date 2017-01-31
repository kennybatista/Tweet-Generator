import random
import sys

#Pass the the command line an integer argument

system_argument_number = sys.argv[1]

file_to_open = open("words.txt", "r")
words = file_to_open.read().split()


random_words = []
for i in range(0, int(system_argument_number)):

    randomInt = random.randint(0,len(words))
    random_word = words[randomInt]
    random_words.append(random_word)



print(random_words)
