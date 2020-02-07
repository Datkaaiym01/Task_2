a = int(input())
b = list(map(int, input().split()))
b.sort()
s = sum(b[:-1])
if max(b) < s:
    print('YES')
else:
    print('NO')