#include<stdio.h>
int main()
{
    int n,i,k,j,s;
    float A[50][50],L[50][50],U[50][50],X[50],b[50];
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
        for(j=1;j<=n;j++)
            scanf("%f",&A[i][j]);
    }
    for(i=1;i<=n;i++)
        scanf("%f",&b[i]);
    float sum,z[50];
    for(k=1;k<=n;k++)
    {
        U[k][k]=1;
        for(i=k;i<=n;i++)
        {
            sum=0;
            for(s=1;s<=k-1;s++)
                sum+=L[i][s]*U[s][k];
            L[i][k]=A[i][k]-sum;
        }

        for(j=k+1;j<=n;j++)
        {
            sum=0;
            for(s=1;s<=k-1;s++)
                sum+=L[k][s]*U[s][j];
            U[k][j]=(A[k][j]-sum)/L[k][k];
        }
    }
    for(i=1;i<=n;i++)
    {                                        //forward subtitution method
        sum=0;
        for(s=1;s<i;s++)
        sum+=L[i][s]*z[s];
        z[i]=(b[i]-sum)/L[i][i];
    }
    for(i=n;i>0;i--)
    {
        sum=0;
        for(s=n;s>i;s--)
            sum+=U[i][s]*X[s];
        X[i]=(z[i]-sum)/U[i][i];
    }
	printf("The Solution is :\n");
    for(i=1;i<=n;i++)
        printf("\nx[%d] = %.4f", i + 1, X[i]);
    printf("\n");
}


