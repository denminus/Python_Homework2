#Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
#Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а 
#Катя должна их отгадать. Для этого Петя делает две подсказки. 
#Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
import math
x=int(input("Введите чило X при условии(X≤1000) "))
y=int(input("Введите чило Y при условии(Y≤1000) "))
s=float(input("Введите сумму X и Y "))
p=float(input("Введите произведение X и Y "))
print("Загаданные числа ",x, "и", y )
d=s*s-4*p
if d<0:
    print("Решения нет, неверно введены значения ")
elif d==0:
    x1=s/2
    print("Число X равно ", int(round(x1)), "Число Y равно ", int(round(s-x1)))
elif d>0:
    x1=(s+math.sqrt(d))/2
    x2=(s-math.sqrt(d))/2
    print("Решение имеет следующие два значения :")
    print("Число X1 равно ", int(round(x1)), "Число Y1 равно ", int(round(s-x1)))
    print("Число X2 равно ", int(round(x2)), "Число Y2 равно ", int(round(s-x2)))







