"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        new_arr = []
        p_1 = p_2 = 0
        while p_1 < len(nums1) and p_2 < len(nums2):
            if nums1[p_1] <= nums2[p_2]:
                new_arr.append(nums1[p_1])
                p_1 += 1
            else:
                new_arr.append(nums2[p_2])
                p_2 += 1
        while p_1 < len(nums1):
            new_arr.append(nums1[p_1])
            p_1 += 1
        while p_2 < len(nums2):
            new_arr.append(nums2[p_2])
            p_2 += 1
        len_arr = len(new_arr)
        if len_arr & 1 == 0:
            return (new_arr[int(len_arr/2)] + new_arr[int(len_arr/2-1)])/2
        else:
            return float(new_arr[int(len_arr/2)])

if __name__ == "__main__":
    print(Solution().findMedianSortedArrays([1,2],[3,4]))