import random


def trace(mat, contr): 
    i = 0 
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(f'|{mat[i][j] : .6f}', end='')
        print(f'|{contr[i]:.6f}')
        print( '--' * 5*len(mat[i]))
    print('#'*50)


def swap(mat, i, contr): 
    if i < len(mat) - 1: 
        for j in range(len(mat[i])): 
            mat[i][j], mat[i+1][j] = mat[i+1][j], mat[i][j]
            contr[i], contr[i+1] = contr[i+1], contr[i]
        else:
            mat[i][j], mat[0][j] = mat[0][j], mat[i][j]
            contr[i], contr[0] = contr[0], contr[0]
    temp = [mat, contr]
    return temp


def solve(mat, x, n): 
    if n == len(mat) - 1: 
        x[n] = mat[len(mat) -1][len(mat[n]) - 1]/mat[len(mat)-1][len(mat[n]) - 2]
        return x[n]
    solsum = mat[n][len(mat[n])-1]
    for i in range(len(mat[n])-2, 0, -1):
        solsum -= mat[n][i] * x[i]
    x[n] = solsum/mat[n][n]
    return x[n]



def det(mat, total = 0): 
    ind = list(range(len(mat)))
    if len(mat) == 2 and len(mat[0]) == 2:
            return mat[0][0]*mat[1][1] - mat[1][0]*mat[0][1]
    for fc in ind: 
        temp_mat = mat.copy()
        temp_mat = temp_mat[1:]
        hei = len(temp_mat)
        for i in range(hei): 
            temp_mat[i] = temp_mat[i][:fc] + temp_mat[i][fc+1:]
        sign = (-1) ** (fc%2)
        sub_det = det(temp_mat)
        total += sign * mat[0][fc] * sub_det 
    return total
        

mat = [[-7, -9, 1, -9, 29],
       [-6, -8, -5, 2, 42],
       [-3, 6, 5, -9, 11],
       [-2, 0, -5, -9, 75]]
contr = [sum(mat[0]), 
         sum(mat[1]), 
         sum(mat[2]), 
         sum(mat[3])]
det_mat = [mat[i][:len(mat)] for i in range(len(mat))]
x = [0,
     0,
     0,
     0]
trace(mat, contr)

temp = [mat, contr]
for i in range(len(mat) - 1): 
    if mat[i][i+1] == 0: 
        temp = swap(mat, i, contr)
    mat = temp[0]
    contr = temp[1]

for i in range(len(mat)-1):
    for j in range(i+1, len(mat)):
        if mat[j][i] != 0:
            coef = mat[j][i]/mat[i][i]
            for k in range(len(mat[j])): 
                mat[j][k] -= mat[i][k] * coef
                contr[j] -= contr[i] * coef 

trace(mat, contr)

for i in range(len(mat)-1, -1, -1): 
    x[i] = solve(mat, x, i)

for i in range(len(x)): 
    print(f'x{i+1} = {x[i]:.6f}')

determ = det(det_mat)
print(f'det Mat = {determ}')

minor_mat = det_mat 
temp = det_mat 
backup = [0,0,0]
for i in range(len(mat)):
    temp = det_mat[:i] + det_mat[i+1:]
    sec_temp = det_mat[:i] + det_mat[i+1:]
    for j in range(len(temp)+1):
        for k in range(len(temp)): 
            temp[k] = sec_temp[k][:j] + sec_temp[k][j+1:]
    minor_mat[i][j] = det(temp)

for i in range(len(minor_mat)//2): 
    for j in range(len(minor_mat)//2): 
        minor_mat[i][j], minor_mat[j][i] = minor_mat[i][j], minor_mat[j][i] 

for i in range(len(minor_mat)): 
    for j in range(len(minor_mat)): 
        if (i+1 % 2 == 0) or (j+1 % 2 == 0): 
            minor_mat[i][j] = -minor_mat[i][j] / determ
        else: 
            minor_mat[i][j] /= determ

if determ == 0: 
    print('Обратной матрицы не существует, т.к. заданная матрица является вырожденной')
else: 
    print('обратная матрица: \n' + '--' * 5*len(minor_mat))
    for i in range(len(minor_mat)):
        for j in range(len(minor_mat)):
            print(f'|{minor_mat[i][j]:.6f}', end='')
        print('|\n'+'--' *5*len(minor_mat))
