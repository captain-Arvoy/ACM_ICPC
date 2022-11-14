import java.util.Scanner;
public class Inverted_star{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of lines of star: ");
        int line = sc.nextInt();
        for (int line_iterator = 0; line_iterator < line; line_iterator++){
            for (int star = line; star > line_iterator; star--){
                System.out.print("*");
            }
            System.out.println();
        }
        
    }
}