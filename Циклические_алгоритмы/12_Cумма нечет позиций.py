a = input()
b = list(a)
k = 0
for x in range(0, len(b),2):
    k+=int(b[x])
print(k)