a = input()
b = list(a)
for x in b[:]:
    if int(x) % 2 == 0:
        b.remove(x)

S = ''.join(b)
print(S)