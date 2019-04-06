from math import *

def f(x, y):
    return x*x + y*y
'''
## Массивы значений абсцисс и ординат
def get_array(x_beg, step, amount):
    x_tbl = [x_beg + step*i for i in range(amount)]
    y_tbl = [f(x) for x in x_tbl]
    return x_tbl, y_tbl
'''
##############
##############
def get_table(x_beg, x_h, x_n, y_beg, y_h, y_n):
    x = [x_beg + i*x_h for i in range(x_n)]
    y = [y_beg + i*y_h for i in range(y_n)]
    z = [[f(i, j) for i in x] for j in y]
    return x, y, z
##############
##############

## Вывод таблицы значений
def print_table(x, y, z):
    
    print("   y\\x ", end = '')
    for i in x:
        print("{:6}".format(i), end = ' ')
    
    for i in range(len(y)):
        print("\n{:6}".format(y[i]), end = ' ')
        for j in z[i]:
            print("{:6}".format(j), end = ' ')
    print('\n')
    
## Матрица разделенных разностей
def matrix(tbl, n):
    for i in range(n):
        tmp = []
        for j in range(n-i):
            tmp.append((tbl[i+1][j] - tbl[i+1][j+1]) / (tbl[0][j] - tbl[0][i+j+1]))
        tbl.append(tmp)
    return tbl

## Выбор ближайших точек
def dots(tbl, n, x):
    tbl_len = len(tbl)
    i_near = min(range(tbl_len), key = lambda i: abs(tbl[i] - x)) #
    space_needed = ceil(n / 2)    
    if (i_near + space_needed + 1 > tbl_len):
        i_end = tbl_len
        i_start = tbl_len - n
    elif (i_near < space_needed):
        i_start = 0
        i_end = n
    else:
        i_start = i_near - space_needed + 1
        i_end = i_start + n        

    return i_start, i_end

#### Непосресредственно интерполяция
##def interpolation(tbl, n, x):
##    matr = get_diff_matr(tbl, n)
##    tmp = 1
##    res = 0
##    for i in range(n+1):
##        res += tmp * matr[i+1][0]
##        tmp *= (x - matr[0][i])
##    return res
##
##def multi_interpolate(x, y, z, x_value, y_value, x_n, y_n):
##    ix_beg, ix_end = choose_dots(x, x_n + 1, x_value)
##    iy_beg, iy_end = choose_dots(y, y_n + 1, y_value)
##
##    x = x[ix_beg : ix_end]
##    y = y[iy_beg : iy_end]
##    z = z[iy_beg : iy_end]
##    for i in range(y_n + 1):
##        z[i] = z[i][ix_beg : ix_end]
##
##    result = [interpolate([x, z[i]], x_n, x_value) for i in range(y_n + 1)]
##    
####    [newtons_interpolation([x, z[i]], x_n, x_val) for i in range(y_n + 1)]
##    res = interpolate([y, result], y_n, y_value) 
##    return res #([y, res], y_n, y_val)

def get_diff_matr(tbl, n):
    for i in range(n):
        tmp = []
        for j in range(n-i):
            tmp.append((tbl[i+1][j] - tbl[i+1][j+1]) / (tbl[0][j] - tbl[0][i+j+1]))
        tbl.append(tmp)
    return tbl

def newtons_interpolation(tbl, n, x):
    matr = get_diff_matr(tbl, n)
    tmp = 1
    res = 0
    for i in range(n+1):
        res += tmp * matr[i+1][0]
        tmp *= (x - matr[0][i])
    return res

def multi_interpolate(x, y, z, x_val, y_val, x_n, y_n):
    ix_beg, ix_end = dots(x, x_n + 1, x_val)
    iy_beg, iy_end = dots(y, y_n + 1, y_val)

    x = x[ix_beg : ix_end]
    y = y[iy_beg : iy_end]
    z = z[iy_beg : iy_end]
    for i in range(y_n + 1):
        z[i] = z[i][ix_beg : ix_end]

    #print("Choosen dots:"
    #print_matrix(x, y, z)

    res = [newtons_interpolation([x, z[i]], x_n, x_val) for i in range(y_n + 1)]
    return newtons_interpolation([y, res], y_n, y_val)


x_beg = float(input("Введите начало для x: "))
x_h = float(input("Введите шаг для х: "))
x_N = int(input("Введите количество точек: "))

y_beg = float(input("Введите начало для y: "))
y_h = float(input("Введите шаг для y: "))
y_N = int(input("Введите количество точек: "))

x, y, z = get_table(x_beg, x_h, x_N, y_beg, y_h, y_N)
##print("\nCreated matrix:")
print_table(x, y, z)

x_n = int(input("Введите степень полинома для х: "))
x_find = float(input("Введите x: "))

y_n = int(input("Введите степень полинома для у: "))
y_find = float(input("Введите y: "))

# Results
found = multi_interpolate(x, y, z, x_find, y_find, x_n, y_n)
print("\nВычисленное значение   : ", found)
print("F(x, y)        : ", f(x_find, y_find))
print("Погрешность          : ", abs(f(x_find, y_find) - found), "\n")
    
