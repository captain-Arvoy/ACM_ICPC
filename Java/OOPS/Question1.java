//print the sum, the difference, the product of two complex numbers by creating a class named 'complex'
//with separate methods for each operations whose real and imaginary parts are entered by user
import java.util.Scanner;
public class Question1{
    int[] multiply(int recived_array[][]){
        int multiply_[] = new int [2];
        multiply_[0] = recived_array[0][0] * recived_array[1][0] ;
        multiply_[1] = recived_array[0][1] * recived_array[1][1] ;
        return multiply_; 
    }
    int[] sum(int recived_array[][]){
        int sum_cmplx[] = new int [2];
        sum_cmplx[0] = recived_array[0][0] + recived_array[1][0];
        sum_cmplx[1] = recived_array[0][1] + recived_array[1][1];
        return sum_cmplx; 
    }
    int[] diff(int recived_array[][]){
        int sbtrct_cmplx[] = new int [2];
        sbtrct_cmplx[0] = recived_array[0][0] - recived_array[1][0];
        sbtrct_cmplx[1] = recived_array[0][1] - recived_array[1][1];
        return sbtrct_cmplx; 
    }
    
    public static void main(String args[]){
        Question1 q1_ob = new Question1();
        Scanner sc = new Scanner(System.in);
        int input_complex[][] = new int [2][2];
        for (int i = 0; i < 2; i++){
            System.out.println("Enter "+(i+1)+" number...");
            for (int j = 0; j < 2; j++){
                if (j == 0){
                    System.out.print("Input real part : ");
                }
                if (j == 1){
                    System.out.print("Input imaginary part : ");
                }
                input_complex[i][j] = sc.nextInt();
            }
        }
        int sum[] = q1_ob.sum(input_complex);
        int product[] = q1_ob.multiply(input_complex);
        int diff[] = q1_ob.diff(input_complex);
       System.out.println("The sum of two numbers are: "+sum[0]+"+"+sum[1]+"j"); 
       System.out.println("The product of two numbers are: "+product[0]+"+"+product[1]+"j"); 
       System.out.println("The substracton of two numbers are: "+diff[0]+diff[1]+"j"); 

    }
}