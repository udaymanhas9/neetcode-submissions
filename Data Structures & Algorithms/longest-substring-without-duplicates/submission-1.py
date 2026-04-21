class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        longest = 0
        start_of_current = 0

        for i in range(len(s)):
            if s[i] in seen and seen[s[i]] >= start_of_current:
                start_of_current = seen[s[i]] + 1

            seen[s[i]] = i
            longest = max(longest, i - start_of_current + 1)

        return longest
        