#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
#не превосходящие числа N.
n=int(input("Введите чило N "))
i = 1
while 2 ** i <= n:
    print("Двойка в степени " , i, "равно ", 2 ** i)
    i += 1
