"""Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle."""


class Maximum_Subarray:
    def brute_force(self, nums):

        for i in range(len(nums)):
            for j in range(i):
                print(nums[j])
            print("\n")

    def kadane(self, nums):
        max_curr = max_global = nums[0]
        # Starting from 1 for case of single value in nums.
        for i in range(1, len(nums)):
            max_curr = max(nums[i], nums[i] + max_curr)
            if(max_curr > max_global):
                max_global = max_curr
        return max_global


a = Maximum_Subarray()
print(a.kadane([1]))
