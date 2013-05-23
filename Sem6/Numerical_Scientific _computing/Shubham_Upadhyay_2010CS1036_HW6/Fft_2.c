#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#define PI	3.14159265358979323846264338327
double function( double t );
void fft1(double d[], int n2, int i_sign);
double* samp( int k );
int main(int argc, char * argv[])
{
	int i;
	int Nx;
	int NFFT;
	double *x;
	double *X;
	int k = 6;
	x = samp(k);
	Nx = pow(2,k);;
	NFFT = (int)pow(2.0, ceil(log((double)Nx)/log(2.0)));
	X = (double *) malloc((2*NFFT+1) * sizeof(double));
	for(i=0; i<Nx; i++)
	{
		X[2*i+1] = x[i];
		X[2*i+2] = 0.0;
	}
	printf("\nInput sequence:\n");
	for(i=0; i<NFFT; i++)
	{
		printf("x[%d] = (%.2f + j %.2f)\n", i, X[2*i+1], X[2*i+2]);
	}
	fft1(X, NFFT, 1);
	printf("\nFFT:\n");
	for(i=0; i<NFFT; i++)
	{
		printf("X[%d] = (%.2f + j %.2f)\n", i, X[2*i+1], X[2*i+2]);
	}
}
double* samp( int k )
{
	int n = pow(2,k);
	int i;
	double *v;
	v = (double*)malloc(n* sizeof(double));
	for( i = 0; i < n; i++ )
		v[i] = function(i);
	return v;	
} 
double function( double t )
{
//	double f=pow(t,2);
	return exp(-pow(t,2))*((sin(0.3*t) + cos(0.5*t))); 
}	
void fft1(double d[], int n2, int i_sign)
{
    double tmp, r, pr, pi, wi, theta;
    double tmpr, tmpi;
	int n, max, m, j, step, i;   
    n = n2 << 1;
    j = 1;
    for (i = 1; i < n; i += 2) {
	if (j > i) {
	    tmpr = d[j];     d[j] = d[i];     d[i] = tmpr;
	    tmpr = d[j+1]; d[j+1] = d[i+1]; d[i+1] = tmpr;
	}
	m = n >> 1;
	while (m >= 2 && j > m) {
	    j -= m;
	    m >>= 1;
	}
	j += m;
    }
    max = 2;
    while (n > max) {
	step = 2*max;
	theta = (2.0*PI)/(i_sign*max);
	tmp = sin(0.5*theta);
	pr = -2.0*tmp*tmp;
	pi = sin(theta);
	r = 1.0;
	wi = 0.0;
	for (m = 1; m < max; m += 2) {
	    for (i = m; i <= n; i += step) {
		j =i + max;
		tmpr = r*d[j]   - wi*d[j+1];
		tmpi = r*d[j+1] + wi*d[j];
		d[j]   = d[i]   - tmpr;
		d[j+1] = d[i+1] - tmpi;
		d[i] += tmpr;
		d[i+1] += tmpi;
	    }
	    r = (tmp = r)*pr - wi*pi + r;
	    wi = wi*pr + tmp*pi + wi;
	}
	max = step;
    }
}
