# include <stdio.h>  
void main()   
{   
	int n ;   
	float A[50][50], X[50] ;   
	scanf("%d", &n) ;   
	int i, j, k;   
	double s, p ;   
	for(i = 0 ; i < n ; i++)   
    {   
		for(j = 0 ; j < n ; j++)   
			scanf("%f", &A[i][j]) ;      
    } 
	for(i=0;i<n;i++)
	scanf("%f", &A[i][n]) ;  
    for(i = 0 ; i < n - 1 ; i++)   
    {   
		for(j = i + 1 ; j < n ; j++)   
		{   
			p = A[j][i] / A[i][i] ;   
			for(k = i ; k < n + 1 ; k++)   
				A[j][k] = A[j][k] - p * A[i][k] ;   
		}   
    }   
    X[n-1] = A[n-1][n] / A[n-1][n-1] ;   
    for(i = n - 2 ; i >= 0 ; i--)   
    {   
		s = 0 ;   
		for(j = i + 1 ; j < n ; j++)   
		{   
			s += (A[i][j] * X[j]) ;   
			X[i] = (A[i][n] - s) / A[i][i] ;   
		}   
    }
	printf("The Solution is :\n");   
    for(i = 0 ; i < n ; i++)   
		printf("\nx[%d] = %.4f", i + 1, X[i]) ; 
	printf("\n");  
}  
