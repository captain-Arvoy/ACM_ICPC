import java.util.Scanner;
public class Question3{
    public static int checkpalindrome(int n){
        int N = n;
        int sum=0; 
        while (N > 0){
            int rem = N % 10;
            sum = sum*10 + rem;
            N = N / 10;
        }
        return sum;
    }
    public static void main(String args[]){
        Scanner ob = new Scanner(System.in);
        System.out.print("Enter the number: ");
        int number = ob.nextInt();
        int reverse = checkpalindrome(number);
        if (reverse == number){
            System.out.println(number+" is palindrome number.");
        }else{
        System.out.println(number+" is not palindrome number.");
    }
    }
}