public class Rhombus_solid {
    public static void print_rhombus(){
        for (int i = 1; i<=5; i++){
            for (int j = 0; j<(5-i);j++){
                System.out.print("  ");
            }
            System.out.println("* * * * * ");
        }
    }
    public static void main(String args[]){
        // Scanner ob = new Scanner(System.in);
        print_rhombus();
    }
}
