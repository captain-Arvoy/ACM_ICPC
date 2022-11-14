public class Rhombus_hollow {
    public static void print_rhombus_hollow(){
        for (int i = 1; i <= 5 ; i++){

            for (int k = 5; k > i; k--){
                System.out.print("  ");
            }

            for (int j = 1; j <= 5; j++){
                if (j==5||j==1||i==1||i==5){
                    System.out.print("* ");
                }else{
                    System.out.print("  ");
                }
            }
            System.out.println();
        }
    }
    public static void main(String args[]){
        // Scanner ob = new Scanner(System.in);
        print_rhombus_hollow();
    }
}
