// Revise Successful YUHUUUUU :D !!!
import java.util.Scanner;
public class Revise{
	public static void main(String args[]){
		Scanner sc = new Scanner (System.in);
		Operations ob = new Operations();
//		System.out.println("Enter the size of a
//		int size = sc.nextInt();
		int input_arr [] = {1,-2,6,-1,3};
		int prefix_arr[] = new int[input_arr.length];
		ob.printEmpty(prefix_arr);
		ob.gen_prefix(input_arr, prefix_arr);
		System.out.println("The maximum subarray sum = "+ob.maxSubSum(prefix_arr));
	}
}
class Operations{
	void printEmpty(int prefix_arr[]){
		for (int i = 0; i < prefix_arr.length; i ++){
		//	System.out.print(prefix_arr[i]+" ");
		}
	}
 	void gen_prefix(int input_arr[],int prefix_arr[]){
		for (int i = 0; i < input_arr.length; i ++){
			if ( i == 0){
				prefix_arr[i] = prefix_arr[i] * 0 + input_arr[i];
			} else {
				prefix_arr[i] = prefix_arr[i-1] + input_arr[i];
			}
		}
	}
	int maxSubSum(int prefix_arr[]){
		int max = Integer.MIN_VALUE;
		for (int i = 0; i < prefix_arr.length; i++){
			for (int j = i; j < prefix_arr.length; j++){
				if (max < (prefix_arr[j] - prefix_arr[i])){
					max = prefix_arr[j] - prefix_arr[i];
				}
			}
		}
		return max;
	}
}
