#include <stdio.h>
int avg(int arr[2][2])
{
    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            printf("The value at arr[%d][%d] =%d\n", i, j, arr[i][j]);
        }
    }
}
int main(int argc, char const *argv[])
{
    // int arr[]={1,2,3,4,5};
    // avg(arr);
    // printf("arr=%x\n",arr);
    int arr2[][2] = {{1, 2}, {3, 4}};
    avg(arr2);
    return 0;
}
