#include <stdio.h>
int main(){
    char in,temp;
    char loop = 'y';
    while(loop == 'y'){
        printf("-->");
        scanf("%c",&in);
        printf(": %d",(int)in);
        scanf("%c",&temp);
        printf("\nnext?[y/n] ");
        scanf("%c",&loop);
        scanf("%c",&temp);
        printf("\n");
    }
    return 0;
}
