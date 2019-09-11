class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        sta = 0
        end = len(nums) - 1
        while(sta <= end):
            mid = (sta+end) / 2
            if nums[mid] < target:
                sta = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                return mid
        if nums[mid] < target:
            return mid+1
        else:
            return mid