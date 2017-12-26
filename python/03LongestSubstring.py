class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        frontier = 0
        maximum = 0
        dictionary = dict()
        for i in range(len(s)):
            if s[i] not in dictionary:
                maximum = max(maximum, i-frontier+1)
            else:
                if dictionary[s[i]] >= frontier:
                    maximum = max(maximum, i-dictionary[s[i]])
                    frontier = dictionary[s[i]] + 1
                else:
                    maximum = max(maximum, i-frontier+1)
            dictionary[s[i]] = i
        return maximum
                    

if __name__ == '__main__':
    obj = Solution()
    print obj.lengthOfLongestSubstring("tmmzuxt")