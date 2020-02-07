a, b = map(int, input().split())
c = 0
if a > 0 and b < 0 or a == b and a > 0 and b > 0:
    for x in range(a):
     c = c + b
elif a < 0 and b> 0 or a < 0 and b < 0:
    for x in range(abs(a)):
     c = c - b

print('{}*({})={}'.format(a,b,c))