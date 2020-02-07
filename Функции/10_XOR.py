def XOR(x, y):
    if x ^ y:
        print('1')
    else:
        print('0')

a = int(input())
for c in range(a):
    x, y = map(int, input().split())
    XOR(x,y)
