class Solution(object):
    def longestSubarray(self, nums):
        left = 0
        zero_count = 0
        maxx = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            if zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            maxx = right - left
        return maxx
