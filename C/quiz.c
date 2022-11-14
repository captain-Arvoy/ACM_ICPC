#include <stdio.h>
int main()
{
    int a;
    printf("Enter the number for the following options:\n1.passed Maths and science\n2.passed Maths\n3.passed Science\n");    
    scanf("%d",&a);
    if(a==1)
    {
        printf("You are getting gift worth Rupees 45!");
    }
    else if(a==1||a==2){
        printf("You are getting prize of worth Rupees 15");
    }
    else{
        printf("Sorry you have to pass atleast one exam to be eligible for the prize!");
    }
    return 0;
}