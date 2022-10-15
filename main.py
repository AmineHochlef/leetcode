class Solution(object):
    def plusOne(self, digits):
        s=0
        digits=digits[::-1]
        for i in range(len(digits)):
            s=s+digits[i]*(10**i)
        sus+1
        S=[int(x) for x in str(s)]
        for i in range (len(S)):
            digits[i]=int(S[i])
        return(digits)
        