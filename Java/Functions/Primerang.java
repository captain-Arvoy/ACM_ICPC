//Program for printing prime numbers
import java.util.Scanner;
import java.math.*;
public class Primerang{
    public static boolean prime(double number){
        boolean isPrime = true;
        for (int i = 2; i <= Math.sqrt(number); i++){
            if (number % i == 0){
                isPrime = false;
            }
        }
        return isPrime;
    }
    public static void main(String args[]){
        Scanner ob = new Scanner(System.in);
        System.out.print("Enter the limit to find the prime in the range: ");
        int limit = ob.nextInt();
        for (int i = 2; i <= limit; i++){
            if (prime(i) == true){
                System.out.print(i+" ");
            }
        }
    }
}