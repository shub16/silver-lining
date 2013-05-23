#include<stdio.h>
int RAND_MAX=6;
int main()
{
  int ar[13],i;
  for(i=1;i<13;i++)
    ar[i]=0;
  srandom(time(NULL));
  for(i=1;i<=1000;i++)
  {
    int a=random()%RAND_MAX;
    int b=random()%RAND_MAX;
    if(a==0)
	a=6;
    if(b==0)
	b=6;
    int c=a+b;
    ar[c]++;
  }
  for(i=2;i<13;i++)
    printf("The number of %ds : %d\n",i,ar[i]);
}
