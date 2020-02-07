a = input()
b = list(a)
sum = 0
if len(b) % 2 == 1:
    for x in range(len(b)):
        sum+=int(b[x])
else:
    for x in range(len(b)//2):
        sum+=int(b[x])
print(sum)