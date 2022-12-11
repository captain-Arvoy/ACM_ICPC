public class Sorting {
    public static void bubblesort(int arr[]){
        for (int i = 0; i < arr.length; i++){
            for (int j = 0; j < arr.length - i - 1; j++){
                if (arr[j] > arr [j+1]){
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }
        for (int i = 0; i < arr.length; i++){
            System.out.print(arr[i]+" ");
        }
    }

    public static void selectionsort(int arr[]){
        int max_ka_index,temp;
        for (int i = 0; i < arr.length; i++){
            max_ka_index = i;
            for (int j = i+1; j < arr.length-1; j++){
                if (arr[j] > arr[j+1]){
                    max_ka_index = arr[j+1];/***DOUBT***
                                                Arey max_ka_index should store index na */
                }
            }
            temp = arr[max_ka_index];
            arr[max_ka_index] = arr[i];
            arr[i] = temp;
        }
        for (int i = 0; i < arr.length; i++){
            System.out.print(arr[i]+" ");
        }
    }

    public static void insertionsort(int arr[]){
        for (int i = 1; i < arr.length; i++){
            int prev = i-1, temp = arr[i], index_of_temp = i;
            //It just seeks the correct place to place the protagonist, with swaping the side kicks at the same time.
            while (prev >= 0 && arr[prev] > temp){
                arr[index_of_temp] = arr[prev];
                index_of_temp = prev;
                prev--;
            }
            arr[index_of_temp] = temp;
        }
        for (int i = 0; i < arr.length; i++){
            System.out.print(arr[i]+" ");
        }
    }

    public static void countingsort(int arr[]){
        int largest_number = Integer.MIN_VALUE;
        for (int i = 0; i < arr.length; i++){
            largest_number = Math.max(largest_number, arr[i]);
        }
        int counting[] = new int[largest_number+1];
        int sorted_array[] = new int[arr.length];
        int sorted_array_marker = 0;
        for (int i = 0; i < arr.length; i++){
           int element_of_arr = arr[i];
            counting[element_of_arr]++;
        }
        for (int i =0; i < counting.length; i++){
            
            while (counting[i] > 0){
                sorted_array[sorted_array_marker] = i;
                sorted_array_marker ++;
                counting[i]--;
            }
        }
        for (int i = 0; i < sorted_array.length; i++){
            System.out.print(sorted_array[i]+" ");
        }
        
    }
    public static void main(String args[]){
        int arr[] = {3, 6, 2, 1, 8, 7, 4, 5, 3, 1};
        System.out.print("Bubble sort:\n");
        bubblesort(arr);
        System.out.print("\n-----------------------\nSelection sort:\n");
        selectionsort(arr);
        System.out.println();
        System.out.print("------------------------\ninsertion sort:\n");
        insertionsort(arr);
        System.out.println();
        System.out.print("--------------------------\ncounting sort:\n");
        countingsort(arr);
    }

}
