# -*- coding: utf-8 -*-

a: int = 5
print(a)

house = ['кирпи', 'доски', 'песок']
print(house)

print(house.pop())
print(house)

house.sort()
print(house)

house.append('обои')
print(house)

# Различе между append и extend

furniture = ['стол', 'стул', 'шкаф']
house.append(furniture)
print(house)

house.pop()
house.extend(furniture)
print(house)
