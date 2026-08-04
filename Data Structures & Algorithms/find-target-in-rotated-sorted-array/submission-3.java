class Solution {
    public int search(int[] nums, int target) {
        int l = 0;
        int r = nums.length - 1; 

        while(l <= r) {
            int m = l + (r - l) / 2;

            if(nums[m] == target) return m;

            if (nums[m] > nums[r]) {
                if (nums[m] > target
                    && target >= nums[l]) {
                        // to the left half
                        r = m-1;
                } else {
                        // to the right half
                        l = m+1;
                }

            } else {  // nums[m] < nums[r]
                if (nums[m] < target
                    && target <= nums[r]) {
                        // to the right half
                        l = m+1;
                    } else {
                        // to the left half
                        r = m-1;
                    }
            }
        }

        return -1;
    }
}
