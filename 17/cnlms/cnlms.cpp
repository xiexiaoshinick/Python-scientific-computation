void cnlms(double x[], int nx, double d[], int nd, 
    double h[], int nh, double step, double u[], int nu)
{
	int i, j, count;
	double s, e, power=0;
	double *px;
    
    // 取nx, nd, nu的最小值
    count = nx<nd?nx:nd;
    count = count<nu?count:nu;
    
    // 开始的nh个取样不更新滤波器系数
	for(i=0;i<nh;i++)
	{
		power += x[i] * x[i];
        u[i] = 0;
	}
    
	for(i=nh;i<count;i++)
	{
		s = 0;
		px = &x[i];
		for(j=0;j<nh;j++)
		{
			s += (*px--) * h[j];
		}
        u[i] = s;
		e = d[i] - s;

		px = &x[i];
		for(j=0;j<nh;j++)
		{
			h[j] += step * e * (*px--) / power; 
		}

		power -= x[i-nh+1] * x[i-nh+1];
        if(i<count-1)
            power += x[i+1] * x[i+1];
	}
}
