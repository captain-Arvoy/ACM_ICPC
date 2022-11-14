import java.io.*; // for handling input/output
import java.util.*; // contains Collections framework

// don't change the name of this class
// you can add inner classes if needed
public class Q1{
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);
        int number_of_tests = sc.nextInt();
        int input_array[][] = new int [number_of_tests][3];
        for (int i = 0; i < number_of_tests; i++){
            for (int j = 0; j < 3 ; j++){
                if (sc.hasNextInt()){
                       input_array[i][j] = sc.nextInt();
                }
            }
        }
        for (int i = 0; i < number_of_tests; i++){
            if (input_array[i][0] == input_array[i][1] && input_array[i][1] == input_array[i][2]){
                System.out.println("Yes");
            } else {
                System.out.println("No");
            }
        }

    }
}