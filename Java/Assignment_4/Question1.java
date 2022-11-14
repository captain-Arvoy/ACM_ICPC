public class Question1 {
    public static void main (String args[]){
        int even_sum = 0, odd_sum = 0;
        for (int i = 0; i < 100; i++ ){
            if (i%2 == 0){
                even_sum += i;
            }else{
                odd_sum += i;
            }
        }
        System.out.println("The sum of odd integers= "+odd_sum+"\nThe sum of even integers= "+even_sum);
    }
}
