def NOR(x, y):
    if x | y:
        print(0)
    else:
        print(1)

a = int(input())
for c in range(a):
    x, y = map(int, input().split())
    NOR(x,y)