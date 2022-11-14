import java.util.Scanner;
class arraysum_algorithm {
    public int[] ignition_code(){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter choice for arrays (0- for system default array 1: your choice array ): ");
        int ch = sc.nextInt();
        System.out.println();
        switch(ch){
            case 0:
//                int numbers[] = {-2,-3,4,-1,-2,1,5,-3};
                int numbers[] = {3,2,1,5,4:};
                return numbers;
            case 1:
                System.out.print("Enter the size of the array: ");
                int size = sc.nextInt();
                System.out.println();
                int number[] = new int[size]; 
                for (int i = 0 ; i < size; i++){
                    System.out.print("Enter "+(i+1)+"th element of array: ");
                    number[i] = sc.nextInt();
                    System.out.println();
                }
            return number;
            default:
            System.out.println("Only 1 and 2 is available as options!");
            return null;
        }
        
    }
    public void printSubarrays(int number[]) {
        int sum;
        System.err.println("Entered Subarrays");
        Scanner sc = new Scanner(System.in);
        int choice = 1;
        switch(choice){
        case 1:
            for (int i = 0; i < number.length; i++) {
                int max = Integer.MIN_VALUE, min = Integer.MAX_VALUE;
                for (int j = i; j < number.length; j++) {
                    System.out.print("(");
                    sum = 0;
                    for (int k = i; k <= j; k++) {
                        System.out.print(number[k]);
                        sum += number[k];
                        if (sum < min) {
                            min = sum;
                        } else if (sum > max) {
                            max = sum;
                        }
                        if (k != j) {
                            System.out.print(",");
                        }
                    }
                    System.out.print(")");
                    System.out.print("Sum = " + sum);
                    System.out.print("  ");
                }
                System.out.println();
                if (max == Integer.MIN_VALUE) {
                    System.out.print("\n|| The maximum sum = N/A ;The minimum sum = " + min);
                } else {
                    System.out.print("\n|| The maximum sum = " + max + ";The minimum sum = " + min);
                }
                System.out.println();
            }
            break;
        // case 2:
        //     for (int i = 0; i < number.length; i++) {
        //         int max = Integer.MIN_VALUE, min = Integer.MAX_VALUE;
        //         for (int j = i; j < number.length; j++) {
        //             System.out.print("(");
        //             sum = 0;
        //             for (int k = i; k <= j; k++) {
        //                 System.out.print(number[k]);
        //                 sum += number[k];
        //                 if (sum < min) {
        //                     min = sum;
        //                 } else if (sum > max) {
        //                     max = sum;
        //                 }
        //                 if (k != j) {
        //                     System.out.print(",");
        //                 }
        //             }
        //             System.out.print(")");
        //             System.out.print("Sum = " + sum);
        //             System.out.print("  ");
        //         }
        //         if (max == Integer.MIN_VALUE) {
        //             System.out.print("|| The maximum sum = N/A ;The minimum sum = " + min);
        //         } else {
        //             System.out.print("|| The maximum sum = " + max + ";The minimum sum = " + min);
        //         }
        //         System.out.println();
        //     }
        
    }
}

    public void prefix_maxsum(int numbers[]) {
        int n = numbers.length;
        int max_sum = Integer.MIN_VALUE;
        int current_sum = 0;
        int prefix[] = new int[n];
        prefix[0] = numbers[0];
        //creating prefix sum array
        for (int i = 1; i < n; i++) {
            prefix[i] = numbers[i] + prefix[i - 1];
        }
        for (int j = 0; j < n; j++) {
            int start = j;
            for (int k = 0; k < n; k++) {
                int end = k;
                current_sum = start == 0 ? prefix[end] : prefix[end] - prefix[start - 1];
                if (current_sum > max_sum) {
                    max_sum = current_sum;
                }
            }
        }
        System.out.println("The maximum Sum is: "+max_sum);
    }
    
    public void kadane_algorithm(int numbers[]){
        int n = numbers.length, max_sum = Integer.MIN_VALUE, current_sum = numbers[0];
        for (int i = 0; i < n; i++){
            current_sum += numbers[i];
            if (current_sum < 0){
                current_sum = 0;
            }
            max_sum = Math.max(max_sum,current_sum);
        }
        System.out.println("The maximum sum of the array: "+max_sum);
}
}
public class Subarrays{
    public static void main(String args[]) {
        Scanner mainscanner = new Scanner(System.in);
        arraysum_algorithm aS = new arraysum_algorithm();
        int numbers [] = aS.ignition_code();
        System.out.print("which way you want to find maxsum:-\n(1)bruteforce\n(2)prefix method\n(3)Kadane algorithm\n>");
        int choice = mainscanner.nextInt();
        switch(choice){
            case 1:
                aS.printSubarrays(numbers);
                break;
            case 2: 
                aS.prefix_maxsum(numbers);
                break;
            case 3:
                aS.kadane_algorithm(numbers);
                break;
            default:
                System.out.println("Internet option search kariyo mile to batana....idhar nahi milega");
        }
    }
}
