#include<stdio.h>
long double fact(int n)
{
	if(n==0 || n==1)
		return 1;
	else 
		return n*fact(n-1);
}
int main()
{
	int n,i;
	scanf("%d",&n);
	int a[n];
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	for(i=0;i<n;i++)
	{
		printf("%0.0Lf\n",fact(a[i]));
	}
}
