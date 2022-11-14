#include <stdio.h>
void tr(char *ptr)
{
    for (int i=0;i<101;i++)
    {
        printf("%c",*(ptr+i));
    }
}

int main()
{
    char arr[100];
    scanf("%[^\n]s",&arr);
    tr(arr);
    return 0;
}