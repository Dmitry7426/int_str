import re
from slovar import *

arr = []
slovar = []

# Раскладываем простое трехзначное число и формируем массив
def creat_arr(a, b):
    global thousand
    global from0To19
    global hundreds
    global tens
    global from0To2
    if b == 'И':
        from0To2 = from0To2_I
        from0To19 = from0To19_I
        tens = tens_I
        hundreds = hundreds_I
        thousand = thousands_I
    elif b == 'Р':
        from0To2 = from0To2_P
        from0To19 = from0To19_P
        tens = tens_P
        hundreds = hundreds_P
        thousand = thousands_P

    sl = str('{0:,}'.format(a).replace(',', ' '))
    sl = sl.split()
    a = 0
    for j in range(0, len(sl)):
        a += 1
        i = int(sl[j])
        if i <= 19:
            arr.append(from0To19[i])
        elif 19 < i <= 99:
            arr.append(tens[(i // 10) - 1] + ' ' + from0To19[(i % 10)])
        elif 100 < i <= 999:
            w = i % 100
            if w <= 19:
                to19 = from0To19[w]
            elif 19 < w <= 99:
                to19 = (tens[(w // 10) - 1] + ' ' + from0To19[(w % 10)])
            arr.append(hundreds[(i // 100) - 1] + ' ' + to19)

    if len(arr) == 1:
        data = []
        data.append(tish(1, sl[0]))
        return data

    elif len(arr) == 2:
        data = []
        data.append(tish(2, sl[0]))
        data.append(tish(1, sl[1]))
        return data

    elif len(arr) == 3:
        data = []
        data.append(tish(3, sl[0]))
        data.append(tish(2, sl[1]))
        data.append(tish(1, sl[2]))
        return data

    elif len(arr) == 4:
        data = []
        data.append(tish(4, sl[0]))
        data.append(tish(3, sl[1]))
        data.append(tish(2, sl[2]))
        data.append(tish(1, sl[3]))
        return data
    else:
        return 0


# разбивка по блокам
def tish(a, b):

    if a == 1:
        tho = thousand[0]
        w = b
    elif a == 2:
        tho = thousand[1]
        w = b
    elif a == 3:
        tho = thousand[2]
        from0To2 = from0To19
        w = b
    elif a == 4:
        tho = thousand[3]
        w = b
        from0To2 = from0To19
    if int(w) <= 19:
        if int(w) == 1:
            slovar.append(from0To19[1] + ' ' + tho[0])
        elif int(w) == 2:
            slovar.append(from0To19[2] + ' ' + tho[1])
        elif int(w) == 3 or int(w) == 4:
            slovar.append(from0To19[int(w)] + ' ' + tho[1])
        elif int(w) >= 5:
            slovar.append(from0To19[int(w)] + ' ' + tho[2])
    if 20 <= int(w) <= 99:
        if int(w) % 10 == 1:
            slovar.append(tens[(int(w) // 10) - 1] + ' ' + from0To2[1] + ' ' + tho[0])
        elif int(w) % 10 == 2:
            slovar.append(tens[(int(w) // 10) - 1] + ' ' + from0To2[2] + ' ' + tho[1])
        elif int(w) % 10 == 3 or int(w) % 10 == 4:
            slovar.append(tens[(int(w) // 10) - 1] + ' ' + from0To19[int(w) % 10] + ' ' + tho[1])
        elif int(w) % 10 >= 5:
            slovar.append(tens[(int(w) // 10) - 1] + ' ' + from0To19[int(w) % 10] + ' ' + tho[2])
        elif int(w) % 10 == 0:
            slovar.append(tens[(int(w) // 10) - 1] + ' ' + from0To19[int(w) % 10] + ' ' + tho[2])
    if 100 <= int(w) <= 999:
        slovar.append(hundreds[(int(w) // 100) - 1] + ' ' + tens[(int(w) % 100) // 10 - 1] + ' ' + from0To19[int(w) % 10] + ' ' + tho[1])
    return slovar

def mil(a, b):
    if a == 3:
        w = b
        print('Приняла mil', w)
        if int(w) <= 19:
            if int(w) == 1:
                slovar.append(from0To2[1] + ' ' + thousands[1][0])
            elif int(w) == 2:
                slovar.append(from0To2[2] + ' ' + thousands[1][1])
            elif int(w) == 3 or int(w) == 4:
                slovar.append(from0To19[int(w)] + ' ' + thousands[1][1])
            elif int(w) >= 5:
                print(int(w))
                slovar.append(from0To19[int(w)] + ' ' + thousands[1][2])
        if 20 <= int(w) <= 99:
            if int(w) % 10 == 1:
                slovar.append(tens[(int(w) // 10) - 1] + ' ' + from0To2[1] + ' ' + thousands[1][0])
            elif int(w) % 10 == 2:
                slovar.append(tens[(int(w) // 10) - 1] + ' ' + from0To2[2] + ' ' + thousands[1][1])
            elif int(w) % 10 == 3 or int(w) % 10 == 4:
                slovar.append(tens[(int(w) // 10) - 1] + ' ' + from0To19[int(w) % 10] + ' ' + thousands[1][1])
            elif int(w) % 10 >= 5:
                slovar.append(tens[(int(w) // 10) - 1] + ' ' + from0To19[int(w) % 10] + ' ' + thousands[1][2])
            elif int(w) % 10 == 0:
                slovar.append(tens[(int(w) // 10) - 1] + ' ' + from0To19[int(w) % 10] + ' ' + thousands[1][2])
        print('slovar', slovar)
        if 100 <= int(w) <= 999:

            slovar.append(hundreds[(int(w) // 100) - 1] + ' ' + tens[(int(w) % 100) // 10 - 1] + ' ' + from0To19[int(w) % 10]  + ' ' + thousands[0][1])
    #         print(int(w) // 100, 'Первый цифра')
    #         print(int(w) // 10)
    #         print(int(w) % 100)
    #         print((int(w) % 100) // 10, 'Второй цифра')
    #         print(int(w) % 10, 'Третий цифра')
    #         hund = hundreds[(int(w) // 100) - 1]
    #         print(hund)
    #         two_digit = tens[((int(w) % 100) // 10) - 1]
    #         print(two_digit)
    #         tre_digit = from0To19[(int(w) % 10)]
    #         print(tre_digit)
    #
    return slovar


def st():
    try:
        w, p = abs(int(input('Введи число не более 999999999999: '))), str(input('Введите какого падежа: '))

        if 0 > w > 999999999999:
            print('Число вне диапазона!')
        else:
            result = creat_arr(int(w), str(p))
            res = result[:1]
            for i in res:
                print(*i)
    except:
        print('Число вне диапазона!')

st()
