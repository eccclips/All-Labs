letter = input("Введите номер СТОЛБЦА: ")
number = int(input("Введите номер СТРОКИ: "))
mas1 = ['a', 'c', 'e', 'g']
if letter in mas1:
    if number % 2 == 0:
        print("Клетка белая")
    else:
        print("Клетка чёрная")
else:
    if number % 2 == 1:
        print("Клетка белая")
    else:
        print("Клетка чёрная")