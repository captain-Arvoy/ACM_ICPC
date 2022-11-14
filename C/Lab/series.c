#include <stdio.h>
int main(){
	int even = 5, odd = 10;
	int limit;
	printf("Enter your Limit: ");
	scanf("%d",&limit);
	printf("%d %d",odd,even);
	for (int i = 1; i <= limit; i++){

		if (i % 2 == 0){
			even+=10;
			printf(" %d ",even);
		}
		else {
			odd += 50;
			printf(" %d ",odd);
		}
	}
	printf("\n");
	return 0;
}
