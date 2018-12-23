# 1

a = '1.00001'
b = '2'
c = 500

# a)
d = float(a) + c
# or d = str(c) + a

# b)
d = int(b) + c
# or d = str(c) + b

# c) it will work


# 2
inp = input('Write a character: ')
res = inp + ' - '
inp = inp.lower()
if len(inp) > 1:
    print('Write only ONE character')
elif ord('a') <= ord(inp) <= ord('z'):
    print(res, ord(inp) - ord('a') + 1)
else:
    print('You should write character from a to z')

# 3
inp = input('Введите букву: ')
res = inp + ' - '
inp = inp.lower()
if len(inp) > 1:
    print('Нужно написать только одну букву')
elif ord('а') <= ord(inp) <= ord('е'):
    print(res, ord(inp) - ord('а') + 1) # +1 because а - 0
elif inp == 'ё':
    print(res, 7)
elif ord('ж') <= ord(inp) <= ord('я'):
    print(res, ord(inp) - ord('а') + 2) # +2 because we don't count ё
else:
    print('Введите букву от А до Я')


# 4
a = float(input('A: '))
b = float(input('B: '))
c = float(input('C: '))
# for one-line input you can use:
# a, b, c = list(map(input().split(), float))

# solution without if
print('Max is: ', max(a, b, c))
# min() and max() functions take multiple arguments

#solution with if
if a >= b and a >= c:
    print('Max is: ', a)
elif b >= a and b >= c:
    print('Max is: ', b)
else:
    print('Max is: ', c)
