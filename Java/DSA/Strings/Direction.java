import java.util.Scanner;
import java.math.*;
public class Direction {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        String input = new String();
        System.out.print("Enter the direction String: ");
        input = sc.next();
        System.out.println("The displacement travelled is: "+cal_disp(input));
    }
    public static double cal_disp(String input){
        //origin
        int x = 0, y = 0;
        for (int i = 0; i < input.length(); i++){
            if (input.charAt(i) == 'E'){
                x++;
            } else if (input.charAt(i) == 'W'){
                x--;
            } else if (input.charAt(i) == 'N'){
                y++;
            } else if (input.charAt(i) == 'S'){
                y--;
            }
        }
        double displacement = Math.sqrt((Math.pow(x,2)+Math.pow(y,2)));
        return displacement;
    }
}
