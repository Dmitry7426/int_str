import re


zero = ''
from0To2 = [zero, 'одна', 'две'];
from0To19 = [zero, 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять',
             'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать',
             'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать'];
tens = ['десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто', zero];
hundreds = ['сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот'];
thousands = [['', '', ''],
             ['тысяча', 'тысячи', 'тысяч'],
             ['миллион', 'миллиона', 'миллионов'],
             ['миллиард', 'миллиарда', 'миллиардов'],
             ['триллион', 'триллиона', 'триллионов'],
             ['квадриллион', 'квадриллиона', 'квадриллионов'],
             ['квинтиллион', 'квинтиллиона', 'квинтиллионов'],
             ['секстиллион', 'секстиллиона', 'секстиллионов'],
             ['септиллион', 'септиллиона', 'септиллионов'],
             ['октиллион', 'октиллиона', 'октиллионов'],
             ['нониллион', 'нониллиона', 'нониллионов'],
             ['дециллион', 'дециллиона', 'дециллионов']];
# res = ''
# tmp = ''
arr = []
slovar = []
# arr_tmp = []
# to19 = ''
# sl = str('{0:,}'.format(i).replace(',', ' '))
# sl2 = []
# sl2 = sl.split()
# len = len(sl2)
# print(type(len))
# for _ in range(len):
#     number = int(''.join(map(str, sl2)))
#
# print(number)
# Функция разложения простого 3х значного числа
def creat_arr(a):
    sl = str('{0:,}'.format(a).replace(',', ' '))
    sl = sl.split()
    a = 0
    tmp = []
    for j in range(0, len(sl)):
        a += 1


        i = int(sl[j])
        print('Массив из J', i)
        print('Длинна массива', len(sl))
        print('Вест полученный массив', sl)

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

    print('Весь массив арр', arr)
    if len(arr) == 1:

        return str(tish(1, sl))

    elif len(arr) == 2:

        return str(tish(2, sl[0])) + ' ' + str(arr[1])

    elif len(arr) == 3:
        print(sl[0], sl[1], sl[2])
        return str(tish(3, sl[0])) + str(tish(2, sl[1])) + str(tish(1, sl[2]))

    elif len(arr) == 4:
        return str(tish(4, sl[0])) + str(tish(3, sl[1])) + str(tish(2, sl[2])) + str(tish(1, sl[3]))
    else:
        return 0



#
#
# e = 1
# sl = str('{0:,}'.format(e).replace(',', ' '))
#
# sl = sl.split()
# # print(sl)
# a = 0
# for i in sl:
#     a += 1


