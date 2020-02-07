import random
n,k = map(int,input().split())
a = []
for x in range(n):
    a.append(random.randint(1,6))
print(a)
c = [x for x in range(len(a)) if a[x] == k]
for x in c:
    print(x)
