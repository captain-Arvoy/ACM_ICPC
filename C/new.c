/*wap to input the minutes and print in hour and minutes*/
#include <stdio.h>
int main(){
    int time_inp, hour, minutes;
    printf("Enter the time: ");
    scanf("%d",&time_inp);
    hour = time_inp / 60;
    minutes = time_inp - 60*hour;
    printf("The time is:\n%d hrs %d mins\n",hour,minutes); 
    return 0;
}