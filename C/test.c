
#include <stdio.h>


#define REGREAD(_DAYOFWEEK_)\
({\
	char* str;\
	switch (_DAYOFWEEK_){\
		case 1:\
		case 2:\
		case 3:\
		case 4:\
		case 5:\
			str = "小伙子，好好上班！";\
			break;\
		case 6:\
		case 7:\
			str = "小伙子，来加个班呀！";\
			break;\
		default:\
			str = "小伙子，今年过年别回家了,加个班吧！";\
	}\
	(str);\
})\

int main() {
	int i;
    char* str;
	for(i = 0; i <= 7; i++){
		str = REGREAD(i);
    	printf("%s\n", str);
	}
    return 0;
}
