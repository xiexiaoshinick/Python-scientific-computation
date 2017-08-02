#include "demo.h"

double power(double x)
{
    return x*x;
}

double sum_power(int n)
{
    int i;
    double sum = 0;
    for(i=0;i<n;i++)
        sum += power((double)i);
    return sum;
}
