class Solution {
    public boolean hasDuplicate(int[] nums) {
        for(int i = 0; i < nums.length; i++){
            for(int l = 0; l < nums.length; l++){
                if(i!=l && (nums[i] == nums[l])){
                    return true;
                }
            }
        }
        return false;
    }
}