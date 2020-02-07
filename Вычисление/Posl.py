# ариф. прогрессия
# ввод: 3 4 5
# вывод: 7
a1, a2, an = map(int, input().split())
an = a1 + (an-1)*(a2-a1)
print(an)