public class Diagonalsum {
    public static void sumofdiagonal(int matrix[][]){
        int primary_sum = 0, secondary_sum = 0;
        //O(n^2) approach a.k.a Brute force
        for (int i = 0; i < matrix.length ; i++){
            for (int j = 0; j < matrix[0].length; j++){
                if (i == j){
                    primary_sum += matrix[i][j];
                    
                } else if (i+j == matrix.length - 1) {
                    secondary_sum += matrix[i][j]; 
                }
            }
        }
        System.out.println("{O(n^2)}:\n"+"Total sum = "+(primary_sum+secondary_sum));
        //O(n) approach
        for (int i = 0; i < matrix.length; i++){
            primary_sum += matrix[i][i];
            if (i!= (matrix.length - 1 -i)){ 
                secondary_sum += matrix[i][matrix.length-1-i];
            }
        }
        System.out.println("{O(n)}:\n"+"Total sum = "+(primary_sum+secondary_sum));
    }
    public static void main(String args[]){
        int arr[][] = {{1,2,3,4},
                       {5,6,7,8},
                       {9,10,11,12},
                       {13,14,15,16}};
        sumofdiagonal(arr);
    }
    
}
