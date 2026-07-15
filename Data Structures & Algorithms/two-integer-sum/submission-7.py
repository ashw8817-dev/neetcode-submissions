class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#goal: in a list of numbers along with a provided target, 
#find the indexes of 2 different numbers that add to the target
#plan: start with an empty dictionary to track numbers we have seen already
#for each index and value in numbers
#find missing number for each index (target-num)
#if missing_number is seen already: return missing number index and index
#else: store the number as the key and index as the value 
#so that on the next iteration the dictionary's key is now the index
#e.g. num = 2 i = 0, stores {2:0} in the dict. so the number "2" 
#is at index 0, and this is added to the "already seen" dictionary

        dictionary = {}
        for index, num in enumerate(nums):
            missing_num = target - num
            if missing_num in dictionary:
                return [dictionary[missing_num], index]
            else:
                dictionary[num] = index
        
                
            



                

            
            

                
                
                
            
