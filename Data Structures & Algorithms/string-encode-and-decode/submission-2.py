class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res
    def decode(self, s: str) -> List[str]:
        n = len(s)
        i = 0
        ans = []
        while i < n:
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            i = j+1
            j = i + length

            ans.append(s[i:j])
            i = j
        return ans
    