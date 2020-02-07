a = int(input())
b = list(map(int, input().split()))
c = max(b)
i = 0
for x in range(a):
    if b[x] == c:
        i+=1
print('{} {}'.format(c,i))