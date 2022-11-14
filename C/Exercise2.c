#include <stdio.h>
/*
*kms to miles
*inches to foot
*cms to inches
*pound to kgs
*inches to meters
*/
int main()
{
        int inp;
        float op1=0.621371;
        float op2=0.08333;
        float op3=0.393701;
        float op4=0.453592;
        float op5=0.0254;

    char ch;
    while(8)
    {
    printf("\n\nEnter your choice for the following:-\n1.Convert Kms to miles\n2.Convert inches to foot\n3.Convert cms to inches\n4.Convert pound to Kgs\n5.Convert inches to meters\n Type \"q\" to exit\n");
    scanf("%c",&ch);
    switch(ch)
    {
        case 'q':
            printf("Thank you for using our service!...");
            goto end;
            break;
        case '1':
            printf("Enter Kms: ");
            scanf("%f",&inp);
            printf("Quantity in miles= %0.4f",inp*op1);
            break;
        case '2':
            printf("Enter quantity in inches:- ");
            scanf("%f",&inp);
            printf("Quantity in foot= %0.4f",inp*op2);
            break;
        case '3':
            printf("Enter the quantity in cms= ");
            scanf("%f",&inp);
            printf("Quantity in inches= %0.4f",inp*op3);
            break;
        case '4':
            printf("Enter the quantity in pound= ");
            scanf("%f",&inp);
            printf("Quantity in Kgs= %0.4f",inp*op4);
            break;
        case '5':
            printf("Enter the quantity in inches= ");
            scanf("%f",&inp);
            printf("Quantity in meters= %0.2f",inp*op5);
            break;
        default:
            printf("Invalid choice!");
            break;
    }
    }   
    end:
        return 0; 
}
//yeh 2nd run mein invalid choice bolta hai