a = int(input('Введите количество бутылок объёмом 1 литр и меньше: '))
b = int(input('Введите количество бутылок объёмом более одного литра: '))
print('Итоговая сумма составит ' + str('%.2f' % (a * 0.10 + b * 0.25)) + '$.') # умножаем количество маленких бутылок на 0.1 и больших на 0.25
