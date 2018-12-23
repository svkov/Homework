# 1

d = {
    'Python': 'Питон',
    'I': 'Я',
    'Love': 'Люблю'
}

print(' '.join([d['I'], d['Love'], d['Python']]))

# 2

# we need to copy dictionary to iterate through non-updated keys
for i in d.copy().keys():
    v = d[i]
    d[v] = i
print(' '.join([d['Я'], d['Люблю'], d['Питон']]))

# 3

a = (1, 2, 3)
# a.append(5) - exception, tuple is immutable

b = [1, 2, 3]
b.append(5)  # OK, list is mutable

# 4

import random

n = int(input())
for i in range(5):
    # we need matrix contain numbers in string type
    matrix = [[str(random.randint(0, 10)) for i in range(n)] for j in range(n)] # generator of generator
    file = open(str(i + 1)+'.txt', 'w')
    strings = [' '.join(s) for s in matrix]
    file.write(str(n) + '\n' + '\n'.join(strings))
    file.close()

# 5

for i in range(5):
    file = open(str(i + 1)+'.txt', 'r')
    matrix = [s.split() for s in file]
    # in first line we have a dimension
    n = matrix.pop(0)  # to remove dimension of matrix
    n = int(n[0])  # because in n something like ['3']
    # transpose matrix
    matrix_T = [[matrix[col][row] for col in range(n)] for row in range(n)]
    # also you can use this:
    # matrix_T = map(list, zip(*matrix))

    # sorting
    sorted_matrix = [sorted(s) for s in matrix_T]
    # transpose again
    matrix = [[sorted_matrix[col][row] for col in range(n)] for row in range(n)]
    print(matrix)

