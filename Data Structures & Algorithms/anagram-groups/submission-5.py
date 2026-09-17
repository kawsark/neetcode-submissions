class Solution:
  
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for i in range(len(strs)): #act, pots
            key_list = sorted(strs[i])
            key = "".join(key_list)

            if key in anagrams:
                anagrams[key].append(strs[i])
            else:
                anagrams[key] = [strs[i]]
        
        return list(anagrams.values())

    
    
    def isAnagram(self, a: list, b: list):
        if len(a) != len(b):
            return False

        comp = [0]*26

        for i in range(len(a)):
            comp[ord(a[i])-ord('a')] += 1
            comp[ord(b[i])-ord('a')] -= 1
        
        for i in comp:
            if i != 0:
                return False

        return True

        

        