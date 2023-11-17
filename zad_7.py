import random

random = random.randint(1, 10)

while True:
  num = input('Zgadnij liczbe z przedziału 1-10: ')
  if (int(num) == random):
      print('Zgadłeś!')
      break
  else:
      print('Nie zgadłeś!')