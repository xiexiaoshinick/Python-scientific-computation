%module nlms_swig
%{
#define SWIG_FILE_WITH_INIT
#include "cnlms.h"
%}
%include "numpy.i"
%init %{
    import_array();
%}

void cnlms(
    double * IN_ARRAY1, int DIM1,  // x
    double * IN_ARRAY1, int DIM1,  // d
    double * INPLACE_ARRAY1, int DIM1, // h
    double step,
    double * ARGOUT_ARRAY1, int DIM1 // u
);

%pythoncode %{
def nlms(x, d, h, step):
    n = min(len(x), len(d))
    return _nlms_swig.cnlms(x, d, h, step, n)
%}