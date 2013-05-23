#include<stdio.h>
#include<math.h>
#define SIZE     10

void main()
{
    int choice,n,i,j;
    float c[SIZE][SIZE+1];
    FILE *fp;
    void arrange_systeam(float c[SIZE][SIZE+1],int n);
    void basic_gauss_elimination(float c[SIZE][SIZE+1],int n,FILE *fp);
    void gauss_elimination_pivoting(float c[SIZE][SIZE+1],int n,FILE *fp);
    void gauss_jacobi(float c[SIZE][SIZE+1],int n,FILE *fp);
    void gauss_seidel(float c[SIZE][SIZE+1],int n,FILE *fp);
    fp = fopen("sysoflin.dat","w");

    printf("\nENTER NUMBER OF EQUATION =");
    fprintf(fp,"\nENTER NUMBER OF EQUATION =");
    scanf("%d",&n);
    fprintf(fp,"%d",n);

    for(i=0;i<n;i++)
    {
        for(j=0;j<n+1;j++)
        {
            printf("\nENTER COEFFICENT OF EQUATION-%d X[%d] =",i+1,j
+1);
            fprintf(fp,"\nENTER COEFFICENT OF EQUATION-%d X[%d] =",i
+1,j+1);
            scanf("%f",&c[i][j]);
            fprintf(fp,"%f",c[i][j]);
        }
    }

    while(1)
    {
        printf("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
        fprintf(fp,"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
        printf("\n\t\tMENU");
        fprintf(fp,"\n\t\tMENU");
        printf("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
        fprintf(fp,"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
        printf("\n1. BASIC GAUSS ELIMINATION METHOD");
        fprintf(fp,"\n1. BASIC GAUSS ELIMINATION METHOD");
        printf("\n2. GAUSS ELIMINATION WITH PIVOTING");
        fprintf(fp,"\n2. GAUSS ELIMINATION WITH PIVOTING");
        printf("\n3. GAUSS JACOBI METHOD");
        fprintf(fp,"\n3. GAUSS JACOBI METHOD");
        printf("\n4. GAUSS SEIDEL METHOD");
        fprintf(fp,"\n4. GAUSS SEIDEL METHOD");
        printf("\n5. QUIT");
        fprintf(fp,"\n5. QUIT");
        printf("\n\n ENTER YOUR CHOICE = ");
        fprintf(fp,"\n\n ENTER YOUR CHOICE = ");
        scanf("%d",&choice);
        fprintf(fp,"%d",choice);

        switch(choice)
        {
            case 1:
                basic_gauss_elimination(c,n,fp);
                break;
            case 2:
                gauss_elimination_pivoting(c,n,fp);
                break;
            case 3:
                gauss_jacobi(c,n,fp);
                break;
            case 4:
                gauss_seidel(c,n,fp);
                break;
            case 5:
                fclose(fp);
                exit(1);
            default:
                printf("\nENTER PROPER VALUE\n");
                fprintf(fp,"\nENTER PROPER VALUE\n");
        }
    }
}

void arrange_systeam(float c[SIZE][SIZE+1],int n)
{
    int i,j,p,q;
    float max,temp;

    for(i=0;i<n-1;i++)
    {
        max = fabs(c[i][i]);
        p = i;
        for(j=i+1;j<n;j++)
        {
            if(fabs(c[j][i]) > max)
            {
                max = c[j][i];
                p = j;
            }
        }
        if(p != i)
        {
            for(q=0;q<n+1;q++)
            {
                temp = c[i][q];
                c[i][q] = c[p][q];
                c[p][q] = temp;
            }
        }
    }
}
void basic_gauss_elimination(float c[SIZE][SIZE+1],int n,FILE *fp)
{
    int i,j,k;
    float temp,x[SIZE],sum;

    for(j=0;j<n-1;j++)
    {
        for(i=j+1;i<n;i++)
        {
            temp = c[i][j] / c[j][j];
            for(k=j;k<=n;k++)
            {
                c[i][k] = c[i][k] - (temp * c[j][k]);
            }
        }
    }

    x[n-1] = c[n-1][n] / c[n-1][n-1];

    for(i=n-2;i>=0;i--)
    {
        sum = 0;
        for(j=i+1;j<n;j++)
        {
            sum = sum + (c[i][j] * x[j]);
        }
        x[i] = (c[i][n] - sum)/c[i][i];
    }
    printf("\nSOLUTION OF GIVEN SYSTEM\n");
    fprintf(fp,"\nSOLUTION OF GIVEN SYSTEM\n");
    for(i=0;i<n;i++)
    {
        printf("\nx%d = %.3f ",i,x[i]);
        fprintf(fp,"\nx%d = %.3f ",i,x[i]);
    }
    printf("\n");
    fprintf(fp,"\n");
    

}

void gauss_elimination_pivoting(float c[SIZE][SIZE+1],int n,FILE *fp)
{
    int i,j,k,p,q,m;
    float temp,x[SIZE],sum,max;

    for(j=0;j<n-1;j++)
    {
        max = fabs(c[j][j]);
        p=j;
        for(m=j+1;m<n;m++)
        {
            if(fabs(c[m][j]) > max)
            {
                max = c[m][j];
                p = m;
            }
        }
        if(p != j)
        {
            for(q=j;q<n+1;q++)
            {
                temp = c[j][q];
                c[j][q] = c[p][q];
                c[p][q] = temp;
            }
        }
        for(i=j+1;i<n;i++)
        {
            temp = c[i][j] / c[j][j];
            for(k=j;k<=n;k++)
            {
                c[i][k] = c[i][k] - (temp * c[j][k]);
            }
        }
    }

    x[n-1] = c[n-1][n] / c[n-1][n-1];

    for(i=n-2;i>=0;i--)
    {
        sum = 0;
        for(j=i+1;j<n;j++)
        {
            sum = sum + (c[i][j] * x[j]);
        }
        x[i] = (c[i][n] - sum)/c[i][i];
    }
    printf("\nSOLUTION OF GIVEN SYSTEM\n");
    fprintf(fp,"\nSOLUTION OF GIVEN SYSTEM\n");
    for(i=0;i<n;i++)
    {
        printf("\nx%d = %.3f ",i,x[i]);
        fprintf(fp,"\nx%d = %.3f ",i,x[i]);
    }
    
    printf("\n");
    fprintf(fp,"\n");
}

void gauss_jacobi(float c[SIZE][SIZE+1],int n,FILE *fp)
{
    int i,j,p;
    float old_x[SIZE],new_x[SIZE],sum;
    float error,big_error,epsilon;

    printf("\nENTER PRESCRIBED TOLERANCE = ");
    fprintf(fp,"\nENTER PRESCRIBED TOLERANCE = ");
    scanf("%f",&epsilon);
    fprintf(fp,"%f",epsilon);

    /*     Arrange given systeam of linear equation    */


    arrange_systeam(c,n);

    /*    Initialize to all variable to zero    */
for(i=0;i<n;i++)
    {
        old_x[i] = 0;
    }

    printf("\n");
    fprintf(fp,"\n");

    /*    Find solution of given systeam        */


    p = 1;
    do
    {
        big_error = 0;
        printf("%d",p);
        fprintf(fp,"%d",p);
        p++;
        for(i=0;i<n;i++)
        {
            sum = 0;
            for(j=0;j<n;j++)
            {
                if(i != j)
                    sum = sum + (c[i][j] * old_x[j]);
            }
            new_x[i] = (c[i][n] - sum)/c[i][i];

            printf("  x%d = %.5f  ",i,new_x[i]);
            fprintf(fp,"  x%d = %.5f  ",i,new_x[i]);

            error = fabs(new_x[i] - old_x[i]);
            if(error > big_error)
            {
                big_error = error;
            }
        }
        printf("\n");
        fprintf(fp,"\n");
        for(i=0;i<n;i++)
        {
            old_x[i] = new_x[i];
        }
    }
    while(big_error >= epsilon);

    printf("\nSOLUTION OF GIVEN SYSTEAM\n");
    fprintf(fp,"\nSOLUTION OF GIVEN SYSTEAM\n");
    for(i=0;i<n;i++)
    {
        printf("\nx%d = %f",i,new_x[i]);
        fprintf(fp,"\nx%d = %f",i,new_x[i]);
    }
    printf("\n");
    fprintf(fp,"\n");

}

void gauss_seidel(float c[SIZE][SIZE+1],int n,FILE *fp)
{
    int i,j,p;
    float x[SIZE],temp,sum;
    float error,big_error,epsilon;

    printf("\nENTER PRESCRIBED TOLERANCE = ");
    fprintf(fp,"\nENTER PRESCRIBED TOLERANCE = ");
    scanf("%f",&epsilon);
    fprintf(fp,"%f",epsilon);

    /*     Arrange given systeam of linear equation    */


    arrange_systeam(c,n);

    /*     Initialize to all variable to zero    */
for(i=0;i<n;i++)
    {
        x[i] = 0;
    }

    printf("\n");
    fprintf(fp,"\n");

    /*    Find solution of given systeam        */

    p = 1;
    do
    {
        big_error = 0;
        printf("%d",p);
        fprintf(fp,"%d",p);
        p++;
        for(i=0;i<n;i++)
        {
            sum = 0;
            for(j=0;j<n;j++)
            {
                if(i != j)
                {
                    sum = sum + (c[i][j] * x[j]);
                }
            }
            temp = (c[i][n] - sum)/c[i][i];
            printf("   x%d = %.5f  ",i,temp);
            fprintf(fp,"   x%d = %.5f  ",i,temp);
            error = fabs(temp - x[i]);
            x[i] = temp;

            if(error > big_error)
            {
                big_error = error;
            }
        }
        printf("\n");
        fprintf(fp,"\n");
    }
    while(big_error >= epsilon);

    printf("\nSOLUTION OF GIVEN SYSTEAM\n");
    fprintf(fp,"\nSOLUTION OF GIVEN SYSTEAM\n");
    for(i=0;i<n;i++)
    {
        printf("\nx%d = %f",i,x[i]);
        fprintf(fp,"\nx%d = %f",i,x[i]);
    }
    printf("\n");
    fprintf(fp,"\n");
  
}
