class Solution {
    public int singleNumber(int[] nums) {
       int nonRepetitiveNumber= nums[0];
       for(int index=1; index<nums.length; index++)
       {
           nonRepetitiveNumber= nonRepetitiveNumber ^ nums[index];
       }
      return nonRepetitiveNumber;
    }
}