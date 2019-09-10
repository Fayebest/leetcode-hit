class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = self.half_search(nums,target,0)
        sta = 0
        end = 0
        if ans == -1:
            return [-1, -1]
        if ans > 0 and nums[ans-1] == target:
            sta = half_search(nums,target,1)
        else:
            sta = ans
        if ans < len(nums) - 1 and nums[ans+1] == target:
            end = half_search(nums,target,2)
        else:
            end = ans
        return [sta,end]
        

    def half_search(self, nums, target, flag): # flag =1 left   flag=2 right
        sta = 0
        end = len(nums)-1
        while sta <= end:
            mid = (sta + end) / 2
            if nums[mid] < target:
                sta = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                if nums[mid] == target and flag == 1:
                    if mid > 0 and nums[mid - 1] == target:
                        end = mid-1
                    else:
                        return mid
                elif nums[mid] == target and flag == 2:
                    if mid < len(nums) -1 and nums[mid +1 ] == target:
                        sta = mid + 1
                    else:
                        return mid
                elif flag == 0:
                    return mid  
        return -1

                
