public class Diamond {
    public static void print_diamond(){
        for (int i = 1; i <=4 ; i++){
            for (int j = 4; j > i ; j--){
                System.out.print("  ");
            }
            for (int k = 0 ; k < (2*i-1);k++){
                System.out.print("* ");
            }
            System.out.println();
        }
        for (int i = 1; i <=4 ; i++){
            for (int j = 1; j < i ; j++){
                System.out.print("  ");
            }
            for (int k = 0 ; k < (9-2*i);k++){
                System.out.print("* ");
            }

            System.out.println();
        }
    }
    public static void main(String args[]){
        // Scanner ob = new Scanner(System.in);
        print_diamond();
    }
}
