class Solution:
    def firstUniqChar(self, s: str) -> int:
        l = len(s)
        count = collections.Counter(s)
        for i in range(l):
            if count[s[i]] == 1:
                return i
        return -1