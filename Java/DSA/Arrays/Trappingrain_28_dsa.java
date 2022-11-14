public class Trappingrain_28_dsa{
    public static int totalwater(int height[]){
        int n = height.length, watersum = 0;
        int leftmax[] = new int[n];
        int rightmax[] = new int[n];
        int waterheight;
        leftmax[0] = height [0];
        rightmax[n-1] = height [n-1];
        for (int i = 1; i < n; i++){
            leftmax[i] = Math.max(height[i],leftmax[i-1]);
        }
        for (int j = n-2; j >=0; j--){
            rightmax[j] = Math.max(height[j],rightmax[j+1]);
        }
        for (int i = 0; i < n; i++){
            waterheight = Math.min(leftmax[i],rightmax[i]);
            watersum += (waterheight - height[i])*1;
        }
        return watersum;
    }
    public static void main(String args[]){
        int height[] = {4,2,0,3,2,5};
        System.out.print("{");
        for (int i = 0; i < height.length; i++){
            if ( i+1 < height.length){
                System.out.print(height[i]+", ");
            } else{
                System.out.print(height[i]);
            }
        }
        System.out.println("}");
        System.out.println(totalwater(height));
    }
}