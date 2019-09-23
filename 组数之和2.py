class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        tempans = []
        sta = 0
        def back_track(sta,Lsum):
            if Lsum == target:
                ans.append(tempans[:])
            for i in range(sta,len(candidates)):
                if i > sta and Lsum[i] == Lsum[i-1]:
                    continue
                if Lsum + candidates[i] <= target or (target < 0 and Lsum < 0):
                    tempans.append(candidates[i])
                    Lsum = Lsum + candidates[i]
                    back_track(i+1,Lsum)
                    Lsum = Lsum - candidates[i]
                    tempans.pop()
                else:
                    break
        back_track(0,0)
        return ans
            

            