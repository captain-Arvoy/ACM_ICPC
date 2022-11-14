#include <stdio.h>
int main(){
	int a,b;
	printf("Enter two numbers: ");
	scanf("%d",&a);
	scanf("%d",&b);
	printf ("\na = %d\n b = %d\n",a,b);
	a = a+b;
	b = a - b;
	a = a - b;
	printf("a = %d\n b = %d\n",a,b);
	return 0;
}
