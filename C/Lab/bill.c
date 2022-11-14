#include <stdio.h>
int main(){
	int unit;
	float amount = 0.0f;
	printf("Enter the unit: ");
	scanf("%d",&unit);
	if (unit < 200){
		amount += unit*1.20;
	} else if ( unit < 400){
		amount += unit * 1.5;
	} else if (unit < 600){
		amount += unit * 1.8;
	} else{
		amount += unit * 2.00;
	}
	if (amount > 400){
		amount = 0.15 * (amount - 400) + amount;
	} else if (amount < 100){
		amount = 100;
	}
	printf("Total amount: %f",amount);
}
	
