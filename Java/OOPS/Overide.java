class Superman{
    void hello(){
        System.out.println("Hello I am superman");
    }
}
class Batman extends Superman{
    @Override
    void hello(){
        System.out.println("I am Batman!");
    }
}
public class Overide {
    public static void main(String args[]){
        Batman sp = new Batman();
        sp.hello();
    }
}
