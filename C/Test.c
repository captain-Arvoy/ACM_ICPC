#include <stdio.h>
int main(int argc, char const *argv[])
{
    int a=256;
    int *p=&a;
    printf("%d",*p);
    return 0;
}
