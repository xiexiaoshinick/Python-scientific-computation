%module(directors="1") demo

%{
#include <stdio.h>
#include "demo.h"
%}

FILE *fopen(const char *filename, const char *mode);
int fputs(const char *, FILE *);
int fclose(FILE *);

double global_test;
void print_global();

double * make_array(int n);
void free_array(double * x);
double get_element(double * x, int n);
void set_element(double * x, int n, double v);

struct Point
{
    double x, y;
};

class CPoint
{
public:
    double x, y;
    double power();
};

//void add_mult(double x, double y, double * OUTPUT, double *OUTPUT);

%apply double *OUTPUT {  double *p, double *s };
void add_mult(double x, double y, double * s, double *p);
%clear double *s, double *p;

double add(double *INPUT, double *INPUT);

void inc(int *INOUT);

double sum_func(double (*op)(double), int s, int e);

%callback("cb_%s");
double square(double x);
double reciprocal(double x);
double linear(double x);
%nocallback;

%feature("director") Sum;
class Sum
{
    public:
    double Cal(int s, int e);
    virtual double Func(double x);
};
