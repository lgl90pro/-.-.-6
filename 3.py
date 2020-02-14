from enum import Enum # Імпортуємо функцію Enum.

while True:
    class month (Enum): # Задаємо клас 'місяць'
        January = 1
        February = 2
        March = 3
        April = 4
        May = 5
        June = 6
        July = 7
        August = 8
        September = 9
        October = 10
        November = 11
        December = 12
    class season (Enum): # Задаємо клас 'сезон'
        Winter = 1
        Spring = 2
        Summer = 3
        Autumn = 4

    while True:
        try:
            s = month [input ('Month: ')] # Питаємо користувача місяць.
            break
        except KeyError: # Перевіряємо введені дані на помилки.
            print('Ви можете задати лише один із 12 місяців (англійською мовою).')
            print()

    if(s == month.January or s == month.February or s == month.December): # Виводимо результат.
        print(f'Your season: {season.Winter.name}')
    elif(s == month.March or s == month.April or s == month.May):
        print(f'Your season: {season.Spring.name}')
    elif(s == month.June or s == month.July or s == month.August):
        print(f'Your season: {season.Summer.name}')
    elif(s == month.September or s == month.October or s == month.November):
        print(f'Your season: {season.Autumn.name}')

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
