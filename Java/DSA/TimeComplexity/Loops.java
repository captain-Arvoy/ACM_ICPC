public class Loops{
	public static void main(String args[]){
		for (int i = 0;i < 10; i = i+2){
			for (int j = i+1; j <= 2; j++){
				System.out.printf("%d ",j);
			}
			System.out.println();
		}
	}
}
