public class Butterfly {
    public static void pattern_butterfly(){
                
        
    //***********************************************************BLOCK 1*************************************************************************
    
    
    
        for (int i = 1; i <= 5; i++){
            //-------------------------1st quadrant-------------------------------------------------            
            for (int j = 5; j > (5-i); j--){
                System.out.print("* ");
            }
            for (int k = (5-i); k > 0; k--){
                System.out.print("  ");
            }
            //-------------------------1st quadrant-------------------------------------------------            
            //-------------------------2nd quadrant-------------------------------------------------            
            for (int m = (5-i); m > 0; m--){
                System.out.print("  ");
            }
            for (int l = 5; l > (5-i); l--){
                System.out.print("* ");
            }
            System.out.println();
            //-------------------------2nd quadrant-------------------------------------------------            
        }


    //**********************************************************BLOCK 2*************************************************************************



        for (int i = 5; i > 0; i--){
            //-------------------------3rd quadrant-------------------------------------------------            
            for (int j = 1; j <= i; j++){
                System.out.print("* ");
            }
            for (int k = (5-i); k > 0; k--){
                System.out.print("  ");
            }
            //-------------------------3rd quadrant-------------------------------------------------            
            //-------------------------4th quadrant-------------------------------------------------            
            for (int m = (5-i); m > 0; m--){
                System.out.print("  ");
            }
            for (int l = 1; l <= i; l++){
                System.out.print("* ");
            }
            System.out.println();
            //-------------------------4th quadrant-------------------------------------------------            
        }
    }
    public static void main(String args[]){
        pattern_butterfly();
        String a ="correct";
        String  b = "wrong";
        String c = 5>6? a : b;
    }
}
