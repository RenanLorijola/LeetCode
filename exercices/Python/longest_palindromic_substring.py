class Solution:
    maxLength = 0
    start = 0
    def longestPalindrome(self, s: str) -> str:
        lenght = len(s)
        
        if lenght == 1:
            return s
        for i in range(lenght-1):
            self.extendPalindrome(s, i, i)
            self.extendPalindrome(s, i, i+1)
        return s[self.start: self.start+self.maxLength]

    def extendPalindrome(self, s: str, j: int, k: int):
        while j >= 0 and k < len(s) and s[j] == s[k]:
            j-=1
            k+=1
        if self.maxLength < k - j - 1:
            self.start = j + 1
            self.maxLength = k - j -1

    

solution = Solution()
print(solution.longestPalindrome("a"))