# include <stdio.h>
# include <string.h>
void wait(int accelaration){
    int store = 0;
    for (int i = 0; i< 100000000-accelaration ; i++){
        store = store + i;
    } 
}

int main(){
    char response[3];
    char greeting[20],msg[90];
    char* msg_ptr = msg;
    char* greeting_ptr = greeting;
    strcpy(msg,"Ready to Resume JAVA, don't worry about pending works\nwith harinaam we can solve it :)!");
    strcpy(greeting,"Welcome back sir!\n");
    scanf("%[^\n]*c",response);
    int compare_string_result;
    compare_string_result=strcmp(response,"go");
    if (compare_string_result == 0){
        for (int i=0; i < strlen(greeting) ; i++){
            printf("%c",*(greeting_ptr+i));
            wait(300000);
        }
        for (int i=0; i < strlen(msg) ; i++){
            printf("%c",*(msg_ptr+i));
            wait(30000000);
        }
    }
}
