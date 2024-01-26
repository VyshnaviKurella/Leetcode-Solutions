class Solution {
    public void moveZeroes(int[] nums) {
        int intcount=0;

        for(int i=0;i<nums.length;i++)
        {
            if(nums[i]!=0)
            {
                nums[intcount]=nums[i];
                intcount++;
            }
        }
        while(intcount<nums.length)
        {
            nums[intcount]=0;
            intcount++;
        }
        
    }
}