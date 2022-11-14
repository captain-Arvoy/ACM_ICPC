import java.util.Scanner;
class Recursion{
    Recursion(){
        //Accessed  Recursion class!
    }
    int sum(int n){
        if (n == 0){
            return 0;
        }
        return n+sum(n-1);
    }
}
public class Sum_of_N{
    public static void main(String args[]){
        Scanner sc = new Scanner (System.in);
        int _input_;
        System.out.print("Enter N for sum of N natural numbers\nN: ");
        _input_ = sc.nextInt();
        Recursion child = new Recursion();
        System.out.println("The sum of "+_input_+" natural numbers is: "+child.sum(_input_));
    }
}

