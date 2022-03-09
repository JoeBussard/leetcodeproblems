#!/bin/python

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = nums1 + nums2
        nums3.sort()
        if len(nums3) & 1:
            return nums3[(len(nums3)-1)/2]
        else:
            if len(nums3) == 0:
                return 0
            return (float(nums3[len(nums3)/2]) + float(nums3[len(nums3)/2 -1])) / 2.0
