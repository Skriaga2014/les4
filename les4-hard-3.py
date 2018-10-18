'''
# Задание-3 (Ферзи):
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
# друг друга. Вам дана расстановка 8 ферзей на доске.
# Определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 — координаты 8 ферзей.
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.
'''




def positions(x,y):
    poss = []
    for i in range(8):
        poss.append([x + i, y + i])
        poss.append([x - i, y - i])
        poss.append([x + i, y - i])
        poss.append([x - i, y + i])
        poss.append([x, y + i])
        poss.append([x, y - i])
        poss.append([x + i, y])
        poss.append([x - i, y])

    poss = set([str(i) for i in poss if 0 < i[0] < 9 and 0 < i[1] < 9])
    return poss

def impact(f1, f2):
    f1 = positions(*f1)
    f2 = {"["+str(f2[0])+", "+str(f2[1])+"]"}
    if len(f1 & f2) > 0:
        return "YES"
    return "NO"

from random import randint

list = [[randint(1, 8), randint(1, 8)] for i in range(8)]
print ("Координаты ферзей:", list)
for i in list:
    for n in list:
        if i != n: print(i, n, "Бьются? -", impact(i,n))







