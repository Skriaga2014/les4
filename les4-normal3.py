'''
# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# # Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
'''

import random                                           # Импортируем модуль для создания случайного ряда чисел

ch = ""                                                 # Пустая строковая переменная
for i in range(2500):                                   # 2500 раз добавляем в строку случайное число от 0 до 9
       ch += str(random.randint(0,9))
if ch[0] == "0": ch = str(random.randint(1,9)) + ch[1:] # Если строка начинается с 0, то заменяем начало на число 1-9
f = open ("les4-3.txt","w")                             # Открываем файл les4-3.txt для записи
f.write(ch)                                             # Записываем в него созданную из случайных чисел переменную
f.close()                                               # Закрываем файл.

n = open ("les4-3.txt","r")                             # Открываем файл les4-3.txt на чтение
ch2 = n.read()                                          # Содержимое файла присваиваем переменной ch2

                                                 # ВАРИАНТ 1:

long = []                                               # Будущий список с длинными последовательностями каждого числа
for i in range (0,10):                                  # Используем каждое число от 0 до 9
       num = 0                                          # Будущая переменная с числом элементов в последовательности
       record = 0                                       # Рекорд повторений в последовательности
       for t in ch2:                                    # Просмотр переменных в импортированной строке
              if t == str(i): num += 1                  # Если искомое число = t, увеличиваем счетчик повторов
              else: num = 0                             # Если искомое число не равно t, обнуляем счетчик повторов
              if num > record: record = num             # Если счетчик повторов больше, чем было до этого = новый рекорд
       long.append(str(i)*record)                       # Умножаем искомое число на рекорд последовательности повторений

len_max = max(len(i) for i in long)                     # Ищем, сколько символов в самой длинной последовательности
print ("Вариант 1: Самые длинные комбинации цифр:")                #
for i in long:                                          # Если длина последовательности в списке последовательностей
       if len(i) == len_max: print (i)                  # равна длине самой длинной последовательности, то принтим её

                                                 # ВАРИАНТ 2:

max_long = 0                                            # Максимальная длина последовательности
print ("Вариант 2: Самые длинные комбинации цифр:")
for i in reversed(range(len(ch2))):                     # Паребираем числа по убыванию от 2500...
       for r in range (0,10):
              if ch2.count(str(r)*i) > 0:               # Первое встречное число - максимальная длина последовательности
                     if max_long == 0: max_long = len(str(r)*i)
                     if len(str(r)*i) == max_long:      # если длина последовательности равна длине макс. последоват.:
                            print(str(r) * i)           # принтим эту последовательность

                                                 # ВАРИАНТ 3:

import re

max_long = max(len(i) for i in re.findall("[0]+|[1]+|[2]+|[3]+|[4]+|[5]+|[6]+|[7]+|[8]+|[9]+", ch2))
www = [i for i in re.findall("[0]+|[1]+|[2]+|[3]+|[4]+|[5]+|[6]+|[7]+|[8]+|[9]+", ch2) if len(i) == max_long]
print ("Вариант 3: Самые длинные комбинации цифр:",sorted(set(www)))

