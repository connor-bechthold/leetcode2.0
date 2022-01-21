#My solution
#O(nlogn) time, O(n) space
class Solution:
    def countBits(self, n: int) -> List[int]:
        
        #Pretty straightforward, shift left each time and and with 1, incrementing as usual
        ret = []
        for i in range(0, n+1):
            ones = 0
            while i != 0:
                if i & 1 == 1:
                    ones += 1
                i >>= 1
            ret.append(ones)
        return ret
    
#Ideal solution
#O(n) time, O(n) space
class Solution:
    def countBits(self, n: int) -> List[int]:
        
        #Too long to explain, just looking for a pattern like normal dp stuff
        if n == 0:
            return [0]
        
        ret = []
        dp = [0] * (n+1)
        offset = 1
        for i in range(1, n+1):
            dp[i] = dp[(i - offset)] + 1
            
            if (i + 1) == 2*offset:
                offset *= 2
            
        return dp
