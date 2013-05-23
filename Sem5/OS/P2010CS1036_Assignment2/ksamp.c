#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>
#include<unistd.h>
 void convert_time(int x)
 {
	 int sec,min,hour;
	 hour=x/3600;
	 min=x/60- (hour *60);
	 sec=x-((min*60) + (hour*3600));
	 printf("%d hours %d minutes %d seconds\n",hour,min,sec);
 }
int convert(char *text)
{
   int i, value;
   for (i = 0, value = 0; text [ i ] != '\0'; ++i)
   {
      value *= 10;
      value += text [ i ] - '0';
   }
   return value;
}
void first()
{
	int *b;
	FILE *fp,*gp;
	char *c,n[1000],*v;
	int p,i=0;
	printf("Kernel Version : ");
	c="/proc/version";
	fp = fopen(c,"r");
	fscanf(fp,"%s",n);
	while(i!=2)
	{
		fscanf(fp,"%s",n);
		i++;
	}
	printf("%s\n",n);
	fclose(fp);
	c="/proc/cpuinfo";
	printf("Processor Type : \n");
	fp = fopen(c,"r");
	while(fgets(n, 1000 , fp) != NULL)
	{
		if(strstr(n,"processor")||strstr(n,"model name")||strstr(n,"cpu MHz")||strstr(n,"cache size"))
			printf("%s",n);
	}
	fclose(fp);
    c="/proc/stat";
	fp = fopen(c, "r");
	int t;
	fscanf(fp,"%s",n);
	while(strcmp(n,"btime")!=0)
		fscanf(fp,"%s",n);
	fscanf(fp,"%s",n);
	t=((time(NULL))-convert(n));
	printf("Time since last boot in seconds : %d\n",t);
	fclose(fp);
}
void second()
{
	int *p,*b;
	FILE *fp;
	char *c,n[10000],*v,ch;
	c="/proc/diskstats";
	fp = fopen(c,"r");
	int count=1;
	fscanf(fp,"%s",n);
	while(strcmp(n,"sda")!=0)
		fscanf(fp,"%s",n);
	fscanf(fp,"%s",n);
	printf("Number of Disk Reads : %s\n",n);
	while(count!=5)
	{
		fscanf(fp,"%s",n);
		count++;
	}
	printf("Number of Disk Writes : %s\n",n);
	fclose(fp);
	c="/proc/stat";
	fp = fopen(c, "r");
	fscanf(fp,"%s",n);
	while(strcmp(n,"cpu") != 0)
		fscanf(fp,"%s",n);
	fscanf(fp,"%s",n);
	printf("Time spent by processor in user mode : ");
	convert_time(atoi(n)/sysconf(_SC_CLK_TCK));
	fscanf(fp,"%s",n);
	printf("Time spent by processor in nice mode : ");
	convert_time(atoi(n)/sysconf(_SC_CLK_TCK));
	fscanf(fp,"%s",n);
	printf("Time spent by processor in kernel mode : ");
	convert_time(atoi(n)/sysconf(_SC_CLK_TCK));
	fscanf(fp,"%s",n);
	printf("Time spent by processor is idle : ");
	convert_time(atoi(n)/sysconf(_SC_CLK_TCK));
	fscanf(fp,"%s",n);
	while(strcmp(n,"ctxt")!=0)
		fscanf(fp,"%s",n);
	fscanf(fp,"%s",n);
	printf("Number of context swiches the kernel has performed : %s\n",n);
	fscanf(fp,"%s",n);
	while(strcmp(n,"btime")!=0)
		fscanf(fp,"%s",n);
	fscanf(fp,"%s",n);
	time_t ti;
	ti=convert(n);
	printf("Time at which system was last booted : %s",ctime(&ti));
	fscanf(fp,"%s",n);
	while(strcmp(n,"processes")!=0)
		fscanf(fp,"%s",n);
	fscanf(fp,"%s",n);
	printf("Number of processes created since the last boot up: %s\n",n);
	fclose(fp);	
}
void third(int samp,int obs)
{
	int *b;
	FILE *fp;
	char *c,n[10000],*v;
	c="/proc/meminfo";
	fp = fopen(c, "r");
	fscanf(fp,"%s",n);
	while(strcmp(n,"MemTotal:")!=0)
		fscanf(fp,"%s",n);
	fscanf(fp,"%s",n);
	printf("Amount of memory configured into this computer (in kb) : %s\n",n);
	fscanf(fp,"%s",n);
	while(strcmp(n,"MemFree:")!=0)
		fscanf(fp,"%s",n);
	fscanf(fp,"%s",n);
	printf("Amount of memory currently free (in kb): %s\n",n);
	fclose(fp);
	int i=0;
	c="/proc/loadavg";
	while(i<obs)
	{
		int d=0;
		fp = fopen(c, "r");
		fscanf(fp,"%s",n);
		printf("Load Average averaged over last 1 minute after %d seconds: %s\n",i+2,n);
		sleep(samp);	
		i+=samp;
		fclose(fp);
	}
}
int main (int argc,char *argv[])
{
	char *c;
	int samp;
	int obs;
	if(argc==1)
		first();
	else if(argc==2 && !strcmp(argv[1],"-s"))
	{
		first();
		second();
	}
	else if(argc==4 && !strcmp(argv[1],"-l"))
	{
		samp=convert(argv[2]);
		obs=convert(argv[3]);
		first();
		second();
		third(samp,obs);
	}
	else
	{
		printf("Wrong command line input!!\n");
	}
}
