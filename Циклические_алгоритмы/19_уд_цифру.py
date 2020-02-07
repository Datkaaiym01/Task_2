a = input()
c = int(input())
b = list(a)
for x in b[:]:
    if int(x) == c:
        b.remove(x)
S = ''.join(b)
print(S)