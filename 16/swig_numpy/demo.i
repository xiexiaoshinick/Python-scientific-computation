%module demo

%{
#define SWIG_FILE_WITH_INIT
#include "demo.h"
%}

%include "numpy.i"
%init %{
    import_array();
%}

void drange(double * ARGOUT_ARRAY1, int DIM1);
void rot2d(double ARGOUT_ARRAY2[3][3], double th);
double sum_power(double * IN_ARRAY1, int DIM1);
void power(double *INPLACE_ARRAY1, int DIM1);
