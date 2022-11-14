import java.util.Scanner;
class Function_lobby{
	void print_occurence(int number_array[],int key, int i){
		if (i == number_array.length){
			return;
		}
		
		print_occurence(number_array,key,i+1);
		if (number_array[i] == key){
			System.out.print(i+" ");
		}
	}
}
public class Question1{
	public static void main (String args[]){
		Scanner sc = new Scanner (System.in);
		System.out.println("Enter the key to search: ");
		//Sample array for testing
		int sample_arr[] = {3,2,4,5,6,2,7,2,2};
		int key = sc.nextInt();
		Function_lobby ob = new Function_lobby();
		ob.print_occurence(sample_arr, key, 0);
	}
}
