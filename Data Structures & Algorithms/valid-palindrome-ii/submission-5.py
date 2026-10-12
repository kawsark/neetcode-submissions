class Solution:
    def validSlice(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        
        return True

    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] == s[j]:
                pass
            else:
                if s[i+1] == s[j] or s[i] == s[j-1]:
                    return self.validSlice(s[i+1:j+1]) or self.validSlice(s[i:j])
                else:
                    return False

            i += 1
            j -= 1
        
        return True