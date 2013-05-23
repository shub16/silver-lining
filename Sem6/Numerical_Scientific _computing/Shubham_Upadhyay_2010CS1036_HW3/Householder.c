#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#define MAX 100
void merge(double a[],int left,int mid,int right);
void sort(double a[],int left,int right);
void product(double matrix1[][MAX],double matrix2[][MAX],int n);
void print(double matrix[][MAX],int n);
void eigen(double a[][MAX],int n);
void householder(double a[][MAX], int n)
{
	int i, j, k, l;
	int flag=0;
	double b[MAX][MAX];
    while(flag==0)
    {
		for(i=1;i<n;i++)
		{
            for(j=i+1;j<=n ;j++)
            {
				float theta;
                if((a[i][i]-a[j][j])!=0)
					theta=(atan(2*a[i][j]/(a[i][i]-a[j][j])))/2;
                else
                {
					if(a[i][j]>0)
                        theta=3.14159265/4;
                    else
                        theta=-3.14159265/4;
                }
				float c=cos(theta);
                float s=sin(theta);
				for(k=1;k<=n;k++)
				{
					for(l=1;l<=n;l++)
					{
						b[k][l]=0;
                        if(k==l)
                            b[k][l]=1;
                    }
                }
				b[i][i]=c;
                b[j][i]=-s;
                b[j][j]=c;
                b[i][j]=s;
                product(b,a, n);
                b[i][j]=-s;
                b[i][i]=c;
                b[j][i]=s;
                b[j][j]=c;
				product(a,b, n);
				for(k=1;k<=n;k++)
					for(l=1;l<=n;l++)
						a[k][l]=b[k][l];
            }
		}
		flag=1;
		for(i=1;i<n;i++)
			for(j=i+1;j<=n;j++)
				if(a[i][j]>0.00001)
				{
					flag=0;
					break;
				}
    }	
}
void main()
{
    double sum,s,c,r;
	int i,j,k,n;        
    scanf("%d",&n);
    double w[MAX], v[MAX], q[MAX];
    double tridiagonal[MAX][MAX]; 
    tridiagonal[0][0]=1.0;
    for (i = 1;i<=n;i++)
        for (j=1;j<=n;j++)
            scanf("%lf",&tridiagonal[i][j]);
    for (k=1;k<=n-2;k++)
    {
		sum = 0;
		for (j = k+1; j <= n; j++) 
			sum += tridiagonal[j][k] * tridiagonal[j][k];
		s=sqrt(sum);
		if ( tridiagonal[k+1][k] < 0 ) 
			s=-s;
		r = sqrt( 2.0 * tridiagonal[k+1][k] * s + 2.0 * s * s );
		for (j = 1; j <= k; j++) 
			w[j] = 0.0;
		w[k+1] = ( tridiagonal[k+1][k] + s ) / r;
		for (j=k+2;j<=n;j++) 
			w[j] = tridiagonal[j][k] / r;
		for (i=1;i<=k;i++) 
			v[i] = 0.0;
		for (i = k+1; i <= n; i++) 
		{
			sum = 0.0;
			for (j = k+1; j <= n; j++) 
				sum += tridiagonal[i][j] * w[j];
			v[i] = sum;
		}            
		c = 0;
		for (j = k+1; j <= n; j++) 
			c += w[j] * v[j];
		for (j = 1; j <= k; j++)   
			q[j] = 0.0;
		for (j = k+1; j <= n; j++) 
			q[j] = v[j] - c * w[j];
		for (j=k+2;j<=n;j++) 
			tridiagonal[j][k] = tridiagonal[k][j] = 0.0;
		tridiagonal[k+1][k] = tridiagonal[k][k+1] = -s;
		for (j = k; j <= n; j++) 
			tridiagonal[j][j] -= 4.0 * q[j] * w[j];
		for (i = k+1; i <= n; i++) 
		{
			for (j = i+1; j <= n; j++) 
			{
				tridiagonal[i][j] = tridiagonal[i][j] - 2.0 * w[i] * q[j] - 2.0 * q[i] * w[j];
				tridiagonal[j][i] = tridiagonal[i][j];
			}
		}
    } 
   print(tridiagonal, n);
   householder(tridiagonal,n);
   eigen(tridiagonal,n);
}
void merge(double a[],int left,int mid,int right)
{
    double temp[right-left+2];
    int i=left,j=mid+1,k=0;
    while((i<=mid)&&(j<=right))
    {
        if(a[i]<=a[j])
			temp[k++]=a[i++];
        else
			temp[k++]=a[j++];
    }
    while(i<=mid)
		temp[k++]=a[i++];
    while(j<=right)
		temp[k++]=a[j++];
    for(i=0;i<k;i++)
		a[left+i]=temp[i];
}
void sort(double a[],int left,int right)
{
    int mid;
    if(left>=right)
		return;
    else
    {
        mid=(left+right)/2;
        sort(a,left,mid);
        sort(a,mid+1,right);
        merge(a,left,mid,right);
    }
}
void product(double matrix1[][MAX],double matrix2[][MAX],int n)
{
	int i, j, k;
	double matrix[MAX][MAX];
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=n;j++)
		{
			float temp = 0;
			for(k=1;k<=n;k++)
				temp=temp + matrix1[i][k]*matrix2[k][j];
			matrix[i][j] = temp;
		}
	}
	for( i = 1; i<=n; i++ )
		for( j = 1; j<=n; j++ )
			 matrix2[i][j] = matrix[i][j];
}
void print(double matrix[][MAX],int n )
{
	int i, j;
	for(i = 1;i<=n;i++)
	{
		for(j=1;j<=n;j++)
			printf("%lf ", matrix[j][i] );
		printf("\n");
	}
}
void eigen(double a[][MAX],int n)
{
	int i;
	double ans[MAX];
   	for(i=0;i<n;i++)
        	ans[i]=a[i+1][i+1];
    sort(ans,0,n-1);
    for(i=n-1;i>=0;i--)
        printf("%.4f\n",ans[i]);
}
