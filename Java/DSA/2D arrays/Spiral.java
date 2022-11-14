public  class Spiral{
    public static void printspiral(int arr[][]){
        int startrow = 0, endrow = arr.length-1,startcol = 0, endcol = arr[0].length-1;
        while(startrow <= endrow && startcol <= endcol){
            //printing top
            for (int col = startcol; col <= endcol; col++){
                System.out.print(arr[startrow][col]+" ");
            }
            //printing right
            for (int row = startrow+1; row <= endrow; row++){
                System.out.print(arr[row][endcol]+" ");
            }
            //printing bottom
            for (int col = endcol-1; col >= startcol; col--){
                System.out.print(arr[endrow][col]+" ");
            }
            //printing left
            for (int row = endrow-1; row > startrow; row--){
                System.out.print(arr[row][startrow]+" ");
            }
            startrow++;startcol++;endrow--;endcol--;
        }
    }
    public static void main(String args[]){
        int arr2[][] = {{1,2,3,4},
                       {5,6,7,8},
                       {9,10,11,12},
                       {13,14,15,16}};
        int arr[][] = {{1,2,3,4,5},
                       {5,6,7,8,9},
                       {10,11,12,13,14},
                       {15,16,17,18,19},
                       {20,21,22,23,24}};
        printspiral(arr);
    }
}