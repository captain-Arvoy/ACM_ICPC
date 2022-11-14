import java.util.Scanner;
public class Question5{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the year: ");
        int year_input = sc.nextInt();
        if (year_input % 4 == 0 ){
            if (year_input % 100 == 0){
                if (year_input % 400 == 0){
                    System.out.println("It's a leap year");
                } else {
                    System.out.println("Not leap Year");
                }
            } else {
                System.out.println("Leap year");
            }
        } else{
            System.out.println("Not leap year");
        }
        sc.close();
    }
}