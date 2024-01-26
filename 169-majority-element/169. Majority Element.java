class Solution {
    public int majorityElement(int[] nums) {
         Arrays.sort(nums);
         int count= 1, maxElement=nums[0];
        for( int index = 1; index <nums.length; index++)       
        {  
            if( nums[index-1]==nums[index])
            { count++;
              if(count > nums.length/2)
               maxElement=nums[index];
            }
          else
            count=1;
        }
        return maxElement; 
    }
}