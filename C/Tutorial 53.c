#include <stdio.h>
int main()
{
    int a = 34;
    int *ptr = NULL;//((void *)0) ko type cast kar deta hai
    if (ptr!=NULL){
        printf("The address of a is %d\n",*ptr);
    }
    else{
        printf("The Null pointer can't be deferenced %d");
    }
}