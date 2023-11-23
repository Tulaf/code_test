#include <stdio.h>
#include <stdlib.h>

/* test */
#define TEST(p)                     \
do{                                 \
    if(p!=NULL)                     \
    {                               \
        free(p);                    \
        printf("free success!\n");  \
    }                               \
    p=NULL;                         \
}while(0)
 
/* Get the highest bit of data */
#define HIGHEST_BIT_POSITION(num) \
({\
	typeof(num) _num = (num); \
	typeof(num) _highest_bit_position = 0;	\
	while (_num != 1) { \
		_highest_bit_position++; \
		_num >>= 1; \
	} \
	(_highest_bit_position);\
})\


int main()
{
    int *p=NULL;
    p=(int*)malloc(sizeof(int));
	unsigned int num = 0x8000;

    TEST(p);
    printf("---------done!---------%d\n", HIGHEST_BIT_POSITION(num));
	return 0;
}
