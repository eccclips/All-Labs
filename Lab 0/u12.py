import math
r = float(input('Введите радиус цилиндра: '))
h = float(input('Введите высоту цилиндра: '))
circle = math.pi * r**2 # формула площади круга
print('Объём цилиндра: ' + str('%.1f' % (circle * h))) # объём цилиндра по формуле
