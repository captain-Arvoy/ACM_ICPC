#include <stdio.h>
int coder(char message[]){
    int _bin_mssg_;
    printf("%s",message);
    for (int i = 0; i < length(message); i++){
        printf("%d ",message[i]);
    }
    return _bin_mssg_;
}
int main(){
    char mssg[100];
    printf("Enter your message: ");
    scanf("%[^\n]*c",mssg);
    coder(mssg);
}