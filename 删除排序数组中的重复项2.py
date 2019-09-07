class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        times = 0
        i = 0
        while i < len(nums):
            nums[times] = nums[i]
            times = times+1
            if i < len(nums)-1 and nums[i] == nums[i+1]:
                nums[times] = nums[i+1]
                times = times+1
                i = i+1
            while i<len(nums)-1 and nums[i] == nums[i+1]:
                i=i+1
            i=i+1
        return times
                