class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict

        anagrams_map = defaultdict(list)

        for word in strs :
            sorted_word = tuple(sorted(word))
            anagrams_map[sorted_word].append(word)

        return list(anagrams_map.values())