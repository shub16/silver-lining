#include<stdio.h>
#include<math.h>
double function(double x);
double mod(double  a);
double romberg(int x);
double trapezoidal(float a, float b, int m);
int main(){
	int i=1;
    int m=1;
    int max=1;
    int h=1;
    double a[100];
    int size=0;
    a[0]=romberg(0);
    int count=0;
    while(1){
        double p=romberg(h);
        double x = trapezoidal(a[count],p,count+1);
        a[count++]=p;
        while(count!=max){
            p=x;
            x=trapezoidal(a[count],p,count+1);
            a[count++]=p;
        }
        if(count==max){
            a[count]=x;
            if(mod(a[count]-a[count-1])<0.00000001){
                printf("The solution of integration is %0.9lf\n",a[count]);
                break;
            }
            max	++;
            h++;
            count=0;
        }
    }
    printf(" No of iteration needed is %0.0f\n",pow(2,h)+1);
}
double function(double x){
    return 1.0/(1+x*x*x);
}
double mod(double  a){
    if(a>0)
    return a;
    else
    return -a;
}
double romberg(int x){
    int i;
    int y=pow(2,x);
    double sum=function(0)+function(1);
    double z=1.0/y;
    for(i=1;i<=y-1;i++)
    {
        sum=sum + 2*function(z);
        z=z + 1.0/y;
    }
    return sum/(2*y);
}
double trapezoidal(float a, float b, int m){
    return (pow(4,m)*b - a)/(pow(4,m)-1);
}





