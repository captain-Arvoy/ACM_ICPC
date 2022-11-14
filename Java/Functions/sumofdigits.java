import java.util.Scanner;
public class sumofdigits{
    public static int sum(int n){
        int sum = 0;
        while (n > 0){
            sum+=n%10;
            n/= 10;
        }
        return sum;
    }
    public static void main(String args[]){
        Scanner ob = new Scanner(System.in);
        System.out.print("Enter the number: ");
        int number = ob.nextInt();
        System.out.println("The sum of digits of number = "+sum(number));
}
}