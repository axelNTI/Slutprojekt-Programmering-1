from replit import db
import random
import time


def variables():
  pass


def game():
  pass


def leaderboard():
  for i in db:
    print(f'{i.split().pop(0)}      {db[i]}')


def database(name, value):
  db[f'{time.time()} {name}'] = value


def quicksort(list):
  if len(list) <= 1: return list
  randomItem = random.choice(list)
  return [
    item for sublist in (*[quicksort([i for i in list if i < randomItem])],
                         [i for i in list if i == randomItem],
                         *[quicksort([i for i in list if i > randomItem])])
    for item in sublist
  ]

database('Axel1', [3, 1, 6, 8, 1])
database('Axel2', [2, 3, 3, 4, 6])
database('Axel3', [4, 2, 7, 2, 5])
database('Axel4', [36, 16, 4, 2, 5])
database('Axel5', [8, 5, 7, 7, 2])
leaderboard()