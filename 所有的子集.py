class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.backtrack(nums,0,[])
        return self.ans
    
    def backtrack(self,nums,sta,path):
        self.ans.append(path[:])
        for i in range(sta,len(nums)):
            path.append(nums[i])
            self.backtrack(nums,i+1,path)
            path.pop()