#include <stdio.h> // header file for Standard Input Output
#include <stdlib.h> // header file for Standard Library
#include <math.h>
int main() {

    int A,B;
    scanf("%d",&A);
    
    scanf("%d",&B);
    if (pow(A,B) > pow(B,A)){
        printf("First");
    } else if (pow (A,B) < pow(B,A)){
        printf("Second");
    } else {
        printf("Equal");
    } 
    return 0;
}