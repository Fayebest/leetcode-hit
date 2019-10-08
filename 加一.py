class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        flag = 0
        for i in range(len(digits)-1,-1,-1):
            temp = digits[i]+1
            flag = 0
            if temp == 10:
                flag = 1
                digits[i] = 0
            else:
                digits[i] = temp
                break
        if flag == 1:
            digits.insert(0,1)
        return digits