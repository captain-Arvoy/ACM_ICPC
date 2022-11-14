
import java.util.Scanner;
public class Question2 {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int n, i = 1, fact = 1;
        System.out.print("Enter the number to find the factorial of:");
        n = sc.nextInt();
        if (n == 0){
            System.out.println("The factorial of "+n+" is"+0);
        }else{
            while (i <= n ){
                fact*=i;
                i++;
            }
        }
        System.out.println("The factorial of "+n+" is "+fact);
    }
    
}
