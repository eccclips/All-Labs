dep = int(input('Введите сумму первоначального депозита в рублях: '))
year1 = dep + dep * 0.04 # cумма вклада на конец первого года
year2 = year1 + year1 * 0.04 # cумма вклада на конец второго года
year3 = year2 + year2 * 0.04 # cумма вклада на конец третьего года
print('В конце 1 года сумма на счету составит ' + str('%.2f' % year1) + '₽') # округляем значение до двух знаков после запятой
print('В конце 2 года сумма на счету составит ' + str('%.2f' % year2) + '₽')
print('В конце 3 года сумма на счету составит ' + str('%.2f' % year3) + '₽')
