#include<stdio.h>
#include<math.h>
int n;
void product(float a[][n], float b[][n])
{
	int i, j, k;
	float p[n][n];
	for(i = 0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			float temp = 0;
			for( k = 0; k < n ; k++ )
            temp = temp + a[i][k]*b[k][j];
			p[i][j] = temp;
		}
	}
	for( i = 0; i<n; i++ )
		for( j = 0; j<n; j++ )
			 b[i][j] = p[i][j];
}
float mod(float x)
{
    if(x<0)
		return -x;
	else
		return x;
}
int main()
{
    scanf("%d",&n);
    float mat1[n][n];
    float b[n][n];
    int i,j,k,l;
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            b[i][j]=0;
            if(i==j)
            mat1[i][j]=1;
            scanf("%f",&mat1[i][j]);
        }
    }
    float sum;
    sum=0;
    for(k=2;k<n;k++)
        for(l=0;l<=k-2;l++)
            sum=sum+2*mat1[k][l];
    int flag=0;
    while(flag==0)
    {
		for(i=1;i<n-1;i++)
		{
            for(j=i+1;j<n ;j++)
            {
				float theta=atan(mat1[i-1][j]/mat1[i-1][i]);
                float c=cos(theta);
                float s=sin(theta);
                for(k=0;k<n;k++)
                {
					for(l=0;l<n;l++)
					{
						b[k][l]=0;
                        if(k==l)
							b[k][l]=1;
                    }
                }
				b[j][j]=c;
                b[i][j]=s;
                b[i][i]=c;
                b[j][i]=-s;
                product(b,mat1);
                b[j][j]=c;
                b[i][j]=-s;
                b[i][i]=c;
                b[j][i]=s;
                product(mat1,b);
                for(k=0;k<n;k++)
					for(l=0;l<n;l++)
						mat1[k][l]=b[k][l];
            }
		}
		flag=1;
		for(i=2;i<n;i++)
			for(j=0;j<=i-2;j++)
				if(mod(mat1[i][j])>0.00000001)
					flag=0;
    }
    for(i=0;i<n;i++)
    {
		for(j=0;j<n;j++)
			printf("%.4f   ",mat1[i][j]);
        printf("\n");
    }
}
