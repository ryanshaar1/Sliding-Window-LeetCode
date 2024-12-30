class Solution(object):
    def longestOnes(self, nums, k):
        left = 0
        max_length = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            max_length = right - left + 1
        return max_length
