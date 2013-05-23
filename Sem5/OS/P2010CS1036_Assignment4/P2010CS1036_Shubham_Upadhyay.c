#include<stdio.h>
#include<stdlib.h>
#include<math.h>
float clk=0.0;
float dispatch_overhead,quanta;
FILE *fp;
float waiting_time[10000];
float turn_around_time[10000];
float processor_time=0;
int i=0; //contains number of processes
struct node
{
	int pid;
	int flag;
	float service_time;
	float enter_time;
	float exit_time;
	struct node *next;
};
struct node *next_node;
struct node *ready_queue=NULL;
struct node *last=NULL;
void enqueue(struct node *n)
{
	if(ready_queue==NULL && last==NULL)
	{
		ready_queue=n;
		last=n;
		n->next=ready_queue;
	}
	else 
	{
		last->next=n;
		last=last->next;
		n->next=ready_queue;
	}
}
void print()
{
	struct node *temp=ready_queue;
	if(temp==NULL)
		printf("The queue is empty!");
	else
	{
		while(temp!=last)
		{
			temp=temp->next;
		}
	}
}	
		
struct node* dequeue()
{
	struct node *temp=ready_queue;
	if(ready_queue->next!=ready_queue)
	{
		ready_queue=ready_queue->next;
		last->next=ready_queue;
	}
	else
	{
		ready_queue=NULL;
		last=NULL;
	}
	temp->next=NULL;
	return temp;
}
void event()
{
	char n[1000];
	struct node *new;
	if(next_node!=NULL)
		enqueue(next_node);
	else
		return;
	fscanf(fp,"%s",n);
	if(!feof(fp))
	{
		int *b,et,a=0;
		b=&a;
		new=(struct node*)malloc(sizeof(struct node));
		et=atof(n);
		new->enter_time=et;
		fscanf(fp,"%s",n);
		new->service_time=atof(n);
		new->next=NULL;
		new->flag=0;
		new->exit_time=0;
		new->pid=i;
		waiting_time[i]=0;
		i++;
		next_node=new;
	}
	else
		next_node=NULL;
}
void rr()
{
	while(ready_queue!=NULL)
	{
		struct node *t=dequeue();
		struct node *temp;
		if(clk<t->enter_time)
			clk=t->enter_time;
		if(t->flag==0)
			waiting_time[t->pid]=(clk-t->enter_time);
		else
			waiting_time[t->pid]+=(clk-t->exit_time);
		if(t->service_time<=quanta)
		{
			clk+=t->service_time;
			processor_time+=t->service_time;
			turn_around_time[t->pid]=(clk-t->enter_time);
			while(next_node!=NULL && clk>=next_node->enter_time)
			{
				event();
			}
			if(ready_queue==NULL && next_node!=NULL)
				event();
			clk+=dispatch_overhead;
		}
		else if(t->service_time>quanta)
		{
			clk+=quanta;
			processor_time+=quanta;
			while(next_node!=NULL && clk>=next_node->enter_time)
			{
				event();
			}
			temp=(struct node *)malloc(sizeof(struct node));
			temp->enter_time=t->enter_time;
			temp->service_time=(t->service_time)-quanta;
			temp->next=NULL;
			temp->flag=1;
			temp->exit_time=clk;
			temp->pid=t->pid;
			enqueue(temp);
			clk+=dispatch_overhead;
		}
	}
}
int main(int argc,char *argv[])
{
	float overhead[6]={0,0.005,0.010,0.015,0.020,0.025};
    float quanta1[4]={0.05,0.1,0.25,0.5};
    int p,q;
    for(p=0;p<4;p++)
    {
		for(q=0;q<6;q++)
		{
			processor_time=0;
			i=0;
			clk=0;
			ready_queue=NULL;
			last=NULL;
			printf("\nFor Quanta %f ms & Overhead %f ms\n",quanta1[p],overhead[q]);
			dispatch_overhead=overhead[q];
			quanta=quanta1[p];
			fp=fopen(argv[1],"r");
			struct node *new;
			char n[1000];
			fscanf(fp,"%s",n);
			int et;
			float st;
			float avg_waiting_time,avg_turn_time;
			float total_waiting_time=0,total_turn_time=0;
			new=(struct node *)malloc(sizeof(struct node));
			et=atof(n);
			new->enter_time=et;
			fscanf(fp,"%s",n);
			st=atof(n);
			new->service_time=st;
			new->next=NULL;
			new->pid=i;
			new->flag=0;
			new->exit_time=0;
			waiting_time[i]=0;
			next_node=new;
			processor_time=next_node->enter_time;
			i++;
			event();
			rr();
			fclose(fp);
			int a;
			for(a=0;a<i;a++)
			{
				total_waiting_time+=waiting_time[a];
				total_turn_time+=turn_around_time[a];
			}
			avg_waiting_time=total_waiting_time/i;
			avg_turn_time=total_turn_time/i;
			printf("Average Waiting time for %d processes is : %f\n",i,avg_waiting_time);
			printf("Average Turnaround time for %d processes is : %f\n",i,avg_turn_time);
			printf("Fraction/Percentage of time processor was busy is : %f\n",((processor_time/clk)*100));
		}
	}
}
