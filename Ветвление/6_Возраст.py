# user = int(input())
# n = user % 10
# if (user > 9) and (user < 20) or (user > 110) or (n > 4) or (n == 0):
#     print(f'Вам {user} лет.')
# elif n == 1:
#     print(f'Вам {user} год.')
# else:
#     print(f'Вам {user} года.')
user = int(input())
n = user % 10
if (user > 9) and (user < 20) or (user > 110) or (n > 4) or (n == 0):
    print('Вам', user, 'лет.')
elif n == 1:
    print('Вам', user, 'год.')
else:
    print('Вам', user, 'года.')