import java.util.Scanner;
public class Question1{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int number;
        System.out.print("Enter a number to check: ");
        number = sc.nextInt();
        sc.close();
        if (number > 0){
            System.out.println("The number "+number+" is positive");
        } 
        else if (number < 0) {
            System.out.println("The number"+number+"is negative");
        } else{
            System.out.println("Number is zero. //Are you comedy me");
        }
    }
}