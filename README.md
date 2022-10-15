# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution(object):
    def plusOne(self, digits):
        s=0
        newDigits=[]
        digits=digits[::-1]
        for i in range(len(digits)):
            s=s+digits[i]*(10**i)
        s=s+1
        S=[int(x) for x in str(s)]
        for i in range (len(S)):
            newDigits.append(int(S[i]))
        return(newDigits)
        

                
```