import java.util.Scanner;
public class Stock {
    public static int buyandsellstock(int nic[]){
        int buyprice = nic[0];
        int sellprice = 0;
        int profit = Integer.MIN_VALUE, max_profit = Integer.MIN_VALUE, day_of_bussiness = 0; 
        for (int i = 0; i < nic.length; i++){
            sellprice = nic[i];
            if (sellprice > buyprice){
                profit = sellprice - buyprice;
            }else{
                buyprice = sellprice;
            }
            if (max_profit < profit){
                max_profit = profit;
                day_of_bussiness = i + 1;
            }
        }
        return day_of_bussiness;
    }
    public static void main (String args[]){
        Scanner sc = new Scanner (System.in);
        int pricearray[] = {7,1,5,3,6,4};
        // System.out.print("Enter the total number of days: ");
        // int totaldays = sc.nextInt();
        // int pricearray[] = new int [totaldays] ;
        // for (int i = 0; i < totaldays; i++){
        //     System.out.print("Enter the "+i+"st elements of array: ");
        //     pricearray[i] = sc.nextInt();
        // }
        System.out.println(buyandsellstock(pricearray));
    }
}
