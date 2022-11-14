import java.util.Scanner;
public class Hollow_rectangle {
    public static void holrect(int no_of_row,int no_of_column){
        for (int i = 0; i < no_of_row; i++){
            for (int j = 0; j < no_of_column; j++){
                if (i==0||i==(no_of_row - 1)||j==0||(j==no_of_column - 1)){
                    System.out.print(" ");
                    System.out.print("*");
                }else{
                    System.out.print("  ");
                }
            }
            System.out.println();
        }
    }
    public static void main(String args[]){
        Scanner ob = new Scanner(System.in);
        System.out.print("Enter the number of rows: ");
        int no_of_row = ob.nextInt();
        System.out.print("Enter the number of columns: ");
        int no_of_columns = ob.nextInt();
        holrect(no_of_row,no_of_columns);
    }
}
