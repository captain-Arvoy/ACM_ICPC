#include <stdio.h>
#include <math.h>
int main (){
	int b,a,c;
	double rootp,rootn;
	printf("Enter the coefficient of x (b): ");
	scanf("%d",&b);
	printf("Enter the coefficient  of x^2 (a): ");
	scanf("%d",&a);
	printf("Enter the constant c: ");
	scanf("%d",&c);
	if (pow(b,2)-(4*a*c) > 0){
		rootp = (-b+sqrt(pow(b,2)-(4*a*c)))/(2*a);
		rootn = (-b-sqrt(pow(b,2)-(4*a*c)))/(2*a);
	} else {
		printf("\nVirtual roots ");
	}
	return 0;
}
