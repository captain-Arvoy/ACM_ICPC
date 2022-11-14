#include <stdio.h>
int main()
{
    for (int i = 1; i <= 7; i++)
    {
        int inner_it = 1;
        for (int j = 4; j >= 1; j--)
        {
            printf("%d ", j);
            if (inner_it == i)
            {
                printf("\n");
                break;
            }
            inner_it++;
        }
    }
    return 0;
}
