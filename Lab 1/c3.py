a = input('Введите букву латинского алфавита: ')
glas = ['a', 'e', 'i', 'o','u', 'A', 'E', 'I', 'O', 'U']
if a in glas:
    print('Эта буква гласная')
elif a == 'y' or a == 'Y':
    print('Эта буква может быть и гласной, и согласной')
else:
    print('Эта буква согласная')

