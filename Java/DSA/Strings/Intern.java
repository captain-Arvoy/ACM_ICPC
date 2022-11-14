
public class Intern {
    // public static void check_scope_of_intern(){
    //     String b = "Hari".intern();
    //     /*this must print true because varibles are stored in stack 
    //     *whereas SCP(String constant pool) is stored in heap
    //     */
    // }
    public static void main(String args[]){
        String a = "Hari".intern();
        String c = "Hari";
        // check_scope_of_intern();
        String b = new String("Hari");
        System.out.println(a==b);
    }
}
