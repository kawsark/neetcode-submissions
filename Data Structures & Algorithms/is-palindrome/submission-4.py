class Solution:

    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        
        sl = s.lower()

        while i < j:
            while i < len(sl) and not sl[i].isalnum():
                i += 1
            
            while j >= 0 and not sl[j].isalnum():
                j -= 1
        
            if i < j and sl[i] != sl[j]:
                return False
            
            i += 1
            j -= 1
        
        return True
