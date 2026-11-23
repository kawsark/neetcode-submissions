# Meta: '{"felt":"easy","Time":"25,"Help":"none","Comment":""}'

class Solution:
  
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = {}

        for word in strs:
            word_list = list(word)
            word_list.sort()
            key = "".join(word_list)

            if key in anagrams_dict:
                anagrams_dict[key].append(word)
            else:
                anagrams_dict[key] = [word]
        
        result = []
        for key in anagrams_dict:
            result.append(anagrams_dict[key])
        
        return result

