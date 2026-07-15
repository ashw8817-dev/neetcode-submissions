class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        final_list = []
        for index, value in enumerate(strs):
            sorted_item = "".join(sorted(value))
            if sorted_item not in dictionary:
                 dictionary[sorted_item] = []
            
            dictionary[sorted_item].append(value)
        
        final_list = list(dictionary.values())

        return final_list

                

            
