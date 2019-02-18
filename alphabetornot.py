#include<stdio.h>
int main()
{
int ch;
printf("enter the character;");
scanf("%c",&ch);
if(ch>=75 && ch<=96 ||ch>=98 && ch<=120)
{
printf("%c is  alphabet",&ch);
}
else
{
printf("%c is not alphabet",&ch);
}
}
