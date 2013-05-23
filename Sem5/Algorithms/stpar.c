#include<stdio.h>
#include<time.h>
#include<unistd.h>
#include<math.h>
int main()
{
	long double n;
	scanf("%Lf",&n);
	n=n*4000000007;
	n=sqrt(n);
	time_t t=n;
	printf("%s",ctime(&t));
}
