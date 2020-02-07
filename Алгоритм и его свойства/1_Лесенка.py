a = input()
txt = a.strip().replace('  ', '').split(' ')
for x in range(len(txt)):
    print("  " * x + txt[x])
