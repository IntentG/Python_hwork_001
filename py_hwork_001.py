'''Напишите программу, которая принимает на вход цифру, обозначающую день недели,
 и проверяет, является ли этот день выходным.

Пример:
- 6 -> да
- 7 -> да
- 1 -> нет'''

day_number = int(input("Введите число дня недели:   "))

def WeekEnd (number):
    if number > 0 and number <= 7:
        if number > 0 and number <= 5:
            print (f"{number} день - будний.")
        else:
            print (f"{number} день - выходной.")
    else:
        print ("Введите Земной день недели")


WeekEnd (day_number)
