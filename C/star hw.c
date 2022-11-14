#include <stdio.h>
void patt(int rws, int ch)
{

    switch (ch)
    {
    case 1:
        for (int i = 0; i < rws; i++)
        {
            for (int j = 0; j <= i; j++)
            {
                printf("*");
            }
            printf("\n");
        }
        break;

    case 2:
        for (int i = rws; i >= 0; i--)
        {
            for (int j = 0; j <= i; j++)
            {
                printf("*");
            }
            printf("\n");
        }
        break;
    default:
        printf("Invalid choice");
        break;
    }
}
int main()
{
    int cho, row;
    printf("Enter the choice:\n1.Triangular star pattern\n2.Reversed star pattern\n");
    scanf("%d", &cho);
    printf("How many number of rows you want to print: ");
    scanf("%d", &row);
    patt(row, cho);
    return 0;
}