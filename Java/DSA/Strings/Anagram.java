                                    //THE PROGRAM IS COMPLETE
import java.io.IOException;
import java.util.Scanner;
public class Anagram{
    public static void checkpalindrome(String formal_argument, String formal_argument2){
        //converting the strings to lower case so that we don't have to check separately for uppercase
        formal_argument = formal_argument.toLowerCase();
        formal_argument2 = formal_argument2.toLowerCase();
        int sum = 52;
        /*Here I applied the algorithm that-
         *given 2 Strings,there
         * the sum of differences of unicode of characters is equal to 0 
         * it has time complexity of O(n)
        */
        // If the strings don't have same length then how can they ever be eligible for palindrome.
        if (formal_argument.length() != formal_argument2.length()){
            System.out.println("The words are not eligible to be palindrome");
        } else {
            sum = 0;
            for (int i = 0; i < formal_argument.length(); i++){
                sum += (formal_argument.charAt(i)-formal_argument2.charAt(i));
            }
        }
        if (sum == 0){
            System.out.println("The Strings are palindrome");
            //The program actually ends in line 20
            //The below code is to check the success of my algorithm against brute force 
            boolean cross_check = check(formal_argument,formal_argument2);
            if (cross_check){
                System.out.println("Success");
            } else{
            System.out.println("fail");
            }
        } else {
            System.out.println("The strings are not palindrome");
        }
    }
    public static void main(String args []){
        Scanner sc = new Scanner (System.in);
        System.out.print("Enter the 1st String: ");
        String input = sc.next();
        System.out.print("Enter the 2nd String: ");
        String input2 = sc.next();
        checkpalindrome(input,input2);
    }
    //Below function uses brute force method O(n^2)
    public static boolean check(String formal_argument,String formal_argument2) {
        int count = 0;
        for (int i = 0; i < formal_argument.length(); i++){
            for (int j = 0; j < formal_argument2.length(); j++){
                if (formal_argument.charAt(i) == formal_argument2.charAt(j)){
                    count++;
                }

            }
        }
        if (count == formal_argument.length()){
            return true;
        } else {
            return false;
        }
    }
}