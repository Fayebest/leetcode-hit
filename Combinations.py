class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        tempans = []
        def back_track(sta,n,k):
            if len(tempans) == k:
                ans.append(tempans[:])
            else:
                for i in range(sta,n+1):
                    tempans.append(i)
                    back_track(i+1,n,k)
                    tempans.pop()
        back_track(1,n,k)
        return ans