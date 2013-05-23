#include<iostream>
using namespace std;
#include<string.h>
#include<stdlib.h>
#include<stdio.h>
#include<ctype.h>


void decrypt_text(char pass[], char b[])		//decrypts the text based on the password
{
int len, size;
len = strlen(b);
size = strlen(pass);
int i = 0;
int j = 0;
char temp;
for(i = 0; i < len; i++)
{
	temp = b[i];
	b[i] = 65 + b[i] - pass[j];
	if(b[i] < 65)
		b[i] = 91 - (65-b[i]);
	j = (j+1)%size;
}
cout<<"The decrypted text\n";
cout<<b<<"\n";

}

void find_pass(char b[], int res)		//password is found based on cryptanalysis
{
char key[26];
int count[26];
int i = 0;
int j = 0;
int max = 0;
int ans;
int length;
int iter = 0;
length = strlen(b);
int x =  0;
for(x = 0; x < 26; x++)
{
		count[x] = 0;
		key[x] = 0;
}
for(i = 0;i < res; i++)
{
	max = 0;
	ans = 9;
	for(x = 0; x < 26; x++)
	{
		count[x] = 0;
	}
	j = i;
	while(j < length-1)
	{
		count[b[j]-65]++;
		j = j + res;
	}
	for(x = 0; x < 26; x++)
	{
		if(max < count[x])
		{
			max = count[x];
			ans = 65 + x;
		}
	}
	if(ans >= 'E')
	{
		key[iter++] = ans - 4;
	}
	else
	if(ans < 'E')
	{
		key[iter++] = 65 + (91 - ans) + 4;
	}

}
key[iter] = '\0';
cout<<"The key is "<<key<<"\n";
decrypt_text(key,b);
}

void crypto(char a[], char b[])//text is encrypted
{
int length;
length = strlen(b);
int count[10];
int i = 0;
int j = 0;
int k = 0;
for(i = 0; i < 10; i++)
{
	count[i] = 0;
}
for(i = 1; i < 10; i++)
{
	for(j = 0; j < length-i; j++)
	{
		if(b[j] == b[j+i])
			count[i]++;
	}	
}

int max = 0;
int res = 0;
for(i = 1; i < 10; i++)
{
	if(count[i] > max)
	{
		max = count[i];
		res = i;
	}
}
cout<<"The key length is ";
cout<<res<<"\n";
find_pass(b, res);
}

int main()
{
char key[10];					// contains the password
char a[1000000];
char b[1000000];
cin>>key;
char c;
int length;
int i = 0;
int shift;
char new_char;
int k1 = 0;
int k2 = 0;
length = strlen(key);
fflush(stdin);
c = getchar();
while((c = getchar()) != EOF)		//text is being encrypted
{
	if(isalpha(c))
	{
	shift = key[i];
	a[k1++] = toupper(c);
	new_char = (shift + toupper(c) - 65);
	if(new_char > (65+26))
	{
		new_char = 65 + (new_char-(91));
	}
	i= (i+1)%length;	
	b[k2++] = new_char;	
	}	
}
a[k1] = '\0';
b[k2]= '\0';
cout<<"The encrypted text is \n";
cout<<b<<"\n";
crypto(a,b);
}
