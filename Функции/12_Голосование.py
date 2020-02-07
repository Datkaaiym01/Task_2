def bool_Election(x, y, z):
    if x == y == z == 1: print('1')
    elif (x == y and y != 0) or (y == z and y != 0) or (x == z and z != 0):
        print('1')
    if x == y == z == 0: print('0')
    elif (x == y and y != 1) or (y == z and y != 1) or (x == z and z != 1):
        print('0')
        
a = int(input())
for c in range(a):
    x, y, z = map(int, input().split())
    bool_Election(x,y,z)