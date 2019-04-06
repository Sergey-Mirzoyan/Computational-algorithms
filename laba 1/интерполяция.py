from math import *

def f(x):
    return x**2

## Массивы значений абсцисс и ординат
def get_array(x_beg, step, amount):
    x_tbl = [x_beg + step*i for i in range(amount)]
    y_tbl = [f(x) for x in x_tbl]
    return x_tbl, y_tbl

## Вывод таблицы значений
def print_table(x, y):
    length = len(x)
    print("X\tY")
    for i in range(length):
        print("%.4f\t%.4f" % (x[i], y[i]))
    print()
    
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
    tbl_len = len(tbl[0])
    i_near = min(range(tbl_len), key = lambda i: abs(tbl[0][i] - x)) #
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

    return [tbl[0][i_start:i_end], tbl[1][i_start:i_end]]

## Непосресредственно интерполяция
def interpolate(tbl, n, x):
    tbl = dots(tbl, n + 1, x)
    matr = matrix(tbl, n)
    tmp = 1
    res = 0
    for i in range(n+1):
        res += tmp * matr[i+1][0]
        tmp *= (x - matr[0][i])
    return res
        

x_beg = float(input("Введите начало  "))
x_step = float(input("Введите шаг: "))
x_amount = int(input("Введите количество точек: "))

x_tbl, y_tbl = get_array(x_beg, x_step, x_amount)

print_table(x_tbl, y_tbl)

n = int(input("Введите степень полинома: "))
if 1 <= n < len(x_tbl):
        
    x = float(input("Введите x: "))
    if x_tbl[0]< x < x_tbl[len(x_tbl)-1]:
        found = interpolate([x_tbl, y_tbl], n, x)

        print("\nВысчитанное значение: ", found)
        print("Точное значение     : ", f(x))
        print("Погрешность         : ", abs(f(x) - found), "\n")
        print("Корень функции: ", interpolate([y_tbl, x_tbl], n, 0))
    else:
        found = interpolate([x_tbl, y_tbl], n, x)

        print("\nВысчитанное значение: ", found)
        print("Точное значение     : ", f(x))
        print("Погрешность         : ", abs(f(x) - found), "\n")
        print("Корень функции: ", interpolate([y_tbl, x_tbl], n, 0))
        print("Х находится за пределами значений таблицы. Случай экстраполяции")
elif n >= len(x_tbl):
    print("Слишком большое значение полинома")
else:
    print("Слишком малое значение полинома")
    
