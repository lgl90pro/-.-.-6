from enum import Enum # Імпортуємо функцію Enum.

while True:
    class converter (Enum): # Задаємо клас 'конвертер'
        USD = 1
        EUR = 2
        CZK = 3
        PLN = 4

    USD = 24.58 # Задаємо теперішній курс валют.
    EUR = 26.9
    CZK = 1.08
    PLN = 6.31

    while True:
        try:
            x = float(input('Amount of money: ')) # Питаємо користувача кількість грошей.
            if(x>0):
                pass
            else:
                print("Кількість грошей не може бути задана від'ємним числом або нулем.")
                print()
                continue
            break
        except ValueError: # Перевіряємо введені дані на помилки.
            print('Кількість грошей може бути задана лише числом.')
            print()
    while True:
        try:
            p = converter[input('Currency: ')] # Питаємо користувача валюту.
            break
        except KeyError:
            print('Введіть лише одну із наступних валют: USD, EUR, CZK, PLN.')

    if(p == converter.USD): # Виводимо результат.
        print(f'{x} USD у гривнях - {USD*x:.2f} грн.')
    elif(p == converter.EUR):
        print(f'{x} EUR у гривнях - {EUR*x:.2f} грн.')
    elif(p == converter.CZK):
        print(f'{x} CZK у гривнях - {CZK*x:.2f} грн.')
    elif(p == converter.PLN):
        print(f'{x} PLN у гривнях - {PLN*x:.2f} грн.')

    print()
    print('Бажаєте повторити задачу?')
    while True:  # Питаємо користувача, чи хоче він повторити задачу.
        question = input('(Так/Ні): ')
        if (question == 'Так' or question == 'так' or question == 'Yes' or question == 'yes' or question == 'y' or question == '+'):
            print()
            break
        elif (question == 'Ні' or question == 'ні' or question == 'No' or question == 'no' or question == 'n' or question == '-'):
            exit(0)
        else:
            print()
            print('Бажаєте повторити задачу?')