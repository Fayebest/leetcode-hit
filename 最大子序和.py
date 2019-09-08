class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsubsum = nums[0]
        nowsum = 0
        flag = 0
        for i in range(0,len(nums)):
            if flag == 1 and nums[i] > 0:
                nowsum = nums[i]
                flag = 0
                if nowsum > maxsubsum:
                    maxsubsum = nowsum
            else:
                nowsum = nowsum + nums[i]
                if nowsum > maxsubsum:
                    maxsubsum = nowsum
                if nowsum < 0:
                    flag = 1
                    nowsum = 0
        return maxsubsum
                