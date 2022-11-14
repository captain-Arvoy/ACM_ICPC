import java.util.Scanner;
public class Captalise{
    public static void main(String args[]){
        Scanner ob = new Scanner(System.in);
        System.out.print("->");
        int choice = ob.nextInt();
        String _input_variable_;
        switch(choice){
            case 0:
                System.out.print("Enter the String to capitalise: ");
                _input_variable_ = ob.nextLine();
                break;
            default:
                _input_variable_ = "Hare krsna hare krsna krsna krsna hare Hare Hare/ hare Ram hare Ram Ram Ram hare hare";
        }
        System.out.println("The original String is: \n"+_input_variable_+"\nThe capitalised string is: \n"+caps(_input_variable_));
    }
    public static String caps(String _variable_) {
        StringBuilder ob2 = new StringBuilder("");
        for (int i = 0; i < _variable_.length() ; i++){
            if (_variable_.charAt(i) == ' ' && (i + 1) != _variable_.length() - 1){
                ob2.append(_variable_.charAt(i));
                ob2.append(Character.toUpperCase(_variable_.charAt(i+1)));
                i++;/*so that when the program doesn't copy again the letter at i+1
                    *that is after line 22(a.k.a  space) the control should traverse 'r' not k again */
            } else {
                ob2.append(_variable_.charAt(i));
            }
        }
        return ob2.toString();
    }
}