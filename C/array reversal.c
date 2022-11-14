#include <stdio.h>

void arr_rev(int *arr_p, int le)
{

    int t, le2 = (int)le / 2;
    for (int i = 0; i < le2; i++)
    {
        int inx = le - 1 - i;
        t = *(arr_p + i);
        *(arr_p + i) = *(arr_p + inx);
        *(arr_p + inx) = t;
    }
}

int main()
{
    int le;
    printf("Enter the size of array: ");
    scanf("%d", &le);
    int arr[le];
    printf("Enter array:\n");
    for (int i = 0; i < le; i++)
    {
        scanf("%d", &arr[i]);
    }
    printf("Successful!\n");
    //------------------------------------------output----------------------------------------------------------------------
    printf("Array of your input:\n{");
    for (int i = 0; i < le; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("}\n");
    //------------------------------------------output----------------------------------------------------------------------
    arr_rev(arr, le);
    //------------------------------------------output----------------------------------------------------------------------
    printf("Reversed array:\n{");
    for (int i = 0; i < le; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("}\n");
    //------------------------------------------output----------------------------------------------------------------------
    return 0;
}