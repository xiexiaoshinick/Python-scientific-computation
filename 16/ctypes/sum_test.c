double mysum(double a[], long n)
{
    double sum = 0;
    int i;
    for(i=0;i<n;i++) sum += a[i];
    return sum;
}

double mysum2(double a[], int strides[], int shapes[])
{
    double sum = 0;
    int i, j, M, N, S0, S1;
    M = shapes[0]; N=shapes[1];
    S0 = strides[0] / sizeof(double);
    S1 = strides[1] / sizeof(double);

    for(i=0;i<M;i++){
        for(j=0;j<N;j++){
            sum += a[i*S0 + j*S1];
        }
    }
    return sum;
}