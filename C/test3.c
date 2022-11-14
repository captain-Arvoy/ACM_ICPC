#include<stdio.h>

int main()
{
    int math;
    int phy;
    int che;
    int bio;
    int eng;

    printf("enter math mark : ");
    scanf( "%d"  ,&math);

    printf("\nenter phy mark : ");
    scanf("%d"  ,&phy);

    printf("\nenter che mark : ");
    scanf("%d"  ,&che);

    printf("\nenter bio mark : ");
    scanf("%d" ,&bio);

    printf("\nenter eng mark : ");
    scanf("%d"  ,&eng);

    float total=math+phy+che+bio+eng;

    printf("total marks : %f", total );
   

    double percentage= (total/500) * 100;

    printf("\npercentage : %lf\n", percentage);
    return 0;
    
    




}