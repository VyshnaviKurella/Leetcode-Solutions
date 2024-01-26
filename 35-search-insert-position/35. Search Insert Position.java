class Solution {
    public int searchInsert(int[] nums, int target) {
        int lowval=0;
        int highval=nums.length-1;
         while(lowval<=highval){
            int mid = (lowval+highval)/2;
            if(nums[mid] == target) 
               return mid;
            else if(nums[mid] > target) 
              highval = mid-1;
            else 
             lowval = mid+1;
            
        }
        return lowval;
    }
}