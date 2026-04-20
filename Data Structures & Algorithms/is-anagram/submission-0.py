class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        _dic = defaultdict(int)
        for char in s:
            _dic[char] += 1
        for char in t:
            _dic[char] -= 1
        
        for element in _dic.values():
            if element != 0:
                return False
        return True