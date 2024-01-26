class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        ArrayList<Integer> mp = new ArrayList<>();
        for(int i=0;i<nums2.length;i++)
           mp.add(nums2[i]);

        for(int i=0;i<nums1.length;i++){
            int index = mp.indexOf(nums1[i]);
            int res= -1;
            for(int j=index+1;j<nums2.length;j++)
            {   
               if(nums2[j]> nums1[i])
               {
                   res = nums2[j];
                   j= nums2.length;
               }

            }
            nums1[i]=res;
        }
         
         return nums1;
    }
}