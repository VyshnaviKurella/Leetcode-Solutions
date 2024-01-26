class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {  
        HashMap<Integer, Integer> res = new HashMap<>();
        res.put(0, 0);
        int sum = 0;
        for(int i = 0; i < nums.length; i++){
            sum += nums[i];           
            if(!res.containsKey(sum % k)){  
                res.put(sum % k, i + 1);
            }
            else if(res.get(sum % k) < i){    
                return true;
            }
        }
        return false;
        
    }
}