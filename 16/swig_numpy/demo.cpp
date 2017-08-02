#include <stdio.h>
#include <math.h>
#include "demo.h"

void drange(double * x, int n)
{
    for(int i=0;i<n;i++) x[i]  = i;
}

void rot2d(double x[3][3], double th)
{
    x[0][2] = 0;
    x[1][2] = 0;
    x[2][0] = 0;
    x[2][1] = 0;
    x[0][0] = cos(th);
    x[0][1] = -sin(th);
    x[1][0] = sin(th);
    x[1][1] = cos(th);
    x[2][2] = 1;
}

double sum_power(double * x, int n)
{
    double sum = 0;
    for(int i=0;i<n;i++) sum += x[i]*x[i];
    return sum;
}

void power(double *x, int n)
{
    for(int i=0;i<n;i++) x[i] *= x[i];
}