from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1,len2 = len(s1),len(s2)

        if len1 > len2 :
            return False

        s1_freq = [0]*26
        win_freq = [0]*26

        for ch in s1 :
            s1_freq[ord(ch)-ord('a')] += 1
        
        for i in range(len1) :
            win_freq[ord(s2[i])-ord('a')] += 1

        if s1_freq == win_freq :
            return True

        for i in range(len1,len2) :
            win_freq[ord(s2[i])-ord('a')] += 1
            win_freq[ord(s2[i-len1])-ord('a')] -= 1

            if s1_freq == win_freq :
                return True

        return False