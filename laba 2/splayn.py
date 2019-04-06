def f(x):
    return x**2

def table(xb, step, count):
    x = []
    y = []
    
    for i in range(count):
        x.append(xb + step*i)
    for z in x:
        y.append(f(z))
    return x, y

def print_table(x, y):
    for i in range(len(x)):
        print("%.5f %.5f" % (x[i], y[i]))
    print()
'''
def step_f(x):
    result = 0
    for i in range(len(x)):
        if not i:
          result = 0
        else:
            result = x[i] - x[i-1]
    return result
def A_f(x):
    result = 0
    for i in range(len(x)):
        if not i:
          result = 0
        else:
            result = x[i] - x[i-1]
    return result
def B_f(x):
    result = 0
    for i in range(len(x)):
        if i < 2:
          result = 0
        else:
            result = x[i] - x[i-1]
    return result
def D_f(x):
    result = 0
    for i in range(len(x)):
        if i < 2:
          result = 0
        else:
            result = h[]
    return result
def F_f(x):
    result = 0
    for i in range(len(x)):
        if i < 2:
          result = 0
        else:
            result = x[i] - x[i-1]
    return result
'''
def interpolate(x, y, x_value):
    n = len(x)
    i_near = min(range(n), key = lambda i: abs(x[i] - x_value)) # index of nearest value
    if i_near == 0:
        i_near += 1
    h = [0 if not i else x[i] - x[i - 1] for i in range(n)] # step value
    
    A = [0 if i < 2 else h[i-1] for i in range(n)]
    B = [0 if i < 2 else -2 * (h[i - 1] + h[i]) for i in range(n)]
    D = [0 if i < 2 else h[i] for i in range(n)]
    F = [0 if i < 2 else -3 * ((y[i] - y[i - 1]) / h[i] - (y[i - 1] - y[i - 2]) / h[i - 1]) for i in range(n)]

    # forward
    ksi = [0 for i in range(n + 1)]
    eta = [0 for i in range(n + 1)]
    for i in range(2, n):
        ksi[i + 1] = D[i] / (B[i] - A[i] * ksi[i])
        eta[i + 1] = (A[i] * eta[i] + F[i]) / (B[i] - A[i] * ksi[i])

    # backward
    c = [0 for i in range(n + 1)]
    for i in range(n - 2, -1, -1):
        c[i] = ksi[i + 1] * c[i + 1] + eta[i + 1]


    a = [0 if i < 1 else y[i-1] for i in range(n)]
    b = [0 if i < 1 else (y[i] - y[i - 1]) / h[i] - h[i] / 3 * (c[i + 1] + 2 * c[i]) for i in range(n)]
    d = [0 if i < 1 else (c[i + 1] - c[i]) / (3 * h[i]) for i in range(n)]
##    print(a, b, c, d)
    print(a[i_near] + b[i_near] * (x_value - x[i_near - 1]) + c[i_near] * ((x_value - x[i_near - 1]) ** 2) + d[i_near] * ((x_value - x[i_near - 1]) ** 3))
    return a[i_near] + b[i_near] * (x_value - x[i_near - 1]) + c[i_near] * ((x_value - x[i_near - 1]) ** 2) + d[i_near] * ((x_value - x[i_near - 1]) ** 3)




x_beg = float(input("Введите начало  "))
x_step = float(input("Введите шаг: "))
x_amount = int(input("Введите количество точек: "))

x_tbl, y_tbl = table(x_beg, x_step, x_amount)
print_table(x_tbl, y_tbl)

x = float(input("Введите x: "))

# Results
found = interpolate(x_tbl, y_tbl, x)
print("\nВысчитанное значение: %.5f"% found)
print("Точное значение     %.5f: "% f(x))
print("Погрешность         %.5f: "% abs(f(x) - found), "\n")


##################################################
##x_beg = float(input("Введите начало  "))
##x_step = float(input("Введите шаг: "))
##x_amount = int(input("Введите количество точек: "))
##
##x_tbl, y_tbl = get_array(x_beg, x_step, x_amount)
##
##print_table(x_tbl, y_tbl)
##
##n = int(input("Введите степень полинома: "))
##if 1 <= n < len(x_tbl):
##        
##    
##    if x_tbl[0]< x < x_tbl[len(x_tbl)-1]:
##        found = interpolate([x_tbl, y_tbl], n, x)
##
##        print("\nВысчитанное значение: ", found)
##        print("Точное значение     : ", f(x))
##        print("Погрешность         : ", abs(f(x) - found), "\n")
##        print("Корень функции: ", interpolate([y_tbl, x_tbl], n, 0))
##    else:
##        found = interpolate([x_tbl, y_tbl], n, x)
##
##        print("\nВысчитанное значение: ", found)
##        print("Точное значение     : ", f(x))
##        print("Погрешность         : ", abs(f(x) - found), "\n")
##        print("Корень функции: ", interpolate([y_tbl, x_tbl], n, 0))
##        print("Х находится за пределами значений таблицы. Случай экстраполяции")
##elif n >= len(x_tbl):
##    print("Слишком большое значение полинома")
##else:
##
##
##
##
##
##
##
##
##
##
##











    
    
