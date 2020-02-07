num = map(int, input().split(' '))
list_ = list(num)
string = ' '.join(map(str, sorted(list_)))
print(string)