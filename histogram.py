import random

file_to_open = open("words.txt", "r")
words = file_to_open.read().split()

histogram = {}

for word in words:
    histogram[word] = 1
    for anotherWord in histogram:
        if anotherWord in histogram:
            histogram[anotherWord] += 1


print histogram





print(histogram)
