#include <stdio.h>
#include <string.h>

struct student
{
    char name[20];
    int  age;
    char gend;
}Ard,arvoy,kris;


int main()
{
    strcpy(Ard.name,"Aditya Roshan Dash");
    strcpy(arvoy.name,"Captain Arvoy");
    strcpy(kris.name,"Radha-Raman");
    Ard.age=18;
    arvoy.age=21;
    kris.age=1000;
    Ard.gend='M';
    arvoy.gend='M';
    kris.gend='M';
    printf("Ard's details are:\n%s %d %c\n\n",Ard.name,Ard.age,Ard.gend);
    printf("arvoy's details are:\n%s %d %c\n\n",arvoy.name,arvoy.age,arvoy.gend);
    printf("kris's details are:\n%s %d %c\n",kris.name,kris.age,kris.gend);
    return 0;
}