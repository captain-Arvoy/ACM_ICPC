#include <stdio.h>
#include <stdlib.h>
int c ;
int *no_ptr;
int* req(int *ref_no_ptr)
{
    int *ref_no_ptr2 = (int *)realloc(ref_no_ptr, sizeof(int) * c);
    return ref_no_ptr2;
}
int push(int psh_ele, int *no_ptr)
{
    c++;
    no_ptr = req(no_ptr);
    *(no_ptr + (c - 1)) = psh_ele;
}
int bin(int t, int *ptr)
{
    if (t == 1)
    {
        return push(1, ptr);
    }
    return push(t % 2, ptr), bin((int)t / 2, ptr);
}
int main()
{
    int no;
    int arr[2];
    no_ptr = &arr[0];
    int *ptr = &arr[0];
    printf("Enter the number: ");
    scanf("%d", &no);
    bin(no, ptr);
    for (int i = 0; i < c; i++)
    {
        ptr = ptr + i;
        printf("%d ", *ptr);
    }
    printf("\n");
    return 0;
}