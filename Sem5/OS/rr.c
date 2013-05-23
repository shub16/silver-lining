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
			printf("%d\t%f\t%f\n",temp->pid,temp->enter_time,temp->service_time);
			temp=temp->next;
		}
		printf("%d\t%f\t%f\n",temp->pid,temp->enter_time,temp->service_time);
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
//	printf("%s\n",n);
	if(!feof(fp))
	{
//		printf("hi\n");
//		fscanf(fp,"%s",n);
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
//		free(new);
	}
	else
		next_node=NULL;
	if(next_node!=NULL)
		printf("%f\n%f\n",next_node->enter_time,next_node->service_time);
	else 
		printf("next node is null!\n");
}
void rr()
{
	while(ready_queue!=NULL)
	{
		print();
		struct node *t=dequeue();
		struct node *temp;
		if(clk<t->enter_time)
			clk=t->enter_time;
		if(t->flag==0)
			waiting_time[t->pid]=(clk-t->enter_time);
		else
			waiting_time[t->pid]+=(clk-t->exit_time);
											printf("%f\t%d\t%f\t%f\n",clk,t->pid,t->enter_time,t->service_time);
		if(t->service_time<=quanta)
		{
			clk+=t->service_time;
			processor_time+=t->service_time;
				turn_around_time[t->pid]=(clk-t->enter_time);
			while(next_node!=NULL && clk>=next_node->enter_time)
			{
				printf("hi2\n");
				event();
			}
			if(ready_queue==NULL && next_node!=NULL)
				event();
			clk+=dispatch_overhead;
			printf("hi\t%f\n",clk);
		}
		else if(t->service_time>quanta)
		{
			clk+=quanta;
			processor_time+=quanta;
//				printf("hi1\t %f\n",clk);
			while(next_node!=NULL && clk>=next_node->enter_time)
			{
				printf("hi2\n");
				event();
			}
			temp=(struct node *)malloc(sizeof(struct node));
			temp->enter_time=t->enter_time;
			temp->service_time=(t->service_time)-quanta;
			temp->next=NULL;
			temp->flag=1;
			temp->exit_time=clk;
			temp->pid=t->pid;
			if(ready_queue==NULL)
				printf("EMPTY QUEUE!\n");
			enqueue(temp);
//			free(temp);
			clk+=dispatch_overhead;
				printf("hi1\t %f\t%f\n",clk,temp->service_time);
		}
	}
}
int main(int argc,char *argv[])
{
	printf("Enter the Dispatch overhead (in seconds):");
	scanf("%f",&dispatch_overhead);
	printf("Enter the Time Quanta (in seconds):");
	scanf("%f",&quanta);
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
//	printf("%d\n",et);
	new->enter_time=et;
	fscanf(fp,"%s",n);
	st=atof(n);
	new->service_time=st;
//	printf("%f",st);
	new->next=NULL;
	new->pid=i;
	new->flag=0;
	new->exit_time=0;
	waiting_time[i]=0;
	next_node=new;
	processor_time=next_node->enter_time;
//	free(new);
	i++;
	event();
	rr();
	fclose(fp);
	int a;
	for(a=0;a<i;a++)
	{
		total_waiting_time+=waiting_time[a];
		total_turn_time+=turn_around_time[a];
		printf("Waiting time for process %d is : %f\n",a,waiting_time[a]);
		printf("Turnaround time for process %d is : %f\n",a,turn_around_time[a]);
	}
	avg_waiting_time=total_waiting_time/i;
	avg_turn_time=total_turn_time/i;
	printf("Average Waiting time for %d processes is : %f\n",i,avg_waiting_time);
	printf("Average Turnaround time for %d processes is : %f\n",i,avg_turn_time);
	printf("Fraction/Percentage of time processor was busy is : %f\n",((processor_time/clk)*100));
}
