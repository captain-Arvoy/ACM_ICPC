//WAP to print the prime numbers between 1 to 50
#include <stdio.h>
#include <stdbool.h>
#include <math.h>
void printprime(){
	bool flag_for_j = true;
	for (int j = 1;  j <= 50;j++){
		flag_for_j = true;
		double squareroot = sqrt(j);
		for (int i = 2; i <= squareroot;i++){
			if (j%i == 0){
				flag_for_j = false;
				break;
			}
		}
		if (flag_for_j == true){
			printf("%d  ",j);
		}
	}
}
int main(){
	printprime();
	printf("\n");
}
