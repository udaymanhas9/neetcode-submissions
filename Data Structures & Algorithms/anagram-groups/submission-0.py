class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _dic = defaultdict(list)

        for string in strs:
            print(sorted(string))
            _dic["".join(sorted(string))].append(string)

        return [values for values in _dic.values()]



