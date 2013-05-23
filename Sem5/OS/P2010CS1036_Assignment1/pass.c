#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
int main()
{
	char c[100];
	char ch;
	int len=0,i,upper=0,lower=0,digit=0;
	printf("Enter the password: ");
    while((ch=getchar())!='\n')
    {
        c[len++]=ch;
    }
	i=0;
	while(i<len)
	{
		if(isupper(c[i]))
		  upper++;
		if(islower(c[i]))
		  lower++;
		if(isdigit(c[i]))
		  digit++;
		i++;
	}
	if(lower>=2 && upper>=2 && digit>=2)
		printf("This is a safe password!\n");
	else
		printf("This is not a safe password!\n");
}
