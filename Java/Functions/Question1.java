import java.util.Scanner;
public class Question1{
    public static int avg(int a, int b, int c){
        int avg = (a + b + c)/3;
        return avg;
    }
    public static void main(String args[]){
        Scanner ob = new Scanner(System.in);
        System.out.print("Enter the 1st number: ");
        int a = ob.nextInt();
        System.out.print("Enter the 2nd number: ");
        int b = ob.nextInt();
        System.out.print("Enter the 3rd number: ");
        int c = ob.nextInt();
        System.out.println("The average of 3 numbers = "+avg(a,b,c));
    }
}