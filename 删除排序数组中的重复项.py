class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        times = 0
        i = 0
        while (i<len(nums)):
            while i<len(nums)-1 and nums[i] == nums[i+1]:
                i = i+1
            nums[times] = nums[i]
            times = times+1
            i = i+1
        return times