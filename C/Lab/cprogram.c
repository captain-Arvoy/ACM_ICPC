#include<stdio.h>
int main(){
		char val = 260;

		int ans;
		ans = val + !val + ~val + ++val;
		printf("%d",val);
		return 0;
}
