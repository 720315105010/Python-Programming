#include<stdio.h>
int main()
{
int a;
printf("Enter the number");
scanf("%d",&a);
if(a<0)
{
printf("number is positive");
}
elseif(a>0)
{
printf("number is negative");
}
else
{
printf("number is zero");
}
}
