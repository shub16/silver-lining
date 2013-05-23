#include<stdio.h>
int main()
{
  int sq[1001],i,j,k,d;
  for(i=1;i<1001;i++)
    sq[i]=i*i;
  for(j=1;j<10001;j++)
    for(i=j;i<1001;i++)
    {
		d=0;
		for(k=i;k<1001 && d!=1;k++)
			if(sq[j]+sq[i]==sq[k])
			{
				d++;
				printf("The triplet are : \n %d , %d, %d. \n",j,i,k);
			}
	}
}
