class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_hash = defaultdict(int)

        for char in s:
            char_hash[char] += 1
        
        for char in t:
            char_hash[char] -= 1

        for val in char_hash.values():
            if val != 0:
                return False

        return True
        
