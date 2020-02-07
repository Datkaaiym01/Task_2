# площадь и периметр треугольника
# ввод: 0.0 0.0 3.0 3.0 2.1 1.1
# вывод: 8.71567 1.5
x1, y1, x2, y2, x3, y3 = map(float, input().split())
P = abs(((x1-x2)**2 + (y2-y1)**2)**0.5 + ((x3-x2)**2 + (y3-y2)**2)**0.5 + ((x3-x1)**2 + (y3-y1)**2)**0.5)
S = abs( x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2) ) / 2.0
print(P, S)