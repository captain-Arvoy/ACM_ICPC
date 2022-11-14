import java.util.Scanner;
public class half_pyramid {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of lines of star: ");
        int line = sc.nextInt();
        for (int line_iterator = 1; line_iterator <= line; line_iterator++){
            for (int star = 1; star <= line_iterator; star++){
                System.out.print(star);
            }
            System.out.println();
        }
        
    }
    
}
