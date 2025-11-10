class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        l, maxl, maxc = 0, 0, 0

        for r in range(len(s)):
            freq[ord(s[r]) - ord("A")] += 1
            maxc = max(maxc, freq[ord(s[r]) - ord("A")])
            if (r - l + 1) - maxc > k:
                freq[ord(s[l]) - ord("A")] -= 1
                l += 1
            maxl = max(maxl, r - l + 1)

        return maxl
