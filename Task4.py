# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

width_chocolate = int(input('Введите ширину шоколадки: ' ))
length_chocolate = int(input('Введите длину шоколадки: '))
slices = int(input('Введите количество отламываемых долек: '))


if slices % width_chocolate == 0 or slices % lengt_chocolate == 0:
    print('Yes')
else:
    print('No')