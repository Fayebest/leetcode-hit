class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        end = len(nums) - 1
        i = 0
        while i <= end:
            if nums[i] == val:
                while i < end and nums[end] == val:
                    end = end - 1
                    count = count + 1
                nums[i] = nums[end]
                count = count + 1
                end = end - 1
            i = i + 1
        return len(nums) - count