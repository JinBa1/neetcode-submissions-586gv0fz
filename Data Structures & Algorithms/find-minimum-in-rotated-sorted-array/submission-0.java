class Solution {
    public int findMin(int[] nums) {
        int min = Integer.MAX_VALUE;  // constraint given
        for(int elem : nums) {
            min =  elem < min ? elem : min;
        }
        return min;
    }
}
