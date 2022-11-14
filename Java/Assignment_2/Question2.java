import java.util.Scanner;
public class Question2 {
    public static void main(String args[]){
        Scanner ob = new Scanner(System.in);
        float side, area;
        System.out.print("Enter the side of the square: ");
        side = ob.nextFloat();
        area = side*side;
        System.out.println("The area of the square is: "+area);
        ob.close();
    }
    
}
