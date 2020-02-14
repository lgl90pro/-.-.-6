while True:
    days = range(1, 32)
    mounths = range(1, 13)
    years = range(1901, 2021)

    while True: # Задаємо день місяця і робимо перевірку
        try:
            d = int(input('Введіть день місяця: '))
            break
        except ValueError:
            print('День місяця повинен бути заданий цілим числом.')
            print()
    if (d in days):
        pass
    else:
        print('День місяця повинен бути заданий в діапазоні від 1 до 31.')
        print()
        continue

    while True: # Задаємо порядковий номер місяця і робимо перевірку
        try:
            m = int(input('Введіть порядковий номер місяця: '))
            break
        except ValueError:
            print('Порядковий номер місяця повинен бути заданий цілим числом.')
            print()
    if (m in mounths):
        pass
    else:
        print('Порядковий номер місяця повинен бути заданий в діапазоні від 1 до 12.')
        print()
        continue

    while True: # Задаємо рік і робимо перевірку
        try:
            y = int(input('Введіть рік в діапазоні від 1901 до 2020: '))
            break
        except ValueError:
            print('Рік повинен бути заданий цілим числом.')
            print()
    if (y in years):
        pass
    else:
        print('Рік повинен бути заданий в діапазоні від 1901 до 2020.')
        print()
        continue

    if(1<=d<=28):
        pass
    elif (1 <= d <= 29 and y % 4 == 0): # Робимо перевірку, чи існує такий день місяця.
        pass
    elif ((1 <= d <= 30) and (m != 2)):
        pass
    elif ((1 <= d <= 31) and (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12)):
        pass
    else:
        print('Такого дня даного місяця не існує')
        print()
        continue

    y1 = y
    y2 = y
    m1 = m
    m2 = m

    if (d == 28 and m == 2 and y % 4 == 0): # Визначаємо наступний день від вказаного.
        d1 = d+1
    elif ((d == 28 and m == 2 and y % 4 != 0) or (d == 29 and m == 2 and y % 4 == 0)):
        d1 = 1
        m1 = 3
    elif ((d == 30) and (m == 4 or m == 6 or m == 9 or m == 11)):
        d1 = 1
        m1 = m + 1
    elif (d == 31 and m == 12):
        d1 = 1
        m1 = 1
        y1 = y + 1
    elif (d == 31 and (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10)):
        d1 = 1
        m1 = m + 1
    else:
        d1 = d + 1

    if (d == 1 and m == 1): # Визначаємо попередній день від вказаного.
        d2 = 31
        m2 = 12
        y2 = y-1
    elif (d == 1 and (m == 2 or m == 4 or m == 6 or m == 8 or m == 9 or m == 11)):
        d2 = 31
        m2 = m-1
    elif (d == 1 and m == 3 and y % 4 == 0):
        d2 = 29
        m2 = m-1
    elif (d == 1 and m == 3 and y % 4 != 0):
        d2 = 28
        m2 = m-1
    elif (d == 1 and (m == 5 or m == 7 or m == 10 or m == 12)):
        d2 = 30
        m2 = m-1
    else:
        d2 = d-1

    print(f'Наступний день - {d1}.{m1}.{y1} (форма запису: день.місяць.рік).') #Виводимо наступний та попередній день від вказаного.
    print(f'Попередній день - {d2}.{m2}.{y2} (форма запису: день.місяць.рік).')
    print()
    print('Бажаєте повторити задачу?')
    while True:  # Питаємо користувача, чи хоче він повторити задачу.
        question = input('(Так/Ні): ')
        if (
                question == 'Так' or question == 'так' or question == 'Yes' or question == 'yes' or question == 'y' or question == '+'):
            print()
            break
        elif (
                question == 'Ні' or question == 'ні' or question == 'No' or question == 'no' or question == 'n' or question == '-'):
            exit(0)
        else:
            print()
            print('Бажаєте повторити задачу?')







