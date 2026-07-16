class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        
        for string in strs:
            sorted_word = "".join(sorted(string))
            if sorted_word in seen:
                seen[sorted_word].append(string)
            else:
                seen[sorted_word] = [string]
        return list(seen.values())
            


                

            