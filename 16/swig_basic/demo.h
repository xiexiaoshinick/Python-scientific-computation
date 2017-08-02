extern double global_test;
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

void add_mult(double x, double y, double * s, double *p);

double add(double *x, double *y);

void inc(int *x);

double sum_func(double (*op)(double), int s, int e);

double square(double x);
double reciprocal(double x);
double linear(double x);

class Sum
{
    public:
    double Cal(int s, int e)
    {
        double sum = 0;
        for(int i=s;i<e;i++)
            sum += Func(i);
        return sum;
    }
    virtual double Func(double x){return x;}
};

