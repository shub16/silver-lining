#include<sys/time.h>
#include<signal.h>
#include<unistd.h>
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
long unsigned int fibonacci(unsigned int n);
static void p_sig_handler(int);
static void c1_sig_handler(int);
static void c2_sig_handler(int);
long unsigned int elapsed_usecs(long, long);
long unsigned int delta_time(struct itimerval, struct itimerval);
long unsigned int elapsed_usecs(long sec, long usec)
{
	return( sec * 1000 + usec);
}
long unsigned int delta_time(struct itimerval a,struct itimerval b) 
{
	    long p_usec = a.it_value.tv_sec;
	    long r_usec = b.it_value.tv_sec;
		return abs(p_usec - r_usec);
}
static long p_realt_secs=0,c1_realt_secs=0,c2_realt_secs=0;
static long p_virtt_secs=0,c1_virtt_secs=0,c2_virtt_secs=0;
static long p_proft_secs=0,c1_proft_secs=0,c2_proft_secs=0;
static struct itimerval p_realt,c1_realt,c2_realt;
static struct itimerval p_virtt,c1_virtt,c2_virtt;
static struct itimerval p_proft,c1_proft,c2_proft;
int main(int argc,char **argv)
{
	long unsigned fib=0;
	int pid1,pid2;
	unsigned int fibarg;
	int status;
	fibarg=atoi(argv[1]);
	p_realt.it_interval.tv_sec=1;
	p_realt.it_interval.tv_usec=0;
	p_realt.it_value.tv_sec=1;
	p_realt.it_value.tv_usec=0;
	c1_realt.it_interval.tv_sec=1;
	c1_realt.it_interval.tv_usec=0;
	c1_realt.it_value.tv_sec=1;
	c1_realt.it_value.tv_usec=0;
	c2_realt.it_interval.tv_sec=1;
	c2_realt.it_interval.tv_usec=0;
	c2_realt.it_value.tv_sec=1;
	c2_realt.it_value.tv_usec=0;
	p_virtt.it_interval.tv_sec=1;
	p_virtt.it_interval.tv_usec=0;
	p_virtt.it_value.tv_sec=1;
	p_virtt.it_value.tv_usec=0;
	c1_virtt.it_interval.tv_sec=1;
	c1_virtt.it_interval.tv_usec=0;
	c1_virtt.it_value.tv_sec=1;
	c1_virtt.it_value.tv_usec=0;
	c2_virtt.it_interval.tv_sec=1;
	c2_virtt.it_interval.tv_usec=0;
	c2_virtt.it_value.tv_sec=1;
	c2_virtt.it_value.tv_usec=0;
	p_proft.it_interval.tv_sec=1;
	p_proft.it_interval.tv_usec=0;
	p_proft.it_value.tv_sec=1;
	p_proft.it_value.tv_usec=0;
	c1_proft.it_interval.tv_sec=1;
	c1_proft.it_interval.tv_usec=0;
	c1_proft.it_value.tv_sec=1;
	c1_proft.it_value.tv_usec=0;
	c2_proft.it_interval.tv_sec=1;
	c2_proft.it_interval.tv_usec=0;
	c2_proft.it_value.tv_sec=1;
	c2_proft.it_value.tv_usec=0;
	signal(SIGALRM,p_sig_handler);
	signal(SIGVTALRM,p_sig_handler);
	signal(SIGPROF,p_sig_handler);
	if(setitimer(ITIMER_REAL,&p_realt,NULL)==-1)
		perror("parent real timer set error");
	if(setitimer(ITIMER_VIRTUAL,&p_virtt,NULL)==-1)
		perror("parent virtual timer set error");
	if(setitimer(ITIMER_PROF,&p_proft,NULL)==-1)
		perror("parent profile timer set error");
	pid1=fork();
	if(pid1==0)
	{
		signal(SIGALRM,c1_sig_handler);
		signal(SIGVTALRM,c1_sig_handler);
		signal(SIGPROF,c1_sig_handler);
		if(setitimer(ITIMER_REAL,&c1_realt,NULL)==-1)
			perror("child1 real timer set error");
		if(setitimer(ITIMER_VIRTUAL,&c1_virtt,NULL)==-1)
			perror("child1 virtual timer set error");
		if(setitimer(ITIMER_PROF,&c1_proft,NULL)==-1)
			perror("child1 profile timer set error");
		fib=fibonacci(fibarg);
		getitimer(ITIMER_REAL,&c1_realt);
		getitimer(ITIMER_VIRTUAL,&c1_virtt);
		getitimer(ITIMER_PROF,&c1_proft);
		printf("\n");
		long u=elapsed_usecs(c1_realt.it_value.tv_sec,c1_realt.it_value.tv_usec)/1000;
		printf("Child 1 fib = %ld, real time = %ldsecs, %ldmsecs\n",fib,c1_realt_secs,u);
		u=elapsed_usecs(c1_proft.it_value.tv_sec,c1_proft.it_value.tv_usec)/1000;
		printf("Child 1 fib = %ld, cpu time = %ldsecs, %ldmsecs\n",fib,c1_proft_secs,u);
		u=elapsed_usecs(c1_virtt.it_value.tv_sec,c1_virtt.it_value.tv_usec)/1000;
		printf("Child 1 fib = %ld, user time = %ldsecs, %ldmsecs\n",fib,c1_virtt_secs,u);
		u=abs((elapsed_usecs(c1_proft.it_value.tv_sec,c1_proft.it_value.tv_usec)/1000)-(elapsed_usecs(c1_virtt.it_value.tv_sec,c1_virtt.it_value.tv_usec)/1000));
		long v=delta_time(c1_proft,c1_virtt);
		printf("Child 1 fib = %ld, kernel time = %ldsecs, %ldmsecs\n",fib,v,u);
		fflush(stdout);
		exit(0);
	}
	else
	{
		pid2=fork();
		if(pid2==0)
		{
			signal(SIGALRM,c2_sig_handler);
			signal(SIGVTALRM,c2_sig_handler);
			signal(SIGPROF,c2_sig_handler);
			if(setitimer(ITIMER_REAL,&c2_realt,NULL)==-1)
				perror("child1 real timer set error");
			if(setitimer(ITIMER_VIRTUAL,&c2_virtt,NULL)==-1)
				perror("child1 virtual timer set error");
			if(setitimer(ITIMER_PROF,&c2_proft,NULL)==-1)
				perror("child1 profile timer set error");
			fib=fibonacci(fibarg);
			getitimer(ITIMER_REAL,&c2_realt);
			getitimer(ITIMER_VIRTUAL,&c2_virtt);
			getitimer(ITIMER_PROF,&c2_proft);
			printf("\n");
			long u=elapsed_usecs(c2_realt.it_value.tv_sec,c2_realt.it_value.tv_usec)/1000;
			printf("Child 2 fib = %ld, real time = %ldsecs, %ldmsecs\n",fib,c2_realt_secs,u);
			u=elapsed_usecs(c2_proft.it_value.tv_sec,c2_proft.it_value.tv_usec)/1000;
			printf("Child 2 fib = %ld, cpu time = %ldsecs, %ldmsecs\n",fib,c2_proft_secs,u);
			u=elapsed_usecs(c2_virtt.it_value.tv_sec,c2_virtt.it_value.tv_usec)/1000;
			printf("Child 2 fib = %ld, user time = %ldsecs, %ldmsecs\n",fib,c2_virtt_secs,u);
			u=abs((elapsed_usecs(c2_proft.it_value.tv_sec,c2_proft.it_value.tv_usec)/1000)-(elapsed_usecs(c2_virtt.it_value.tv_sec,c2_virtt.it_value.tv_usec)/1000));
			long v=delta_time(c2_proft,c2_virtt);
			printf("Child 2 fib = %ld, kernel time = %ldsecs, %ldmsecs\n",fib,v,u);
			fflush(stdout);
			exit(0);
		}
		else
		{
			fib=fibonacci(fibarg);
			waitpid(0,&status,0);
			waitpid(0,&status,0);
			getitimer(ITIMER_REAL,&p_realt);
			getitimer(ITIMER_VIRTUAL,&p_virtt);
			getitimer(ITIMER_PROF,&p_proft);
			printf("\n");
			long u=elapsed_usecs(p_realt.it_value.tv_sec,p_realt.it_value.tv_usec)/1000;
			printf("Parent fib = %ld, real time = %ldsecs, %ldmsecs\n",fib,p_realt_secs,u);
			u=elapsed_usecs(p_proft.it_value.tv_sec,p_proft.it_value.tv_usec)/1000;
			printf("Parent fib = %ld, cpu time = %ldsecs, %ldmsecs\n",fib,p_proft_secs,u);
			u=elapsed_usecs(p_virtt.it_value.tv_sec,p_virtt.it_value.tv_usec)/1000;
			printf("Parent fib = %ld, user time = %ldsecs, %ldmsecs\n",fib,p_virtt_secs,u);
			u=abs((elapsed_usecs(p_proft.it_value.tv_sec,p_proft.it_value.tv_usec)/1000)-(elapsed_usecs(p_virtt.it_value.tv_sec,p_virtt.it_value.tv_usec)/1000));
			long v=delta_time(p_proft,p_virtt);
			printf("Parent fib = %ld, kernel time = %ldsecs, %ldmsecs\n",fib,v,u);
			fflush(stdout);
			exit(0);
		}
		printf("this line should never be printed\n");
	}
}
long unsigned int fibonacci(unsigned int n)
{
	if(n==0)
		return 0;
	else if(n==1 || n==2)
		return 1;
	else 
		return (fibonacci(n-1)+fibonacci(n-2));
}
static void p_sig_handler(int signo)
{
	switch(signo)
	{
		case SIGALRM:
			p_realt_secs+=1;
			break;
		case SIGVTALRM:
			p_virtt_secs+=1;
			break;
		case SIGPROF:
			p_proft_secs+=1;
			break;
		default:
		break;
	}
	return;
}
static void c1_sig_handler(int signo)
{
	switch(signo)
	{
		case SIGALRM:
			c1_realt_secs+=1;
			break;
		case SIGVTALRM:
			c1_virtt_secs+=1;
			break;
		case SIGPROF:
			c1_proft_secs+=1;
			break;
		default:
		break;
	}
	return;
}
static void c2_sig_handler(int signo)
{
	switch(signo)
	{
		case SIGALRM:
			c2_realt_secs+=1;
			break;
		case SIGVTALRM:
			c2_virtt_secs+=1;
			break;
		case SIGPROF:
			c2_proft_secs+=1;
			break;
		default:
		break;
	}
	return;
}
