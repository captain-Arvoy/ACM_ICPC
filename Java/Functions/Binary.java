import java.util.Scanner;
public class Binary{
    public static int binary(int n){
        int N = n, bin, place=1, num = 0;
        while (N > 0){
            bin = N%2;
            num +=bin*place;
            place *=10;
            N/=2; 
        }
        return num;
    }
    public static void main(String args[]){
        Scanner ob = new Scanner(System.in);
        System.out.print("Enter the number: ");
        int input = ob.nextInt();
        System.out.println(binary(input));
    }
}