class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag = 0
        for i in range(0,len(nums)):
            if nums[i] == 1:
                flag = 1
            elif nums[i] <= 0 or nums[i]>len(nums):
                nums[i] = 1
        if flag == 0:
            return 1
        for i in range(0,len(nums)):
            if abs(nums[i]) == len(nums):
                nums[0] = -nums[0]
            elif nums[abs(nums[i])] > 0:
                nums[abs(nums[i])] = -nums[abs(nums[i])]
        for i in range(1,len(nums)):
            if nums[i] > 0:
                return i
        if nums[0] > 0:
            return len(nums)
        return len(nums)+1
        