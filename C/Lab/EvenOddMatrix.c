#include <stdio.h>
int main (){
	int arr[3][4] = {{1,2,3,4},{5,6,7,8},{9,10,11,12}},i2 = 0, j2 = 0, flag = 0;
	/* printf("Enter number for 3x4 matrix : "); */
	
	/* for (int i = 0; i < 3; i++){ */
	/* 	for (int j = 0; j < 4; j++){ */
	/* 		scanf("%d",&arr[i][j]); */
	/* 	} */
	/* } */
	while (i2 < 4){
		while (j2 < 5){
			if (flag == 0){//odd block
				if (i2 == 3 && j2 == 4){
					printf("\n");
					flag = 1;
					i2 = 0, j2 = 0;
				}
				if (arr[i2][j2] % 2 != 0){
					printf("%d ",arr[i2][j2]);
				}
			} else {
				if (arr[i2][j2]%2 == 0){
					printf("%d ",arr[i2][j2]);
				}
			}
			j2++;
		}
			i2++;
	}
	return 0;
}


