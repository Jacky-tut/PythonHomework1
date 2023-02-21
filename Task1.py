# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input('Введите трехзначное число: '))
digit_one = number // 100
number_two = number // 10
digit_two = number_two % 10
digit_three = number % 10
digit_summ = digit_one + digit_two + digit_three
print(f'Сумма цифр трехзначного числа равна {digit_summ}')