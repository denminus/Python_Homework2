#Задача 10:
#На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
#Определите минимальное число монеток, которые нужно перевернуть, 
#чтобы все монетки были повернуты вверх одной и той же стороной.
#Выведите минимальное количество монет, которые нужно перевернуть

n=int(input("Введите количество монеток "))
orel=0
reshka=0

for i in range(n):
    m=i+1
    print("Если монетка ", m , "лежит орлом вверх нажмите вставьте число 0, если решкой то любое другое")
    o = int(input())
    if o == 0:
        orel += 1
    else:
        reshka += 1
print("Минимальное количество монет, которые нужно перевернуть: ")
if reshka >= orel:
    print(orel)
else:
    print(reshka)

