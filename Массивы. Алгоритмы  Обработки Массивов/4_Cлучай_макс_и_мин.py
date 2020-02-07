import random

n = int(input())
a = []
b = [a.append(random.randint(-100,100)) for x in range(n)]
del b
max_value = max(a)
min_value = min(a)
max_index = a.index(max_value)
min_index = a.index(min_value)
print(*a, sep=" ")
print("{} {}".format(min_value, min_index))
print("{} {}".format(max_value, max_index))