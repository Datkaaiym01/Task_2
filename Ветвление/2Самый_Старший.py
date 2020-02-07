A, B, C = map(int, input().split(" "))

if A != B and B != C and A != C:
    name = int(max(A, B, C))
    if name == A : print("Anton")
    elif name == B : print("Boris")
    else : print("Victor")
elif A == B == C:
    print("Same age")
else:
    name = int(min(A, B, C))
    if name == A : print("Anton")
    elif name == B : print("Boris")
    else : print("Victor")
