#include <stdio.h>
int main(){
	int length,breadth,area,perimeter;
	printf("Enter the length of rectangle:" );
	scanf("%d",&length);
	printf("Enter breadth of the rectangle:" );
	scanf("%d",&breadth);
	area = length * breadth;
	perimeter = 2*(length + breadth);
	printf("The area of rectangle: %d",area);
	printf("\nThe perimeter of rectangle: %d",perimeter);
	return 0;
}
