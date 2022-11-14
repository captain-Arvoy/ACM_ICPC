import java.util.Scanner;
public class Hw1 {
    public static void main(String args[]){
        Scanner sc = new Scanner (System.in);
        System.out.print("Enter the string: ");
        String string = sc.nextLine();
        //output
        System.out.println("No. of lower case vowels are: "+check_vowels(string));
    }
    public static int check_vowels(String string){
        int c = 0;
        for (int i =  0; i < string.length(); i++){
            if (string.charAt(i) == 'a' || string.charAt(i) == 'e' || string.charAt(i) == 'i' ||string.charAt(i) == 'o' ||string.charAt(i) == 'u' ){
                c++;
            }

        }
        return c;
    }
}
 