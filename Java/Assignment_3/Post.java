import java.util.Scanner;
public class Post{
    public static void main(String args[]){
        Scanner ob = new Scanner(System.in);
        int a = 0,b = a ,c = a;
        while (b < 10){
            c = b++;
            System.out.println("value of a: "+a+"\nvalue of b:"+b+"\nvalue of c: "+c);
            b = a++;
            
            ob.nextLine();
        }
    }
}