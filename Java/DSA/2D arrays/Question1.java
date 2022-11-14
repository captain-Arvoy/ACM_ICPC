import java.util.Scanner;
public class Question1{
    public static int extrema_matrix(int matrix[][]){
        int largest = Integer.MIN_VALUE, smallest = Integer.MAX_VALUE;
        for (int i = 0; i < matrix.length; i++){
            for (int j = 0; j < matrix[0].length; j++){
                if (largest < matrix[i][j]){
                    largest = matrix[i][j];
                }
                if (smallest > matrix[i][j]){
                    smallest = matrix[i][j];
                }
            }
        }
        return largest;
    }
    public static void main(String args[]){
        Scanner ob = new Scanner(System.in);
        int matrix[][] = new int [3][3];
        for (int i = 0; i < matrix.length; i++){
            for (int j = 0; j < matrix[0].length; j++){
                System.out.print("Enter ("+i+", "+j+") element: ");
                matrix[i][j] = ob.nextInt();
            }
        }
        System.out.println("The largest number in the matrix respectively is: "+extrema_matrix(matrix));
    }
}