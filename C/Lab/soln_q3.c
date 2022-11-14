#include <stdio.h>
#include <math.h>
int main(){
	float principal,rate,no_terms,time_period;
	printf("Enter the principal: ");
	scanf("%f",&principal);
	printf("Enter the rate of interest: ");
	scanf("%f",&rate);
	printf("Enter terms: ");
	scanf("%f",&no_terms);
	printf("Enter time period: ");
	scanf("%f",&time_period);	
	double term1 =(1+rate/no_terms);
	double term2 = no_terms*time_period;
	double amount =principal*pow(term1,term2);
	printf("The amount = %lf\n",amount);
	return 0;
}
