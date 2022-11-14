public class Transpose {
    public static void transpose(int matrix[][]){
        int no_of_rows = matrix.length;
        int no_of_columns = matrix[0].length;
        int transpose[][]=new int[no_of_columns][no_of_rows];
        for (int i = 0; i < no_of_rows; i++){
            for (int j = 0; j < no_of_columns; j++){
                transpose[j][i] = matrix[i][j];
            }
        }
        //printing transpose matrix
        for (int i = 0; i < no_of_columns; i++){
            for (int j = 0; j < no_of_rows; j++){
                System.out.print(transpose[i][j]+" ");
            }
            System.out.println();
        }
    }
    public static void main (String args[]){
        int matrix[][] = {{4,7,8},{5,9,7}};
        transpose(matrix);
    }
}
