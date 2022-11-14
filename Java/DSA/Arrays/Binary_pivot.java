//wrong program
/**the whole code is just for show off
if not then correct the code now non sense*/ 
import java.util.Scanner;
public class Binary_pivot {
    public static int findpivot(int arr[]){
        int pivotpoint = 0;
        for (int i = 0; i < arr.length-1; i++){
            if (arr[i] > arr[i+1]){
                pivotpoint = i;
            }
        }
        return pivotpoint;
    }
    public static int whichblock(int target, int arr[]){
        if (target < arr[0]){
            return 2;
        } else if (target == arr[0]){
            return 3;
        }else{
            return 1;
        }
        
    }
    public static void binarysearch(int arr[], int target){
        int ch = whichblock(target, arr);
        int pivotpt = findpivot(arr);
        switch (ch){
            case 1:
/* #debug1*/    System.out.println("*The target is in block 1*");

                int start1 = 0, end1 = pivotpt, mid = (start1+end1)/2;
                while (start1<=end1){
                    if (target < arr[mid]){
                        end1 = mid -1;
                        mid = (start1+end1)/2;
                    } 
                    else if (target == arr[mid]) {
                        System.out.println(mid);
                        break;
                    }else {
                        start1 = mid + 1;
                        mid = (start1+end1)/2;
                    }
                }
                break;
            case 2:
/* #debug1.2*/  System.out.println("*The target is in block 2*");
                int start2 = pivotpt + 1, end2 = arr.length - 1, mid2 = (start2 + end2) / 2;
                while (start2<=end2){
                    if (target < arr[mid2]){
                        end2 = mid2 - 1;
                        mid2 = (start2+end2) / 2;
                    } else if (target == arr[mid2]){
                        System.out.println("The target is found at "+mid2);
                        break;
                    }else {
                        start2 = mid2 + 1;
                        mid2 = (start2 + end2)/2; 
                    }
                }
                break;
            case 3:
                System.out.println(0);
                break;
            default:
                System.out.println("The target is not present in array.");
                break;
        }   
        
    }
    public static void main (String args[]){
        Scanner sc = new Scanner (System.in);
        System.out.print("Enter the size of array to input: ");
        int size_of_array = sc.nextInt();
        int arr [] = new int [size_of_array];
        for (int i  = 0; i < size_of_array; i++){
            System.out.print("Enter the "+(i+1)+"st element: ");
            arr[i] = sc.nextInt();
        }
        System.out.print("Enter the target: ");
        int target = sc.nextInt();
        binarysearch(arr, target);
        sc.close();
    }
}
