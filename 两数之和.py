class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        elem = {}
        for i in range(0,len(nums)):
            elem[nums[i]] =i
        for i in range(0,len(nums)):
            temp = target - nums[i]
            if elem.has_key(temp) and i != elem[temp]:
                return [i,elem[temp]]
        
		
