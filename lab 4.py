import matplotlib.pyplot as plt
import numpy as np
def f(x_arr, coeff):
    res = np.zeros(len(x_arr))
    for i in range(len(coeff)):
        res += coeff[i]*(x_arr**i)
    return res       
def show_graf(matr):
    t = np.arange(-1.0, 10.0, 0.02)
    plt.figure(1)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(t, f(t, matr), 'k')
    for i in range(len(x)):
        plt.plot(x[i], y[i], 'o', markersize=6)
    plt.show()
    
def table(x, y, w):
    print("x\t y\t Вec")
    for i in range(len(x)):
        print(x[i],"\t", y[i],"\t", w[i])
    print()
def print_matrix(x):
    for i in x:
        print(i)
def read_file():
    f = open("file_1.txt", "r")
    x = []
    y = []
    w = []
    for i in f:
        i = i.split(" ")
        x.append(float(i[0]))
        y.append(float(i[1]))
        w.append(float(i[2]))
    return x, y, w

def root(x, y, ro, n): #n - кол-во искомых коэффициентов
    length = len(x)
    sum_x_n = [sum([x[i]**j*ro[i] for i in range(length)]) for j in range(n*2 -1)]
    sum_y_x_n = [sum([x[i]**j*ro[i]*y[i] for i in range(length)]) for j in range(n)]
    matr = [sum_x_n[i:i+n] for i in range(n)]

    for i in range(n):
        matr[i].append(sum_y_x_n[i])
    return Gauss(matr)


def Gauss(matr):
    n = len(matr)
    # приводим к треугольному виду
    for k in range(n):
        for i in range(k+1,n):
            coeff = -(matr[i][k]/matr[k][k])
            for j in range(k,n+1):
                matr[i][j] += coeff*matr[k][j]
    print("\ntriangled:")
    print_matrix(matr)
    # находим неизвестные
    a = [0 for i in range(n)]
    print("res = ", a)
    for i in range(n-1, -1, -1):
        for j in range(n-1, i, -1):
            matr[i][n] -= a[j]*matr[i][j]
        a[i] = matr[i][n]/matr[i][i]
    return a
n = int(input('Степень полинома: '))
x, y, weight = read_file()
table(x, y, weight)
a = root(x, y, weight, n+1)
show_graf(a)
