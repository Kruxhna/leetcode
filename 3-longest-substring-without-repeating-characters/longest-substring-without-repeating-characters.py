class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mpp = [-1]*256
        r,l,length,n = 0,0,0,len(s)

        while r < n :
            if mpp[ord(s[r])] != -1 :
                l = max(mpp[ord(s[r])]+1,l)
            mpp[ord(s[r])] = r
            length = max(length,r-l+1)
            r += 1
        return length