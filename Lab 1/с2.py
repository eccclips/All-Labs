a = int(input('Введите возраст: '))
if a <= 0:
   print('Введено неверное число')
elif a <= 21:
   print("Возраст собаки:", ('%.2f' % (a / 10.5)), "человеческих лет")
else:
   print("Возраст собки:", ('%.2f' % ((a - 21)/4 + 2)), "человеческих лет")