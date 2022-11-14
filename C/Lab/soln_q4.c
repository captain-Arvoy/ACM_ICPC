#include <stdio.h>
#include <math.h>
int main(){
	int b,c;
	printf("Enter b:");
	scanf("%d",&b);
	printf("Enter c:");
	scanf("%d",&c);
	float a =sqrt(pow(b,2) + pow(c,2)); 
	printf("side a = %f",a);
	return 0;
}
