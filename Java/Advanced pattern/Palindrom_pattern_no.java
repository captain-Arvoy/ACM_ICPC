public class Palindrom_pattern_no {
    public static void main(String args[]){
        printpali();
    }

    public static void printpali(){
        for (int i = 1; i <= 5; i++){
            for (int j = 5; j > i; j--){
                System.out.print("  ");
            }
            for (int k = i; k >= 1; k--){
                System.out.print(k+" ");
            }
            for (int l = 2; l <= i; l++){
                System.out.print(l+" ");
            }
            System.out.println();
        }
    }
    
}
