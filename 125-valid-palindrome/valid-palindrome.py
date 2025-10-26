class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == ' ' :
            return True

        clean_s = ""
        for char in s :
            if char.isalnum() :
                clean_s += char.lower()

        return clean_s == clean_s[::-1]