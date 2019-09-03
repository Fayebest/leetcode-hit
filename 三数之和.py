class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        elem = {}
        for i in range(len(nums)):
            elem[nums[i]] = i
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                k = 0 - nums[i] - nums[j];
                if elem.has_key(k) and elem[k] > j:
                    ans.append([i,j,k])
        return ans