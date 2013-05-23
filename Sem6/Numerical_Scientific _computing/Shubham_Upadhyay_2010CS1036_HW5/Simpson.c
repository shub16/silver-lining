#include<stdio.h>
#include<math.h>
float integral1(float x, float y);
int main(){
    float b=2,a=1,d=2,c=1;
    float h=(b-a)/3.0,k=(d-c)/3.0;

    float sum=9.0*h*k*(integral1(a,c)+3*integral1(a,c+k)+3*integral1(a,c+2*k)+integral1(a,d)+3*(integral1(a+h,c)+3*integral1(a+h,c+k)+3*integral1(a+h,c+2*k)+integral1(a+h,d))+3*(integral1(a+2*h,c)+3*integral1(a+2*h,c+k)+3*integral1(a+2*h,c+2*k)+integral1(a+2*h,d))+(integral1(b,c)+3*integral1(b,c+k)+3*integral1(b,c+2*k)+integral1(b,d)))/64.0;
    printf(" The Solution of integration is %f\n",sum);
}
float integral1(float x, float y){
    return 1.0/(x+y);
}
