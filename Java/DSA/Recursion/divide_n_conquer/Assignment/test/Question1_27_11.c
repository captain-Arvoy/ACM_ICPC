class Solution {
    public int pivotInteger(int n) {
              int lSum = 0, rSum = 0;
        for (int k = 1; k < n; k++){
                  for ( int i = 1; i <= k; i++ ) {
                     lSum += i;
                  }   
                  for ( int j = k; j <= n; j++){
                     rSum += j; 
                  }
                  if (lSum == rSum){
                      return k;
                  }
                lSum = rSum = 0;
              
        }
        return -1;
    }
}
/* Instead of starting the sum from the start you can use what I call save state*/ 
