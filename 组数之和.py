class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        tempans = []
        sta = 0
        def back_track(sta,Lsum):
            if Lsum == target:
                ans.append(tempans[:])
            for i in range(sta,len(candidates)):
                if Lsum + candidates[i] <= target or (target < 0 and Lsum < 0):
                    tempans.append(candidates[i])
                    Lsum = Lsum + candidates[i]
                    back_track(i,Lsum)
                    Lsum = Lsum - candidates[i]
                    tempans.pop()
                else:
                    break
        back_track(0,0)
        return ans
            

            