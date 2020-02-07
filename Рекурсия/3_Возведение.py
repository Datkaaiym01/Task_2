A, B = map(int, input().split())
b = A
n = B
# o = 1
def expt(b, n):
    if n == 0:
        print('1')
        return 1
    print ('%s*' %A)
    return b*expt(b, n-1)
# print(('%s*' %A)*B '%s' %o)
print(expt(A, B))
