class Math_{
    int power (int base, int index){
        if (index == 0){
            return 1;
        }
        int product = base * power(base , index-1);
        return product;
    }
}
//Driver code   
public class Power {
    public static void main(String args[]){
        Math_ ob = new Math_();
		Optimisation ob2 = new Optimisation();
        System.out.println("Optimized: "+ob2.optimizedPower(3,3));
        System.out.println("non Optimized: "+ob.power(3,3));

    }
}
class Optimisation{
	public static int optimizedPower(int a,int n){
		if (n == 0){
			return 1;
		}
		int halfPowerSq = optimizedPower(a,n/2);
		halfPowerSq *= halfPowerSq;
		//n is odd
		if (n%2 != 0){
			halfPowerSq = a * halfPowerSq;
		}
		return halfPowerSq;
	}
}