# print(sl)
# разбивка тысяч
def tish(a, b):
    if a == 1:
        tho = thousands[0]
        w = b

        print('Сработал 1й иф')
    elif a == 2:
        tho = thousands[1]
        w = b
    elif a == 3:
        tho = thousands[2]
        from0To2 = from0To19
        w = b
        print('Сработал блок 3')
    elif a == 4:
        tho = thousands[3]
        w = b
        from0To2 = from0To19

    print(w, ' Это B')
    if int(w) <= 19:
        if int(w) == 1:
            slovar.append(from0To2[1] + ' ' + tho[0])
        elif int(w) == 2:
            slovar.append(from0To2[2] + ' ' + tho[1])
        elif int(w) == 3 or int(w) == 4:
            slovar.append(from0To19[int(w)] + ' ' + tho[1])
        elif int(w) >= 5:
            print(int(w))
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

    print('slovar', slovar, int(w))
    if 100 <= int(w) <= 999:
        print(int(w))

        slovar.append(hundreds[(int(w) // 100) - 1] + ' ' + tens[(int(w) % 100) // 10 - 1] + ' ' + from0To19[int(w) % 10] + ' ' + tho[1])
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


result = creat_arr(122123345678)
print(result)
#
# print(slovar)
# elif i >= 1000:
#     arr = []
#     for e in range(len):
#
#         # print(sl2[e])
#         # if int(sl2[e]) == 1:
#         #     thousand = thousands[0][0]
#         # if 2 >= int(sl2[e]) >= 4:
#         #     thousand = thousands[0][1]
#         # if int(sl2[e]) >= 5:
#         #     thousand = thousands[0][2]
#         if int(sl2[e]) <= 19:
#
#             # if int(sl2[e]) != 1 and int(sl2[e]) != 2:
#             #     arr.append(from0To19[int(sl2[e])])
#             #
#             # else:
#             #     arr.append(from0To2[int(sl2[e])])
#
#             if int(sl2[e]) == 1:
#                 arr.append(from0To2[int(sl2[e])] + ' ' + thousands[0][0] + ' ')
#             elif int(sl2[e]) == 2:
#                 arr.append(from0To2[int(sl2[e])] + ' ' + thousands[0][1] + ' ')
#             elif int(sl2[e]) == 3 or int(sl2[e]) == 4:
#                 arr.append(from0To19[int(sl2[e])] + ' ' + thousands[0][1] + ' ')
#             if int(sl2[e]) > 4:
#                 arr.append(from0To19[int(sl2[e])] + ' ' + thousands[0][2] + ' ')
#                 # arr.append(from0To2[int(sl2[e])])
#         elif 19 < int(sl2[e]) <= 99:
#             # print(int(sl2[e]) % 10)
#             if int(sl2[e]) % 10 == 1:
#                 arr.append(tens[(int(sl2[e]) // 10) - 1] + ' ' + from0To2[(int(sl2[e]) % 10)] + ' ' + thousands[0][0])
#             elif int(sl2[e]) % 10 == 2:
#                 arr.append(tens[(int(sl2[e]) // 10) - 1] + ' ' + from0To2[(int(sl2[e]) % 10)] + ' ' + thousands[0][1])
#             elif int(sl2[e]) % 10 == 3 or int(sl2[e]) % 10 == 4:
#                 arr.append(tens[(int(sl2[e]) // 10) - 1] + ' ' + from0To19[(int(sl2[e]) % 10)] + ' ' + thousands[0][1])
#             elif int(sl2[e]) % 10 >= 5:
#                 arr.append(tens[(int(sl2[e]) // 10) - 1] + ' ' + from0To19[(int(sl2[e]) % 10)] + ' ' + thousands[0][2])
#             elif int(sl2[e]) % 10 == 0:
#                 arr.append(tens[(int(sl2[e]) // 10) - 1] + ' ' + from0To19[(int(sl2[e]) % 10)] + ' ' + thousands[0][2])
#
#             # arr.append(tens[(int(sl2[e]) // 10) - 1] +  ' ' + from0To19[(int(sl2[e]) % 10)] + ' ' + thousands[0][2])
#         elif 100 < int(sl2[e]) <= 999:
#
#             w = int(sl2[0]) % 100
#             print(w)
#
#             if w <= 19:
#                 if int(sl2[e]) % 100 == 1:
#                     arr.append(
#                         tens[(int(sl2[e]) // 100) - 1] + ' ' + from0To2[(int(sl2[e]) % 100)] + ' ' + thousands[0][0])
#                 elif int(sl2[e]) % 100 == 2:
#                     arr.append(
#                         tens[(int(sl2[e]) // 100) - 1] + ' ' + from0To2[(int(sl2[e]) % 100)] + ' ' + thousands[0][1])
#                 elif w == 3 or w == 4:
#                     print(tens[(int(sl2[e]) // 10) - 1])
#                     # arr.append(
#                     #     tens[(int(sl2[e]) // 10) - 1] + ' ' + from0To19[(int(sl2[e]) % 10)] + ' ' + thousands[0][1])
#                 elif int(sl2[e]) % 100 >= 5:
#                     arr.append(
#                         tens[(int(sl2[e]) // 100) - 1] + ' ' + from0To19[(int(sl2[e]) % 100)] + ' ' + thousands[0][2])
#                 elif int(sl2[e]) % 100 == 0:
#                     arr.append(
#                         tens[(int(sl2[e]) // 100) - 1] + ' ' + from0To19[(int(sl2[e]) % 100)] + ' ' + thousands[0][2])
#                 to19 = from0To19[w]
#             elif 19 < w <= 99:
#                 to19 = (tens[(w // 10) - 1] + ' ' + from0To19[(w % 10)])
#
#             arr.append(hundreds[(int(sl2[e]) // 100) - 1] + ' ' + to19)
#
#
# a = 0
# for f in arr:
#     a += 1
#     if a == 2:
#         # print(sl2[0])
#         if str(sl2) == 1:
#             thousand = thousands[0][0]
#             # print(thousand)
# # print(a)
# print(arr)



    # if 'две' or 'три' or 'четыре' in arr[0]:
    #     thousand = thousands[0][1]
    #
    # else:
    #     thousand = thousands[0][2]
    #
    # arr_tmp.append(arr[0] + ' ' + thousand + ' ' + arr[1])
# print(arr_tmp)


# print(arr)
#
#
# # функция подмены падежей
# for g in arr:
#     str1 = [_.replace('се', 'YYYY') for _ in arr]
# print(str1)


# a = 0
# for j in arr:
#     a += 1
# if a == 2:
#     if int(arr[0]) == 1:
#         res = arr[0] +  arr[1]
# print(res)

        # print(sl2[e])


    # j = i % 1000
    # tmp = hundreds[(j // 100) - 1] + ' ' + tens[((j // 10) % 10) - 1] + ' ' + from0To19[(j % 10)]
    # res = from0To19[(i // 1000)] + ' ' + thousands[0][0] + ' ' + hundreds[(j // 100) - 1]


# print(tmp)
# print(res)

# print(i // 10)
# print(i % 10)
#
# print(i // 100)
# print((i // 10) % 10 )
# print(i % 10)

# print(i // 1000)
# print((i // 100) % 100 )
# print(i % 1000)