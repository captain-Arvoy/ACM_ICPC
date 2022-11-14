#include <stdio.h>
int main()
{
    int choice;
    printf("Enter your position: ");
    scanf("%d",&choice);
    switch(choice)
    {
        case 1:
        printf("Congratulations! You won a Runner shield\n");
        break;
        case 2:
        printf("Congratulations! You won a Silver medal\n");
        break;
        case 3:
        printf("Congratulations! You won a bronze medal\n");
        break;
        default:
        printf("Good! No problem the competition isn't just about prizes.\n");
        break;
    }
    return 0;
}