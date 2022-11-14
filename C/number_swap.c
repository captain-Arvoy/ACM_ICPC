#include <stdio.h>
int main(){
	int a,b;
	printf("Enter the first number: ");
	scanf("%d",&a);
	
	printf("Enter the second number: ");
	scanf("%d",&b);
	printf("The original values are:\na: %d\nb: %d",a,b);
//	a = a + b;
	b = a + b;
	a = b - a;
	b = b - a;

	printf("\nThe interchanged values are:\na: %d\nb: %d\n",a,b);
}

