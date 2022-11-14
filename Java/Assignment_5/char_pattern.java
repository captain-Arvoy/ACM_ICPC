import java.util.Scanner;
public class char_pattern {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the Number of lines of characters to print: ");
        int char_uni = 65;
        int line = sc.nextInt();
        for (int line_iterator = 1; line_iterator <= line; line_iterator++){
            for (int star = 1; star <= line_iterator; star++){
                System.out.print((char)char_uni);
                char_uni++;
            }
            System.out.println();
        }
        
    }
}
