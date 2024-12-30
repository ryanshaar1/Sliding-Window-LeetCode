class Solution(object):
    def maxVowels(self, s, k):
        vowels = {'a','e','i','o','u'}
        current_maxV = 0
        for i in range(k):
            if s[i] in vowels:
                current_maxV+=1
        maxV = current_maxV
        for i in range(k,len(s)):
            if s[i] in vowels:
                current_maxV+=1
            if s[i-k] in vowels:
                current_maxV-=1
            if current_maxV > maxV:
                maxV = current_maxV
        return maxV
                    
