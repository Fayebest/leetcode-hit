class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        flag = 0
        i = 0
        for i in range(len(nums)-1,0,-1):
            if nums[i] > nums[i-1]:
                for j in range(len(nums)-1,0,-1):
                    if nums[j] > nums[i-1]:
                        temp = nums[j]
                        nums[j] = nums[i-1]
                        nums[i-1] = temp
                        flag = 1
                        break
            if flag == 1:
                break
        index = 0
        if flag == 0 and i == 1:
            i = 0
        for j in range(i,(len(nums)+i)/2):
            temp = nums[j]
            nums[j] = nums[len(nums)-1 - index]
            nums[len(nums)-1 - index] = temp
            index = index+1
            
                