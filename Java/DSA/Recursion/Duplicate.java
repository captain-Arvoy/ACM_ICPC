import java.util.Scanner;
public class Duplicate{
	public static void main(String args[]){
		String _input_string = new String();
		boolean map[] = new boolean[26];
		Scanner sc = new Scanner (System.in);
		//System.out.print("Enter the string: ");
		_input_string = "Appnnacoolegee";
		Main_  obj = new Main_();
		StringBuilder unique = new StringBuilder();
		//calling check_duplicate of Main_
		obj.check_duplicate(_input_string.length()-1,map,_input_string,unique);
	}
}
class Main_{
	void check_duplicate(int i,boolean map[],String _input_string,StringBuilder unique){
		if (i < 0){
			return;
		}
		check_duplicate(i-1,map,_input_string,unique);
		int character =Character.toUpperCase( _input_string .charAt(i)) - 'A';
		if (map[ character] == false){
			map[character] = true;
			check_duplicate(i-1,map,_input_string,unique.append(_input_string.charAt(i)));
		}
		if (i == _input_string.length()-1){
			System.out.println(unique);
			return;
		}
		return;
	}
}
