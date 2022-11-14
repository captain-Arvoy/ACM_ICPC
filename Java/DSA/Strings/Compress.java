import java.util.Scanner;
public class Compress{
    public static void main(String args[]){
        Scanner sc = new Scanner (System.in);
        System.out.print("--->");
        String choice = sc.next();
        String _input;
        switch(choice){
            case "input":
                _input = sc.nextLine();
                break;
            default: 
                System.out.println("Expected output: a4e4io4uk5l4p");
                _input = "aaaaeeeeiooooukkkkkllllp";
                break;
        }
        String output = compressstring(_input);
        System.out.println("Output: "+output);
        if (output.equals("a4e4io4uk5l4p") ){
            System.out.println("Success");
        } else {
            System.out.println("Try again");
        }
    }
    public static String compressstring(String uncompressed_string){
        StringBuilder sb = new StringBuilder("");
        int counter = 0;
        for (int i = 0; i < uncompressed_string.length();){
            char check_char = uncompressed_string.charAt(i);
            counter = 0;
            while (i < uncompressed_string.length() && uncompressed_string.charAt(i) == check_char){
                counter++;
                i++;
            }
            if (counter > 1){
                sb.append(check_char);
                sb.append(counter);
            } else {
                sb.append(check_char);
            }
        }
        return sb.toString();
    }
}