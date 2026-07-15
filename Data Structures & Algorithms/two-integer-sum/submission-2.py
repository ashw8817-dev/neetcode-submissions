class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#goal: in a list of numbers along with a provided target, 
#find the indexes of 2 different numbers that add to the target
#plan: start with an empty dictionary to track numbers we have seen already
#get each index of each number in the list
#check if there is more numbers in the list to go through
#get the number from the index and store both in the dictionary
#in the dictionary, the index is the key, number is value
        dictionary = {}
        
        for i, num in enumerate(nums):
            missing_number = target - num
            if missing_number in dictionary:
                return [dictionary[missing_number], i]
            else:
                dictionary[num] = i
            



                

            
            

                
                
                
            
