#include<stdio.h>
#include<math.h>
#define SPACE ' '
void placehold(char ch , int num);
int main()
{
 float y, x, z;

 printf("��һ��\n");
 printf("��һ��������\n");
 printf("������\n");
 printf("�������\n");
 printf("������֮����,������֮��ѩ\n");
 printf("\n\n\n");
 printf("��ʵ\n");
 printf("��һ�仰\n");
 printf("��һֱ�����˵:\n");

 for (double y = 2.5; y >= -1.6; y = y - 0.2)
 {
 for (double x = -3; x <= 4.8; x = x + 0.1)
 {
 (pow((x*x + y*y - 1), 3) <= 3.6*x*x*y*y*y
 || (x>-2.4 && x<-2.1 && y<1.5 && y>-1)
 || (((x<2.5 && x>2.2) || (x>3.4 && x<3.7)) && y>-1 && y<1.5)
 || (y>-1 && y<-0.6 && x<3.7 && x>2.2)) ? printf(" ") : printf("*");
 }

 printf("\n");
 }
 getchar();
}

void placehold(char ch,int num){
    int begin;
    for(begin=1;begin<=num;begin++){
        putchar(ch);
    }
}