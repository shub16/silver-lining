#include<stdio.h>
void fib()
{
   int i,a=1,b=1,c;
   printf("The first 20 numbers in the Fibonacci sequence :\n");
   for (i=0;i<20;i++)
   {
      if(i<=1)
      c=1;
      else
      {
		c=a+b;
		a=b;
		b=c;
      }
      printf("%d\n",c);
   }
}
int main()
{
	fib();
}
