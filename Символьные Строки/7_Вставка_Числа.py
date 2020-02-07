a = int(input())
b = list(map(int, input().split()))
input_,i = map(int,input().split())
b.insert(i-1,input_)
for i in b:
    print(i,end=' ')