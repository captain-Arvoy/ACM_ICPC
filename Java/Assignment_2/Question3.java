import java.util.Scanner;
public class Question3 {
    public static void main(String args[]){
        Scanner ob = new Scanner(System.in);
        float cost_of_pencil, cost_of_pen, cost_of_eraser, total_cost, gst_cost;
        System.out.print("Enter the cost of pencil: ");
        cost_of_pencil = ob.nextFloat();
        System.out.print("Enter the cost of pen: ");
        cost_of_pen = ob.nextFloat();
        System.out.print("Enter the cost of eraser: ");
        cost_of_eraser = ob.nextFloat();
        total_cost = cost_of_pencil + cost_of_pen + cost_of_eraser;
        System.out.println("The total cost = "+total_cost);
        gst_cost = total_cost + (0.18f)*(total_cost);
        System.out.println("The total cost of the things are (incl. of all taxes): "+gst_cost);
        ob.close();
    }    
    
    
}
