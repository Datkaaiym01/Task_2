#Даны три меры угла в градусах, требуется определить – могут ли эти три угла
# являться углами одного треугольника.
            # Формат входных данных:
# Строка содержит три целых числа A,B,C (числа от 0 до 180).
            # Формат выходных данных:
# Вывести “YES

A, B, C = map(int, input().split())

if A + B + C <= 180 and A > 0 and B > 0 and C > 0:
    print('YES')
else:
    print('NO')