a = int(input())
b = list(map(int,input().split()))
b[b.index(max(b))], b[b.index(min(b))] = b[b.index(min(b))], b[b.index(max(b))]
print(' '.join(map(str, b)))
