"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s.

You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,

typically using all the original letters exactly once.
"""


class Solution:
    def findAnagrams(self, s: str, p: str):
        hash_p = 0
        for x in range(len(p)):
            hash_p += hash(p[x])
        left = 0
        right = len(p)
        res = []
        hash_another = 0
        while right < len(s) + 1:
            if not hash_another:
                for y in range(left, right):
                    hash_another += hash(s[y])
            else:
                hash_another -= hash(s[left - 1])
                hash_another += hash(s[right - 1])
            if hash_another == hash_p:
                res.append(left)
            left += 1
            right += 1
        return res


if __name__ == "__main__":
    print(Solution().findAnagrams("cbaebabacd", "abc"))
