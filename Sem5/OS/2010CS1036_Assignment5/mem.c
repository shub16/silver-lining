#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include "mymalloc.h"
#define MAX 1024*160   // 160 KB of memory

void *mp;
struct mem_space
{	
	int size;
	int used;
	struct mem_space* next;
	struct mem_space* prev;
	struct mem_space*next1;
	struct mem_space*prev1;
};
int size_ht;
struct mem_space** ht; 
struct mem_space* head; 
int test(struct mem_space* curr,int request)
{
	if(curr->size - request > sizeof(struct mem_space))
		return 1;	
	else
		return 0;
		
}
void init_ht()
{
	int i = 0;
	while(1)
	{
		ht[i] = NULL;
		i++;
		if(i>=size_ht)
			break;
	}
}
void add_ht(struct mem_space*curr)
{
	int hv = log2(curr->size);
	struct mem_space*node = ht[hv];
	if(node == NULL)
		ht[hv] = curr;
	else
	{
		curr->prev1 = node;
		node->next1 = curr;
		ht[hv] = curr;
	}
}
void rem_ht(struct mem_space*curr)
{
	int i = log2(curr->size);
	if(curr==NULL)
		printf("Invalid entry to be removed from hash table!\n");
	if(curr->prev1==NULL)
	{
		if(curr->next1!=NULL)
			curr->next1->prev1 =NULL;
		ht[i] = curr->next1;
	}
	else if(curr->prev1!=NULL)
	{
		curr->prev1->next1 = curr->next1;
		if(curr->next1!=NULL)
			curr->next1->prev1=curr->prev1;
	}
		
}
void initMemory(struct mem_space* curr)
{
	curr = (struct mem_space*)mp;
	curr->used =0;
	curr->next=NULL;
	curr->prev =NULL;
	curr->next1=NULL;
	curr->prev1 = NULL;
	curr->size = MAX-sizeof(struct mem_space);
	int i = log2(MAX-sizeof(struct mem_space));
	ht[i] = curr;
}
void MemInit()
{
	mp = malloc(MAX);
	size_ht = log2(MAX)+1;
	ht = (struct mem_space**)malloc(size_ht*sizeof(struct mem_space*));
	init_ht();
	initMemory(head);
	head = mp; 
}
void *MyMalloc(int bytes)
{
	struct mem_space* samp;
	int iter = log2(bytes);
	int i ; 
	for(i = iter;i<size_ht;i++)
	{
		samp=ht[i];
		if(samp == NULL)
		if(samp!=NULL)
		while(samp!=NULL && samp->size<bytes)
			samp=samp->next1;
		if(samp!=NULL)
			break;
	}
	if(i>=size_ht)
	{
		printf("Cannot allocate memory!!\n");
		return 0;
	}
	rem_ht(samp);
	struct mem_space* addr = samp+sizeof(struct mem_space);
	samp->used=1;
	if(test(samp,bytes))
	{
		struct mem_space *curr;
		curr=(struct mem_space*)(addr+bytes);
		curr->used=0;
		curr->size=samp->size-bytes-sizeof(struct mem_space);
		curr->next1=curr->prev1=NULL;
		struct mem_space *temp;
		temp=samp->next;
		if(samp->next!=NULL)
			samp->next->prev=curr;
		samp->next=curr;
		curr->next=temp;
		curr->prev=samp;
		samp->size=bytes;
	
		add_ht(curr);
	}
	struct mem_space*x1=addr-sizeof(struct mem_space);
	return addr;			 		
}
void MyFree(void *p)
{
	struct mem_space* i = (struct mem_space*)(p);
	i = i - sizeof(struct mem_space);
	i->used=0;
	if(i->next!=NULL&&i->next->used==0)
	{
		i->size = i->size+i->next->size+sizeof(struct mem_space);
		if(i->next->next!=NULL)
			i->next->next->prev=i;
		struct mem_space* samp = i->next;
		i->next=i->next->next;
		rem_ht(samp);		
	}
	if(i->prev!=NULL&&i->prev->used==0)	
	{
		rem_ht(i->prev);
		i->prev->next=i->next;
		if(i->next!=NULL)
			i->next->prev = i->prev;
		i->prev->size=i->prev->size+sizeof(struct mem_space)+i->size;
		i=i->prev;			
	}
	i->next1=NULL;
	i->prev1=NULL;
	add_ht(i);
}
