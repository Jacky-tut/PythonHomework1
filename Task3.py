# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, 
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

number_ticket = int(input('Введите шестизначный номер билета: '))
digit_one = number_ticket // 100000
number_ticket_two = number_ticket // 10000
digit_two = number_ticket_two % 10
number_ticket_three = number_ticket // 1000
digit_three = number_ticket_three % 10
number_ticket_four = number_ticket // 100
digit_four = number_ticket_four % 10
number_ticket_five = number_ticket // 10
digit_five = number_ticket_five % 10
digit_six = number_ticket % 10

if digit_one + digit_two + digit_three == digit_four + digit_five + digit_six:
    print('Yes')
else:
    print('No')
   

    

