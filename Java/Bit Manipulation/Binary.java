import java.util.Scanner;
public class Binary{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        char loop = 'y';
        int input_no;
        while (loop == 'y'){
            System.out.print("Enter the number: ");
            input_no = sc.nextInt();
            System.out.println("~"+input_no+"= "+(~input_no));
            System.out.print("Continue? [y/n]: ");
            loop = sc.next();
        }
    }
}