import java.util.Scanner;
public class Binomial {
    public static int factorial(int n){
        if (n == 1){
            return 1;
        }
        return n*factorial(n-1);
    }
    public static double binomial(int n, int r){
        double nCr =factorial(n)/(factorial(r)*factorial(n-r));
        return nCr;
    }
    public static void main (String args[]){
        int n, r;
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the n of nCr: ");
        n=sc.nextInt();
        System.out.print("Enter the r of nCr: ");
        r=sc.nextInt();
        System.out.println("The binomial coffecient is= "+binomial(n,r));
    }
    
}
