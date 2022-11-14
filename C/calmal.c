#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n = 5;
    char *ptr;
    char *ptrz;
    ptr = (char *)calloc(n, sizeof(char *));
    ptrz=
    if (ptr == NULL){
        printf("Memory not allocated!");
        return 1;
    }
    for (int i = 0; i < 5; i++)
    {
        
        ptrz = (char *)calloc(20, sizeof(char));

    }
    for (int i=0; i < 5; i++){
        for (int j=0; j<2 ; j++){
            printf("Enter name: ");
            scanf("%[^\n]c", &(ptr[i]));
        }
    }
    printf("Input done\n");
    for (int j = 0; j < 5; j++)
    {
        printf("Printing %d value of array: ",j+1);
        printf("%s\n", ptr[j]);
    }
    return 0;
}