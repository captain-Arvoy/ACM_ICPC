public class Matrixsorting{
    public static void search_in_array(int arr[][],int key){
        int row = arr.length - 1;
        int column = 0;
        
        while (column <= arr.length - 1 && row >=0){
            if (key < arr[row][column]){
                row--;
            } else if (key > arr[row][column]){
                column++;
            } else {
                System.out.println("Element found at ("+(row+1)+","+(column+1)+")");
                break;
            }
        }
    }
    public static void main (String args[]){
        int matrix[][] = {{10,20,30,40},
                          {15,25,35,45},
                          {27,29,37,48},
                          {32,33,39,50}},key = 35;
        search_in_array(matrix,key);   
    }
}