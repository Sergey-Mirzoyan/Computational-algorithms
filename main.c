#include <stdio.h>
#include <math.h>
#define len 11
void f(float* y, float a0, float a1, float a2)
{
    for (int i = 0; i < len; i++)
        y[i] = (a0 * i)/(a1 + a2*i);
    return;
}
void one_side_left(float* y_left, float* y)
{
    for (int i = 0; i < len - 1; i++)
         y_left[i] = (y[i + 1] - y[i])/1;
    return;
}
void central_dif(float* y_centr, float* y)
{
    for (int i = 1; i < len - 1; i++)
        y_centr[i] = (y[i+1] - y[i-1])/2;
    return;
}
/*
void third(float* y, float *y0, float *yn)
{

    return;
}*/
void Runge(float* y, float* y_runge)
{
    int r = 2;
    for (int i = 1; i < len - 1; i++)
    {
        float yh = (y[i + 1] - y[i - 1]) / (2 * 1);
        float y2h = (y[i + r] - y[i - r]) / (2 * 1 * r);
        y_runge[i] = (yh + (yh - y2h) / (r*r - 1));
    }
    return;
}
float psi(float *y, int i, float a0, float a1, float a2)
{
    return a1*y[i]/(a0 - a2*y[i]);
}
void alignment(float* y, float* y_align, float a0, float a1, float a2)
{
    float  etta[len];
    for (int i = 0; i < len; i++)
        etta[i] = psi(y, i, a0, a1, a2);
    float l[len - 1];
    one_side_left(l, etta);
    for (int i = 1; i < len - 1; i++)
        y_align[i] = l[i] * y[i];
    return;
}
void print(float* y, float* y_left, float* y_centr, float y0, float yn, float *y_runge, float* y_alignment)
{
    printf("x \t y \t \t 1 \t \t 2 \t \t 3 \t \t 4 \t \t 5\n");
    for (int i = 0; i < len; i++)
        if (i == 0)
            printf("%d \t %.4f \t %.4f \t %s \t %.4f \t %s \t %.4f \n", i, y[i], y_left[i], "------", y0, "------", y_alignment[i]);
        else if (i == len-1)
            printf("%d \t %.4f \t %s \t %s \t %.4f \t %s \t %s \n", i, y[i], "------", "------", yn, "------", "------");
        else
            printf("%d \t %.4f \t %.4f \t %.4f \t %s \t\t %.4f \t %.4f\n", i, y[i], y_left[i], y_centr[i], "-----", y_runge[i], y_alignment[i]);
    return;
}
int main (void)
{
    float y[len];
    float y_left[len-1];
    float y_centr[len-2];
    float y_runge[len-2];
    float y_alignment[len - 1];
    float a0;
    float a1;
    float a2;
    float y0;
    float yn;
    puts("Input a0, a1, a2");
    scanf("%f %f %f", &a0, &a1, &a2);
    f(y, a0, a1, a2);
    y0 = (-3*y[0] + 4*y[1] - y[2])/2;
    yn = (-3*y[len-3] + 4*y[len-2] - y[len-1])/2;
    one_side_left(y_left, y);
    central_dif(y_centr, y);
    //third(y, y0, yn);
    Runge(y, y_runge);
    alignment(y, y_alignment, a0, a1, a2);
    print(y, y_left, y_centr, y0, yn, y_runge, y_alignment);
    return 0;
}
