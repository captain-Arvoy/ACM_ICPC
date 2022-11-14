#include <stdio.h>

void pattern(int n){
    // int no_of_columns = 2*n-1;
    //-----1st half box--------
    for (int i = n; i>=1; i--){
        for (int j =n; j>=1; j--){
            if (i>j){
                printf("%d ",i);
            }else{
                printf("%d ",j);
            }
        }
        for (int j2 = 2; j2 <= n; j2++){
            if (i>j2){
                printf("%d ",i);
            }else{
                printf("%d ",j2);
            }            
        }
    printf("\n");
    }
    //-----2nd half box--------
    for (int i2 = 2; i2 <= n; i2++){
        for (int j =n; j>=1; j--){
            if (i2>j){
                printf("%d ",i2);
            }else{
                printf("%d ",j);
            }
        }
        for (int j2 = 2; j2 <= n; j2++){
            if (i2>j2){
                printf("%d ",i2);
            }else{
                printf("%d ",j2);
            }            
        }        
        printf("\n");
    }
}
int main() 
{

    int n;
    printf("Enter the number: ");
    scanf("%d", &n);
    pattern(n);
      // Complete the code to print the pattern.
    
    return 0;
    
}