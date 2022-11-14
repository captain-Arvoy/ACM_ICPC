// #correct complete program
// time complexity = log(n)
import java.util.Scanner;
public class Exponentiation {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the base: ");
        int base = sc.nextInt();
        System.out.print("Enter the exponent: ");
        int power = sc.nextInt();
        exponent(base,power);
    }    
    public static void exponent(int base, int power){
        int n_base = base, ans = 1, n_power = power;
        while (power > 0){    
            if ((power & 1) != 0){//checking Least significant bit
                ans = ans*base;
            }
            //else likhne ki zaroorat nahi hai kyunki agar 0 hua toh 1 multiply ho jayega ans ke saath
            //if you did not get then dry run it
            power = power>>1;//shifting the bit to right hand side aka shifting the bit traverser to left 
            base = base*base;
        }
        System.out.println(n_base+"^"+n_power+"="+ans);
    }
}
