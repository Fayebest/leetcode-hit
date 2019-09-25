class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        tempans = []
        used = [0 for i in range(len(nums))]
        def back_track():
            if len(tempans) == len(nums):
                ans.append(tempans[:])
            for i in range(len(nums)):
                if used[i] == 0:
                    if i > 0 and nums[i] == nums[i-1] and nums[i-1] == 0:
                        continue
                    used[i] = 1
                    tempans.append(nums[i])
                    back_track()
                    used[i] = 0
                    tempans.pop()
        back_track()
        return ans