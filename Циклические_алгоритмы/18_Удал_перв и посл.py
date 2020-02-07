a = input()
b = list(a)
c = b[1:-1]
for x in range(len(c)):
    if c[0] == '0':
        c.remove('0')
S = ''.join(c)
print(S)