class Solution:
    def permute(self, nums):
        ans =[]
        self.backtrack(nums,ans,0)
        return ans

    def backtrack(self,nums,ans,sta):
        if sta == len(nums):
            ans.append(nums)
            print(nums)
        for i in range(sta,len(nums)):
            temp = nums[sta]
            nums[sta] = nums[i]
            nums[i] = temp
            self.backtrack(nums,ans,sta+1)
            temp = nums[sta]
            nums[sta] = nums[i]
            nums[i] = temp

a = Solution()
ans = a.permute([1,2,3])
print(ans)
