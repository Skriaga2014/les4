'''
# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
'''

import random                                       # Импортируем модуль random для создания списка произвольных чисел

list = [random.randint(1,10) for i in range(10)]    # Создаем список произвольных 10 чисел 1-10
print ("list: ", list)                              # Выводим созданный список

list2 = [i**2 for i in list]                        # Каждый элемент созданного списка позводим в квадрат в список list2
print ("list2:", list2)                             # Выводим список list2

#