class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        for string in strs:
            hash_map[''.join(sorted(string))].append(string)

        ans = []
        for lst in hash_map.values():
            ans.append(lst)
        
        return ans