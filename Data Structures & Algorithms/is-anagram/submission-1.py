class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_word1 = sorted(s)
        sorted_word2 = sorted(t)
        if sorted_word1 == sorted_word2:
            return True
        else: return False