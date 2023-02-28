"""
Given a string s, find the length of the longest substring without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        left = right = 0
        slide = ""
        max_length = 0
        while right < len(s):
            slide = s[left:right]
            while s[right] in slide and left < right:
                max_length = max(max_length, len(slide))
                left += 1
                slide = s[left:right]
            right += 1
        slide = s[left:]
        return max(max_length,len(slide))