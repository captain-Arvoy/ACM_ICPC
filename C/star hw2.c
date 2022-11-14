#include <stdio.h>
int main()
{
    int ch;
    printf("Enter the choice:\n1.Triangular star pattern\n2.Reversed star pattern");
    scanf("%d",&ch);
    switch(ch)
    {
        case 1:
        for (int i=0;i<5;i++)
        {
            for (int j=0;j<=i;j++)
            {
                printf("*");
            }
        }
        break;

        case 2:
        for (int i=5; i>=0; i--)
        {
            for (int j=0;j<=i;j--)
            {
                printf("*");
            }
        }
        break;
        default:
        printf("Invalid choice");
        break;
    }
    return 0;
}