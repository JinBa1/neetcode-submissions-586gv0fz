class Solution {
    private int binaryMin(int[] nums, int start, int end) {
        int mid = start + (end - start) / 2;

        // terminal condition

        if (start == end) {
            return nums[end];
        }


        if (nums[mid] > nums[end]) {
            return binaryMin(nums, mid+1, end);
        } else {
            return binaryMin(nums, start, mid);
        }
    }



    public int findMin(int[] nums) {
        return binaryMin(nums, 0, nums.length-1);
    }
}
