#include <stdio.h>
#include<stdlib.h>

double gtime=0;
double turnaround=0;
double wait=0;
double jobcount=0;
double tfree=0;

struct node
{
    double arrivalt;
    double timereq;
    double ttime;
    struct node *next;
    
};

struct node *HEAD;
struct node *dtail;
struct node *dcurr;
struct node *lproc;
struct node *ptail;
int back=0;

void Dispatch()
{
  if(dcurr!=NULL)
  { 
    if(lproc==NULL)
        {
            tfree=tfree-gtime+dcurr->arrivalt;
            gtime=dcurr->arrivalt;
            struct node *temp=malloc (sizeof *temp);
            temp->arrivalt=dcurr->arrivalt;
            temp->timereq=dcurr->timereq;
            temp->ttime=dcurr->ttime;
            temp->next=NULL;
            dcurr=dcurr->next;
            lproc=temp;
            ptail=temp;
        }    
    else
        {
           while((dcurr!=NULL)&&(dcurr->arrivalt<gtime))
           {
                struct node *temp=malloc (sizeof *temp);
                temp->arrivalt=dcurr->arrivalt;
                temp->timereq=dcurr->timereq;
                temp->ttime=dcurr->ttime;
                temp->next=NULL;
                dcurr=dcurr->next;
                ptail->next=temp;   
                ptail=temp;
           }
        }
    }
}

void Step(double quanta, double overhead)
{
      if(lproc==NULL)
      {
            return;
      }
      if(back==1)
        {
                  struct node * temp= lproc->next;
                  ptail->next=lproc;
                  lproc->next=NULL;
                  ptail=lproc;
                  lproc=temp; 
                  back=0;
        }
        if(lproc->timereq-quanta<=0)
                {
                    gtime=gtime+lproc->timereq;
                    turnaround=turnaround+(gtime-lproc->arrivalt);
                    wait=wait+(gtime-lproc->arrivalt-lproc->ttime);
                    if(lproc->next!=NULL)
                    {
                        gtime=gtime+overhead;
                        struct node * temp= lproc->next;
                        free(lproc);
                        lproc=temp;
                        return;
                    }
                    if(lproc->next==NULL)
                    {
                        free(lproc);
                        lproc=NULL;
                        ptail=NULL;
                        return;    
                    }
                }
            else if(lproc->timereq-quanta>0)
                {
                    gtime=gtime+quanta;
                     lproc->timereq=lproc->timereq-quanta;
                    
                    if(lproc->next==NULL)
                    {
                        back=0;    
                    }
                    else
                    {
                        gtime=gtime+overhead;     
                        back=1;
                    }
                }       
}

void main(int argc, char *argv[])
{
         
         double overhead[6]={0,0.005,0.010,0.015,0.020,0.025};
         double quanta[4]={0.05,0.1,0.25,0.5};
         if (argc<2)
            {
                printf("Please supply input file\n") ;
                exit(0);
            }
         FILE *fp ;
         fp=fopen(argv[1],"r");
         if( fp == NULL )
            {
                printf("Cannot open input file\n") ;
                exit(0);
            }
         double a,b;
         int flg=0;
         while(fscanf(fp,"%lf",&a)!=EOF)
            {
                if(flg==0)
                {
                struct node *temp=malloc (sizeof *temp);;
                temp->arrivalt=a;
                fscanf(fp,"%lf",&b);
                temp->timereq=b;
                temp->ttime=b;
                dtail=temp;
                dcurr=temp;
                HEAD=dcurr;
                dtail->next=NULL;
                flg=1;
                lproc=NULL;
                ptail=NULL;
                jobcount++;
                }
                else
                {
                struct node * temp=malloc (sizeof *temp);;
                temp->arrivalt=a;
                fscanf(fp,"%lf",&b);
                temp->timereq=b;
                temp->ttime=b;
                dtail->next=temp;
                dtail=temp;
                dtail->next=NULL;
                jobcount++;
                }
               
            }         
//---------------------------------------------------------------------------------------------------------------------------------------------          
          int i=0;
          int j=0;
          while (i<4)
            {
                while(j<6)
                    {
                        dcurr=HEAD;
                        turnaround=0;
                        wait=0;
                        gtime=0;
                        tfree=0;
                          while(dcurr!=NULL)
                          {
                                Dispatch();
                                Step(quanta[i],overhead[j]);
                          }

                          while(lproc!=NULL)
                          {
                                Step(quanta[i],overhead[j]);
                          }
                          turnaround=turnaround/jobcount;
                          wait=wait/jobcount;
                          tfree=((gtime-tfree)/gtime)*100;
                          printf("\nFor Quanta %lf ms & Overhead %lf ms\n",quanta[i],overhead[j]);
                          printf("Average turnaround time : %lf\n",turnaround);
                          printf("Average waiting time : %lf\n",wait);
                          printf("Processor busy percentage : %lf\n",tfree);
                          j++;
                    }
                    i++;
                    j=0;
            }
}
