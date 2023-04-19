from replit import db
import random
import time

unsortedList = [(random.randint(0, 1000)) for i in range(100000)]


def quicksort(list):
  if len(list) <= 1: return list
  randomItem = random.choice(list)
  return [
    item for sublist in (*[quicksort([i for i in list if i < randomItem])],
                         [i for i in list if i == randomItem],
                         *[quicksort([i for i in list if i > randomItem])])
    for item in sublist
  ]


print(quicksort(unsortedList))
