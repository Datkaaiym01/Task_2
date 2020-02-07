a = b = 1
n = int(input())
if n < 2:
    print('ERROR')
else:
    for i in range(2, n):
        a, b = b, a + b
    print(b)