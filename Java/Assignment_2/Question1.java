import java.util.Scanner;
public class Question1 {
    public static void main(String args[]){
        int a,b,c,avg;
        Scanner in = new Scanner(System.in);
        System.out.print("Input a: ");
        a = in.nextInt();
        System.out.print("Input b: ");
        b = in.nextInt();
        System.out.print("Input c: ");
        c = in.nextInt();
        avg =( a + b + c)/3;
        System.out.println("The average of three numbers = "+avg);
        in.close();
    }
    
}
