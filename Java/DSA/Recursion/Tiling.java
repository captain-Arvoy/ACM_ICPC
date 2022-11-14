// Approach 
/*step1: choice
		Every time there is a tile there is choice whether to put it horizontal or vertical 
  Step2: kaam
  		1 tile dalne ke baad f(n-1) ke liye *b dalne hai
		-Vertical: Agar tile vertical then call f(n-1)
		-Horizontal: Agar tile horizontal toh call f(n-2) kyunki agar 1tile horizontal hai dusra bhi horizontal hoga.
		Total ways = f(n-1)+ f(n-2)*/
import java.util.Scanner;
public class Tiling{
	public static void main(String args[]){
		Scanner sc = new Scanner (System.in);
		int n;
		System.out.print("Enter the value of n: :");
		n = sc.nextInt();
		Engine ob = new Engine();
		System.out.println(ob.tilingproblem(n));
	}
}
class Engine{
	int tilingproblem(int n){
		//base case
		if (n == 0 || n == 1){
			return 1;
		}
		//kaam 
		//vertical choice
		int fn1 = tilingproblem(n-1);
		//horoizontal choice 
		int fnm2 = tilingproblem(n-2);
		int totways = fnm1 + fnm2;
		return totways;
	}
}
