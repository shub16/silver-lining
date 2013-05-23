#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include "mymalloc.h"

int main(int argc, char *argv[])
{
	MemInit();
	int size;
	void *ptr[10];
	int i;
	int MAX_MEMORY_SIZE = 1024;
	/*
	 * try mallocing four pieces, each 1/4 of total size
	 */
	size = MAX_MEMORY_SIZE / 4;

	ptr[0] = MyMalloc(size);
	if(ptr[0] == NULL)
	{
		printf("malloc of ptr[0] failed for size %d\n",
				size);
		exit(1);
	}

	PrintMyMallocFreeList();
	printf("\n");

	ptr[1] = MyMalloc(size);
	if(ptr[1] == NULL)
	{
		printf("malloc of ptr[1] failed for size %d\n",
				size);
		exit(1);
	}

	PrintMyMallocFreeList();
	printf("\n");

	ptr[2] = MyMalloc(size);
	if(ptr[2] == NULL)
	{
		printf("malloc of ptr[2] failed for size %d\n",
				size);
		exit(1);
	}

	PrintMyMallocFreeList();
	printf("\n");

	/*
	 * this one should fail due to rounding
	 */
	ptr[3] = MyMalloc(size);
	if(ptr[3] == NULL)
	{
		printf("malloc of ptr[3] fails correctly for size %d\n",
				size);
	}

	PrintMyMallocFreeList();
	printf("\n");

	/*
	 * free the first block
	 */
	MyFree(ptr[0]);

	PrintMyMallocFreeList();
	printf("\n");

	/*
	 * free the third block
	 */
	MyFree(ptr[2]);

	PrintMyMallocFreeList();
	printf("\n");


	/*
	 * now free secoond block
	 */
	MyFree(ptr[1]);

	PrintMyMallocFreeList();
	printf("\n");

	/*
	 * re-malloc first pointer
	 */
	ptr[0] = MyMalloc(size);
	if(ptr[0] == NULL)
	{
		printf("re-malloc of ptr[0] failed for size %d\n",
				size);
		exit(1);
	}
	PrintMyMallocFreeList();
	printf("\n");

	/*
	 * try splitting the second block
	 */
	ptr[1] = MyMalloc(size/2);
	if(ptr[1] == NULL)
	{
		printf("split second block ptr[1] failed for size %d\n",
				size/2);
		exit(1);
	}
	PrintMyMallocFreeList();
	printf("\n");

	/*
	 * free first block and split of second
	 */
	MyFree(ptr[0]);
	MyFree(ptr[1]);

	PrintMyMallocFreeList();
	printf("\n");


	/*
	 * try mallocing a little less to make sure no split occurs
	 * first block from previous print should not be split
	 */
	ptr[0] = MyMalloc(size-1);
	if(ptr[0] == NULL)
	{
		printf("slightly smaller malloc of ptr[0] failed for size %d\n",
				size);
		exit(1);
	}

	/*
	 * free it and make sure it comes back as the correct size
	 */
	MyFree(ptr[0]);
	
	PrintMyMallocFreeList();
	printf("\n");

	/*
	 * okay, now see if multiples work
	 */
	for(i=0; i < 6; i++)
	{
		ptr[i] = MyMalloc(100);
	}

	/*
	 * free first block, third block, fifth block
	 */
	MyFree(ptr[0]);
	MyFree(ptr[2]);
	MyFree(ptr[4]);
	PrintMyMallocFreeList();
	printf("\n");

	/*
	 * now, free second block -- first, second, third blocks
	 * should coalesce
	 */
	MyFree(ptr[1]);
	PrintMyMallocFreeList();
	printf("\n");

	/*
	 * free the sixth block and it shoudl merge with the last
	 * block leaving two
	 */
	MyFree(ptr[5]);
	PrintMyMallocFreeList();
	printf("\n");

	/*
	 * now free fourth block and they should all be together
	 */
	MyFree(ptr[3]);
	PrintMyMallocFreeList();
	printf("\n");

	printf("made it -- passed test\n");

	exit(0);


}

	

