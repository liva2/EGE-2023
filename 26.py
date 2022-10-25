#задача 90
a = open('26-90.txt')
n = int(next(a).rstrip())
x = []
for i in range(n):
    b = int(next(a).rstrip())
    x.append(b)
d = sorted(x,reverse = True)
s_my = 0
s_mag = 0
for i in range(0, n):
    if i < n // 4:
        s_my = s_my + d[i] * 0.5
    else:
        s_my = s_my + d[i]
print(s_my )
d = sorted(x,reverse = False)
for i in range(0, n):
    if i < n//4:
        s_mag  = s_mag + d[i] * 0.5
    else:
        s_mag = s_mag + d[i]
print(s_mag )
#задача 95
# a = open('26-95.txt')
# n = int(next(a).rstrip())
# x = {}
# for i in range(n):
#      b, c = map(int, next(a).rstrip().split())
#      x[b] = sorted(x.get(b, []) + [c])
# #print(x)
# mini_pod = 0
# domm = {}
# for i, j in x.items():
#      f = 0
#      if len(j) >= 3:
#           for y in range(len(j)-2):
#                if j[y + 1] - j[y] == j[y + 2] - j[y + 1]:
#                     mini_pod = j[y] - 1
#                     f = 1
#                elif (j[y + 1] - j[y])  == 1 and (j[y+2] - j[y+1]) == 2:
#                     mini_pod = j[y + 1] + 1
#                     f = 1
#                elif (j[y + 2] - j[y + 1]) == 1 and (j[y + 1] - j[y]) == 2:
#                     mini_pod = j[y + 1] - 1
#                     f = 1
#                if f==1:
#                     domm[i] = domm.get(i, []) + [mini_pod]
#                     break
#      else:
#           continue
# print(len(domm), *list(max(domm.items()))[1])

#*****************************************************************************************************

# задача 96
#
# a = open('26-96.txt')                       #встаём на начало файла
# n = int(next(a).rstrip())                   #считываем 1-ю строчку файла
# #print(n)
# x = {}                                      #словарь ключ - долгота, значение - широта
# for i in range(n):
#     b, c = map(int,next(a).rstrip().split())    # читаем широту долготу
#     if b >= 0:
#         modB =b // 10
#     else:                                       # если широта < 0, то инвертируем в >0 затем добавим знак -
#         modB = -(-b // 10)
#     x[c] = x.get(c,[]) + [modB]                 # значение в словаре это список целых частей широт делённых на 10
# #print(x)
# m = 1
# for i, j in x.items():                          # проходим по ключ -значениям словаря
#     if len(j)> m:                               # выбираем спиок значений наибольшей длины
#         m = len(j)
#         keyy = i                                # запоминаем ключ и сам список
#         dolg = j
# print(dolg)
# print(keyy, len(set(dolg)))                     # печатаем долготу и количество сигналов
#
