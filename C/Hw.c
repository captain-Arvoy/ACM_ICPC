#include <stdio.h>
struct driver
{
    char name[100];
    char drv_lic_no[100];
    char route[100];
    int kms;
}array[3];
int main()
{
    char a;
    for (int i=0;i<3;i++)
    {   
        printf("---------------------------\nEnter the name: ");
        scanf("%[^\n]*c",&array[i].name);
        scanf("%c",&a);//For emptying buffer memory #buffer
        printf("\nEnter the driving license no.: ");
        scanf("%[^\n]*c",&array[i].drv_lic_no);
        scanf("%c",&a);//For emptying buffer memory #buffer
        printf("\nEnter the route: ");
        scanf("%[^\n]*c",&array[i].route);
        scanf("%c",&a);//For emptying buffer memory #buffer
        printf("\nEnter the distance travelled: ");
        scanf("%d",&array[i].kms);
        scanf("%c",&a);//For emptying buffer memory #buffer
    }
    for (int i=0;i<3;i++)
    {
        printf("-------------\nDetails of %s are:\nname:- %s",array[i].name,array[i].name);
        printf("\nDriving license number of %s is:%s",array[i].name,array[i].drv_lic_no);
        printf("\nRoute travelled by %s is:- ",array[i].name,array[i].route);
        printf("\nDistance travelled by %s is %d\n",array[i].name,array[i].kms);
    }
    return 0;
}