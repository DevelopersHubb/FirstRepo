"""Given an array, Rotate (shift left) an array of n elements to the right by k steps.
For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated
to [5,6,7,1,2,3,4].
After rotating the array add in into another array and display array index with
minumum value."""

public void rotate(int[] nums, int k) {
    if (k > nums.length) 
        k = k % nums.length;
 
    int[] result = new int[nums.length];
 
    for (int i = 0; i < k; i++) {
        result[i] = nums[nums.length - k + i];
    }
 
    int j = 0;
    for (int i = k; i < nums.length; i++) {
        result[i] = nums[j];
        j++;
    }
 
    System.arraycopy(result, 0, nums, 0, nums.length);
}