# 1
name = 'Mateusz'

print('----')
# 2
print(type(name))

print('----')
# 5
print(5 + 7)

print('----')
# 7
print(2 * 4)

print('----')
# 9
print(10 > 5)

print('----')
# 11
try:
  num = input('Podaj liczbe: ')
  if (int(num) > 0):
    print('Liczba jest dodatnia')
except ValueError:
  print('To nie jest liczba')

print('----')
# 13
for num in range(1,6):
  print(num)

print('----')
# 15
print(sum(range(1, 100)))

print('----')
# 19
for num in range(1, 11):
  print('7 * ', num, ' = ', 7 * num)

print('----')
# 20
for num in range(10, 0, -1):
  print(num)
