class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        sta = 0
        end = len(height) - 1
        maxArea = 0
        while sta < end:
            tempArea = (end - sta)* min(height[sta],height[end])
            if tempArea > maxArea :
                maxArea = tempArea
            if height[sta] > height[end]:
                end = end - 1
            else:
                sta = sta + 1
        return maxArea
            