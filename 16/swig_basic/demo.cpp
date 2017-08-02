#include <stdio.h>
#include "demo.h"

double global_test = 100.0;

void print_global()
{
    printf("global_test=%f\n", global_test);
}

double * make_array(int n)
{
    return new double[n];
}

void free_array(double * x)
{
    delete[] x;
}

double get_element(double * x, int n)
{
    return x[n];
}

void set_element(double * x, int n, double v)
{
    x[n] = v;
}

double CPoint::power()
{
    return x*x + y*y;
}

void add_mult(double x, double y, double * s, double *p)
{
	*s = x + y;
	*p = x * y;
}

double add(double *x, double *y)
{
    return *x + *y;
}

void inc(int *x)
{
    (*x)++;
}

double sum_func(double (*op)(double), int s, int e)
{
    double sum = 0;
    int i;
    for(i=s;i<e;i++)
    {
        sum += (*op)(i);
    }
    return sum;
}

double square(double x)
{
    return x*x;
}

double reciprocal(double x)
{
    return 1/x;
}

double linear(double x)
{
    return 0.5*x+1;
}

