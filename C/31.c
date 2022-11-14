#include <stdio.h>
void assign(int * a1,int * b1)
{
    int a2,b2;
    a2=*a1+*b1;
    b2=*a1-*b1;
    *a1=a2;
    *b1=b2;
}
int main()
{
    int a,b;
    printf("Enter the value:");
    scanf("%d%d",&a,&b);
    assign(&a,&b);
    printf("a=%d\nb=%d",a,b);
    return 0;
}