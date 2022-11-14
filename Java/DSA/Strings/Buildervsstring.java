//To check if String is same as String builder converted to String 
public class Buildervsstring{
    public static void main (String args[]){
        StringBuilder ob = new StringBuilder("Hello");
        String a = ob.toString();
        String b = new String("Hello");
        if (a == b){
            System.out.println("String builder is same as String");
        }else {System.out.println(a==b);}
        
    }
}