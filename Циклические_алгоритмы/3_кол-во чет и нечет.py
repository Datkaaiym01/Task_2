a = input()
b = list(a)
i = 0
k = 0
for x in b:
    if int(x) % 2 == 0:
        i+=1
    if int(x) % 2 == 1:
        k+=1

print(k, i)