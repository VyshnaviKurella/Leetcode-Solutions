class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
       HashSet<Integer> list1 = new HashSet<Integer>();
       HashSet<Integer> list2 =new HashSet<Integer>();
       ArrayList<Integer> resList= new ArrayList<Integer>();
       for(int i=0;i<nums1.length;i++)
           list1.add(nums1[i]);
       for(int i=0;i< nums2.length;i++)
           list2.add(nums2[i]);
       if(list1.size()<list2.size())
      { for (int i: list1)
           if(list2.contains(i) )
           resList.add(i);
      }  
      else
      for (int i: list2)
          if( list1.contains(i))
          resList.add(i);

 int[] returnList =new int[resList.size()];
for(int i=0;i<resList.size();i++)
    returnList[i]=resList.get(i);
for(int i=0;i<resList.size();i++)
{
    System.out.println(returnList[i]);
}
return returnList;
    }
}