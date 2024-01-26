class Solution {
    public int climbStairs(int n) {
       if(n <= 1) 
       return 1;
       int val1 = 1 , val2 = 2;
       for(int i = 3; i <= n; i ++) {
           int totalcount = val1 + val2;
           val1 = val2;
           val2 = totalcount;
       } 
       return val2;
    }
}