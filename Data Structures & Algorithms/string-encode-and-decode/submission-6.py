class Solution:

    def encode(self, strs: List[str]) -> str:
        return '#o#'.join(strs) + '#o#' if len(strs) else '' 
    def decode(self, s: str) -> List[str]:
        return s.split('#o#')[:-1]