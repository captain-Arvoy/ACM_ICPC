import java.io.*; // for handling input/output
import java.util.*; // contains Collections framework

// don't change the name of this class
// you can add inner classes if needed
class Test1 {
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);
        int n,m;
        n = sc.nextInt();
        m = sc.nextInt();
        int counter = 0;
        int array[][] = new int[n][m];
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m;j++){
            for (int j = 0; j < m;j++){
                array[i][j] = sc.nextInt();
            }
        }
        //solution
        for (int i = 0; i < n; i++){
                if (array[i][j] != 0){
                    counter++;
                }
            }
        }
        System.out.println(counter);
    }
}