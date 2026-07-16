class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        final_list = []
        for value in strs:
            sorted_item = "".join(sorted(value))
            if sorted_item in dictionary:
                dictionary[sorted_item].append(value)
            else:
                dictionary[sorted_item] = [value]
                #sorted item becomes the key, [value] becomes value
        final_list = list(dictionary.values())

        return final_list

                

            
