import java.util.Scanner;
class Recursion_class{
	int printfactorial(int n){
		if (n == 1){
			return 1;
		}
		return n*printfactorial(n-1);
	}
}

public class Factorial{
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		Recursion_class rc = new Recursion_class();
		System.out.print("Enter the number: ");
		int n = sc.nextInt();
		System.out.println(rc.printfactorial(n));
	}
}
