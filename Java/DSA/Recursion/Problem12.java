import java.util.Scanner;
public class Problem1{
	public static boolean unique(Stringbuilder formal_parameter,int index){
		boolean map[] = new boolean[26];
		System.out.println("Boolean = "+map[4]);
		if (index == formal_parameter.length()){
			return;
		}
		if (map[(int)formal_parameter.charAt(index)] == true){
			unique(formal_parameter, index+1);
		} else {
			map[(int)formal_parameter.charAt(index)] = true; 
		}
	}
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		System.out.print("Enter the String: ");
		Stringbuilder _input_String = sc.next();
	
	}
}
		
		
