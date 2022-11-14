import java.util.Scanner;
public class Inverted_star_pyramid {
    public static void print(int rows){
        for (int i = 1; i <= rows; i++){
            for (int j = 1; j <= (rows - i); j++){
                System.out.print(" ");
            }
            for (int k = 1; k <= i; k++){
                System.out.print("*");
            }
            System.out.println();
        }
    }
    public static void main(String args[]){
        Scanner ob = new Scanner(System.in);
        System.out.print("Enter the number of rows to print: ");
        int rows = ob.nextInt();
        print(rows);
        ob.close();
        
    }
}    
