while True:
    while True:
        try:
            t = int(input('Введіть час, який горить світлофор: ')) # Питаємо користувача час.
            if(t>0):
                pass
            else:
                print('Час може бути заданим лише натуральним числом.')
                print()
                continue
            break
        except ValueError: # Перевіряємо введені дані на помилки.
            print('Ви можете ввести лише ціле число.')
            print()

    t1 = t % 6
    if(t1 == 1 or t1 == 2 or t1 == 3): # Виводимо результат.
        print('Зараз горить зелений сигнал світлофора.')
    elif (t1 == 4):
        print('Зараз горить жовтий сигнал світлофора.')
    elif (t1 == 5 or t1 == 0):
        print('Зараз горить червоний сигнал світлофора.')
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