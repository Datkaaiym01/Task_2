import math
a, b = map(int,input().split())
for x in range(a,b):
    j = 2
    l = round(math.sqrt(x))
    while x % j != 0 and j <= l:
        j+=1
    if j > l :
        print(x)