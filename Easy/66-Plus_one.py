class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [0] + digits 
        i = len(digits)-1
        while(i >=0):
            digits[i] += 1
            if(digits[i] <10):
                break
            digits[i] = 0
            i-=1
        if(digits[0] == 0): return digits[1:]
        return digits