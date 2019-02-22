##include<stdio.h>
#
#int cmp(int * a, int *b){
#	return *a>*b;
#}
#
#int (**compar)(const void *, const void *);
#
##define SIZE 0x100
#int main(int argc, char*argv[]){
#	int nums[SIZE];
#	int (*cmp_p)(const void *, const void *) = cmp;
#	int i;
#	char * p;
#	int bit_pos;
#
#	compar = &cmp_p;
#
#	for (i=0;i<SIZE;i++)
#		read(0,nums+i, sizeof(*nums));
#	
#	fscanf(stdin,"POINTER=%d\n", (int*) &p);
#	fscanf(stdin,"BIT=%d\n", &bit_pos);
#	bit_pos %= 8;
#
#	*(char*)p ^= 1<<bit_pos;
#
#	qsort(nums, SIZE, sizeof(*nums), *compar);
#
#	for (i=0;i<SIZE;i++)
#		printf("%d\n",nums[i]);
#return 0;
#}

with open('./12-challenge.win','wb') as win:
	win.write()
