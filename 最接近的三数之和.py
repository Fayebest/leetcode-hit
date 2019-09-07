class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        near = nums[0] + nums[1] + nums[2]
        nums.sort()
        i = 0
        while i < (len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                tempsum = nums[i] + nums[j] + nums[k]
                temp = target - tempsum
                if abs(temp) < abs(target - near):
                    near = tempsum
                if target - tempsum > 0:
                    j = j + 1
                elif target - tempsum < 0:
                    k = k - 1
                else:
                    return near
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i = i + 1
            i = i + 1
        return near