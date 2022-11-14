import java.util.Scanner;
public class Dis_hw {
    public static int order(String menu[],String key){
        for (int i = 0; i < menu.length; i++){
            if (menu[i].equals(key)){
                return 1;
            }
        }
        return -1;
    }
    public static void main(String args[]){
        Scanner ob = new Scanner(System.in);
        String menu[] = {"Dosa","Samosa","Chole bhature","kadi","Thepla","Masala Dosa"};
        System.out.print("Enter your wish: ");
        String key = ob.nextLine();
        int index = order(menu,key);
        if (index == -1){
            System.out.println("Sorry we don't have the dish today :( ");
        }else{
            System.out.println("I could smell the dish, coming soon!");
        }
        ob.close();
    }    
}
